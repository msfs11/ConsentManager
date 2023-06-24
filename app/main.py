# app/main.py

from fastapi import FastAPI

app = FastAPI(title="ConsentManager")


@app.get("/")
def read_root():
    return {"hello": "world"}
