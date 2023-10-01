import pprint

from src import *

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get("/", response_class=HTMLResponse)
def homeRoute(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/search')
def search(ticker_lookup: str = Form(None)):
    if ticker_lookup is None:
        return f""

    r = requests.get(url=LOOKUP_API_ROUTE,
                     params={
                         "q": str(ticker_lookup),
                         "lang": "en-US",
                         "region": "US",
                         "quotesCount": 10,
                     },
                     headers={
                         "Accept": "*/*",
                         "Connection": "keep-alive",
                         "Host": "query2.finance.yahoo.com",
                         "Origin": "https://finance.yahoo.com",
                         "Referer": "https://finance.yahoo.com/lookup",
                         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0"
                     })
    if r.status_code // 100 != 2:
        return f""
    data: dict = r.json()
    return f"<b>{ticker_lookup}</b><p>{data['quotes']}</p>"
