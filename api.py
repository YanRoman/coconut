from fastapi import FastAPI

import data_loader
from algs.global_top import global_top_predict

app = FastAPI()
df = data_loader.create_df("chunk_0.csv")


@app.get("/api/v1/predict")
def read_root(user_id: str = None):
    return {"product_ids": global_top_predict(df, user_id)}
