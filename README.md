# Yahoo Finance Ticker Lookup tool

## Overview

Light-weight, dynamic and interactive web-based tool to lookup tickers and company names registered on Yahoo! Finance.

| <img width="500px" src="img/demo.gif"/> | 
|:--:| 
| **Fig. 1** : Demo of lookup for **MSFT** and **GOOGL** |


## Getting started

```
git clone https://github.com/lcsrodriguez/yf-finance.git
cd yf-finance/

python3 -m venv .venv
source .venv/bin/activate

pip3 install -r requirements.txt
pip3 freeze
```


```
uvicorn api:app --reload
```

## License

[MIT](LICENSE)
