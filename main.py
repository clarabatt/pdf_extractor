from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from typing import Union
import process_image

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(req: Request):
    return templates.TemplateResponse("home.html", {"request": req})

@app.post("/upload")
async def upload_file(req: Request, file: UploadFile or None = None):
    if not file:
        return templates.TemplateResponse("home.html", { "request": req, "text":  "No file uploaded"})
    else:
        text = process_image.extract(file.filename)
        return templates.TemplateResponse("home.html", { "request": req, "text":  text})

