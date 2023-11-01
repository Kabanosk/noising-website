# Website that helps me prepare a dataset for my Engineering Thesis
## How to run the application
### With uvicorn
1. Clone the repo - `git clone git@github.com:Kabanosk/noising-website.git`
2. Go to repo directory - `cd whisper-website`
3. Create virtual environment - `python3 -m venv venv`
4. Activate the environment - `source venv/bin/activate` / `. venv/bin/activate`
5. Install requirements - `pip install -r requirements.txt`
6. Go to src directory - `cd src`
7. Start uvicorn - `python -m uvicorn main:app --reload`
8. Go to [http://127.0.0.1:8000](http://127.0.0.1:8000) 
