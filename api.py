from src import *

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get("/", response_class=HTMLResponse)
def homeRoute(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/search')
def search(ticker_lookup: str = Form(...)):
    print(ticker_lookup)
    return f"<b>{ticker_lookup}</b>"
