import numpy as np
from loguru import logger
from tqdm import tqdm
import time

from algs.global_top import global_top_train, global_top_predict
import data_loader

df = data_loader.create_df("chunk_0.csv")
test_df, train_df = data_loader.split_train_test(df)


def get_precision(predict_func):
    start_time = time.time()
    test_transactions = data_loader.extract_transactions(test_df)

    if test_transactions.empty:
        logger.info(f"[Method: {predict_func.__name__}] [Precision: 0.0000] [Time: {time.time() - start_time:.4f} sec]")
        return 0

    precisions = []
    for _, row in tqdm(test_transactions.iterrows(), desc=f'Считаю Precision для {predict_func.__name__}...', total=len(test_transactions)):
        predict = predict_func(df, row['user_session'])
        precision = np.isin(predict, row['product_ids']).sum() / len(predict)
        precisions.append(precision)

    average_precision = np.mean(precisions)
    logger.info(f"[Method: {predict_func.__name__}] [Precision: {average_precision:.4f}] [Time: {time.time() - start_time:.4f} sec.]")

    return average_precision


def main():
    # global top
    global_top_train(train_df)
    get_precision(global_top_predict)

    # ... другие алгоритмы


if __name__ == "__main__":
    main()
