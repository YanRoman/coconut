from fastapi import FastAPI

from src import data_loader
from src.algs.global_top import global_top_predict
from src.algs.apriori_alg import apriori_

app = FastAPI()
df = data_loader.create_df("chunk_1.csv")


@app.get("/api/v1/predict")
def read_root(user_id: str = None):
    return {"product_ids": global_top_predict(df, user_id)}


@app.get("/api/v1/apriori")
def call_apr():
    apriori_()
    return {"alls": "good"}
