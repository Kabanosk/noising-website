from fastapi import FastAPI, Request, File, Form
from fastapi.templating import Jinja2Templates

from utils import downsample, prepare_zip_file

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/')
def noise_files(request: Request, zip_file: bytes = File(), downsampling: str = Form("")):
    files = prepare_zip_file(zip_file)
    if downsampling == 'true':
        downsample(files)
    return None

