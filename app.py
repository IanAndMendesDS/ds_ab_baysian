import numpy as np
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
    if np.random.random() < 0.5:
        return templates.TemplateResponse(
            name='pg_layout_red.html',
            context={"request": request},
            request=request,
        )
    else:
         return templates.TemplateResponse(
            name='pg_layout_blue.html',
            context={"request": request},
            request=request,
        )

@app.post('/yes')
async def yes_event(request: Request):
    return RedirectResponse(url='/home', status_code=303)

@app.post('/no')
async def no_event(request: Request):
    return RedirectResponse(url='/home', status_code=303)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)