import numpy as np
import pandas as pd
from efficient_apriori import apriori
from src.data_loader import *
# import plotly.express as px


def apriori_():
    file_path = "chunk_1.csv"
    df = pd.read_csv(file_path)
    tmp = extract_transactions(df)
    transactions = [tuple(row[1]) for row in tmp.values.tolist()]
    tr2 = [tuple(map(str, tpl)) for tpl in transactions]
    print(tr2[:2])
    itemsets, rules = apriori(tr2, min_support=0.2)
    print(itemsets, rules)