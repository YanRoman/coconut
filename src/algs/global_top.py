from collections import Counter


def global_top_train(data):
    pass


def global_top_predict(data, user_context):
    products = data['product_id']

    counter = Counter(products)
    top_products = counter.most_common(3)
    return [product for product, count in top_products]
