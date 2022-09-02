from flask import Flask

from dto.product import CreateProductRequest
from event.event import emit, EventType
from service.product import create_product

app = Flask(__name__)


@app.get('/product')
def make_product(create_product_request: CreateProductRequest) -> None:
    product = create_product(create_product_request)
    emit(EventType.CREATE_PRODUCT, product)
