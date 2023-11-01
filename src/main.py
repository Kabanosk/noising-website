from fastapi import FastAPI, Request, File, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from utils import ZipDataset

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/')
def noise_files(
        request: Request,
        zip_file: bytes = File(),
        downsampling: str = Form(""),
        output_filename: str = Form("")
):
    files = ZipDataset(zip_file)
    if downsampling == 'true':
        files.downsample(8000)
    files.save(output_filename)
    return None

