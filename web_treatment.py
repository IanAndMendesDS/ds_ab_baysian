import numpy as np
import pandas as pd
from fastapi import FastAPI, Request
from fastapi import Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="./templates")


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return Response(status_code=204)


@app.get('/home')
async def home(request: Request):
    return templates.TemplateResponse(
    name='pg_layout_red.html',
    context={"request": request},
    request=request,
    )
  

@app.post('/yes')
async def yes_event(request: Request):
    df = pd.read_csv('data/data_experiment.csv')
    click = 1
    visit = 1
    group = 'treatment'
    df_raw = pd.DataFrame({'click': click, 'visit': visit, 'group': group}, index=[0])
    df = pd.concat([df, df_raw])
    df.to_csv('data/data_experiment.csv', index=False)
    return RedirectResponse(url='/home', status_code=303)

@app.post('/no')
async def no_event(request: Request):
    df = pd.read_csv('data/data_experiment.csv')
    click = 0
    visit = 1
    group = 'treatment'
    df_raw = pd.DataFrame({'click': click, 'visit': visit, 'group': group}, index=[0])
    df = pd.concat([df, df_raw])
    df.to_csv('data/data_experiment.csv', index=False)
    return RedirectResponse(url='/home', status_code=303)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)