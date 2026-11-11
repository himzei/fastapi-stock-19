from datetime import datetime, timedelta

import FinanceDataReader as fdr
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://fastapi-stock-react-19-orcin.vercel.app",
        "http://localhost:5173",  # 로컬 개발용 (Vite)
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_home():
    return {"hello": "world3"}


@app.get("/samsung")
def read_samsung():
    # 삼성전자 종목코드: 005930, 최근 30일 데이터
    start = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    df = fdr.DataReader("005930", start)

    df = df.reset_index()
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

    return {
        "code": "005930",
        "name": "삼성전자",
        "data": df.to_dict(orient="records"),
    }
