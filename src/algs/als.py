from implicit.als import AlternatingLeastSquares
from loguru import logger
from scipy.sparse import csr_matrix


def als_train(df, factors=40, regular=0.01, iterations=3):
    event_ratings = {'view': 1, 'cart': 5, 'purchase': 10}
    df['event'] = df['event_type'].map(event_ratings)

    df = df.groupby(['user_id', 'product_id'])['event'].sum().reset_index()
    matrix = df.pivot(index='user_id', columns='product_id', values='event').fillna(0)
    sparse_matrix = csr_matrix(matrix.values)

    model = AlternatingLeastSquares(factors=factors, regularization=regular, iterations=iterations)
    model.fit(sparse_matrix)
    return model, matrix


def als_pred(user_id, model, matrix):
    if user_id not in matrix.index:
        logger.info(f"User ID {user_id} not found in matrix")
        return []

    user_index = matrix.index.get_loc(user_id)
    user_row = matrix.loc[user_id].values
    user_interactions = csr_matrix(user_row)

    item_ids, scores = model.recommend(user_index, user_interactions, N=10)

    product_ids = matrix.columns[item_ids].tolist()
    return product_ids[0]