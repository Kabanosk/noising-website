from fastapi import FastAPI, Request, File, Form
from fastapi.templating import Jinja2Templates

from utils import ZipDataset

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/')
def noise_files(request: Request, zip_file: bytes = File(), downsampling: str = Form("")):
    files = ZipDataset(zip_file)
    if downsampling == 'true':
        files.downsample(8000)
    return None

