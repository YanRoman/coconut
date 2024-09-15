import numpy as np
import pandas as pd
from efficient_apriori import apriori
from src.data_loader import *


ITEMSETS = {}
RULES = []
MIN_SUPPORT = 0.001
MIN_CONFIDENCE = 0.5


def apriori_(dataset):
    global ITEMSETS, RULES
    transactions = [tuple(row[1]) for row in extract_transactions(dataset).values.tolist()]
    ITEMSETS, RULES = apriori(transactions, min_support=MIN_SUPPORT, min_confidence=MIN_CONFIDENCE)


def apriori_pred(user_id):
    for rule in RULES:
        print(type(rule))
        print(rule)
