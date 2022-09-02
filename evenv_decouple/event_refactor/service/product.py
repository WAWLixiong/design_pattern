from dataclasses import asdict

from domain.product import Product
from dto.product import CreateProductRequest


def create_product(create_product_request: CreateProductRequest) -> Product:
    product = Product(**asdict(create_product_request))
    print(f'产品服务创建新产品:{product}')
    return product
