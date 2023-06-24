from app import ProductApp

app = ProductApp('abdul', '1234')

query_data_1 = {
    'query': 'product',
    'payload': {
        'id': 23
    }
}

query_data_2 = {
    'query': 'length',
}

query_data_3 = {
    'query': 'get info',
    'payload': {
        'id': 23,
        'property': 'rating'
    }
}

response = app.get_data(query_data=query_data_3)
print(response)