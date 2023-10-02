from src import *

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get("/", response_class=HTMLResponse)
def homeRoute(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/search')
def searchRoute(ticker_lookup: str = Form(None)):
    if ticker_lookup is None:
        return f""

    r = requests.get(url=LOOKUP_API_ROUTE,
                     params={
                         "q": str(ticker_lookup),
                         "lang": "en-US",
                         "region": "US",
                         "quotesCount": 20,
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
    l = []
    s = "<table class='table'>"
    i = 0
    headers_ = ["exchange", "shortname", "quoteType", "symbol", "index"]
    for q in data["quotes"]:
        q2 = {}
        if q["isYahooFinance"] is True:
            for h in headers_:
                if h in q:
                    q2[h] = q[h]
            print(q2)
            c = colors.get(q2["quoteType"], "primary") # if q2["quoteType"] in list(colors.keys()) else "primary"
            print(c)
            q2["link"] = f"<a target='_BLANK' href='https://finance.yahoo.com/quote/{q2['symbol']}' role='button' class='btn btn-{c} btn-sm' style='width:100px'>{q2['symbol']}<a>"
            i += 1
            if i == 1:
                s += f"<thead><tr>"
                for e in list(q2.keys()):
                    s += f"<th>{e}</th>"
                s += "</tr></thead>"
            l.append(q2)
            s += f"<tr>"
            for e in list(q2.values()):
                s += f"<td>{e}</td>"
            s += "</tr>"
    return f"Results for: <b><i>{ticker_lookup}</i></b><br><br>{s}"
