import numpy as np
import pandas as pd
from fastapi import FastAPI, Request
from fastapi import Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from scipy.stats import beta

app = FastAPI()
templates = Jinja2Templates(directory="../templates")


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return Response(status_code=204)


@app.get('/home')
async def home(request: Request):
    #get data
    df = pd.read_csv('../data/data_experiment.csv')

    df['no_click'] = df['visit'] - df['click']
    click_array = df.groupby('group').sum().reset_index()[['click', 'no_click']].T.to_numpy()

    # Thompson Agent
    prob_reward = np.random.beta(click_array[0], click_array[1])

    if np.argmax(prob_reward) == 0:
        return templates.TemplateResponse(
            name='pg_layout_blue.html',
            context={"request": request},
            request=request,
        )
    else:
         return templates.TemplateResponse(
            name='pg_layout_red.html',
            context={"request": request},
            request=request,
        )

@app.post('/yes')
async def yes_event(request: Request):
    df = pd.read_csv('../data/data_experiment.csv')
    form = await request.form()
    if form.get('yescheckbox') == 'red':
        visit = 1
        click = 1
        group = 'treatment'
    else:
        visit = 1
        click = 1
        group = 'control'

    df_raw = pd.DataFrame({'click':click, 'visit':visit, 'group': group}, index=[0])
    df = pd.concat([df, df_raw])
    df.to_csv('../data/data_experiment.csv', index=False)

    return RedirectResponse(url='/home', status_code=303)

@app.post('/no')
async def no_event(request: Request):
    df = pd.read_csv('../data/data_experiment.csv')
    form = await request.form()
    if form.get('nocheckbox') == 'red':
        visit = 1
        click = 0
        group = 'treatment'
    else:
        visit = 1
        click = 0
        group = 'control'

    df_raw = pd.DataFrame({'click':click, 'visit':visit, 'group': group}, index=[0])
    df = pd.concat([df, df_raw])
    df.to_csv('../data/data_experiment.csv', index=False)

    return RedirectResponse(url='/home', status_code=303)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
