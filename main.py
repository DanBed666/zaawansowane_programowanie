from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import shutil
import detect

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/result", response_class=HTMLResponse)
async def root(request: Request, file: UploadFile = File(...)):

    try:
        with open(f'{file.filename}', "wb") as buffer:
            buffer.write(file.file.read())
            shutil.copyfileobj(file.file, buffer)

        people, img = detect.pict(buffer.name)

        return templates.TemplateResponse("result.html", {"request": request, "people": people, "myImage": img})
    except (AttributeError, FileNotFoundError):
        return templates.TemplateResponse("index.html", {"request": request, "message": "Niepoprawny format pliku!"})


@app.get("/result", response_class=HTMLResponse)
async def root(request: Request, file: UploadFile = File(...)):

    try:
        with open(f'{file.filename}', "wb") as buffer:
            buffer.write(file.file.read())
            shutil.copyfileobj(file.file, buffer)

        people, img = detect.pict(buffer.name)

        return templates.TemplateResponse("result.html", {"request": request, "people": people, "myImage": img})
    except (AttributeError, FileNotFoundError):
        return templates.TemplateResponse("index.html", {"request": request, "message": "Niepoprawny format pliku!"})
