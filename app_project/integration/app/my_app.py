from typing import Any, Dict
import json

class ProductApp:

    def __init__(self, owner: str, password: str) -> None:
        self.owner = owner
        self.password = password

        if self.owner and self.password:
            self.products = self.load_data()
        else:
            self.products = 'Not allowed'

    def load_data(self) -> dict:

        file_content = None

        with open('./app/products.json') as json_file:

            file_content = json_file.read()

        all_products = json.loads(file_content)

        return all_products
    
    def get_data(self, query_data: Dict[str, Any], **kwargs: Any):

        target_result: Any

        query = query_data.get('query', None)

        if query == 'product':

            payload = query_data.get('payload', None)

            if payload:

                target_result = self.get_product(product_id=payload['id'])

        elif query == 'length':

            target_result = len(self.products['products'])

        elif query == 'get info':

            payload = query_data.get('payload', None)

            if payload:

                p_id = payload.get('id')
                prop = payload.get('property')

                prod = self.get_product(p_id)

                target_result = prod[prop]
        
        return target_result
    
    def get_product(self, product_id: int):

        if product_id:

            # product_id = int(product_id)

            for product in self.products['products']:

                if product['id'] == product_id:

                    return product


