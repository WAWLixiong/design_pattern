from dto.product import CreateProductRequest
from service.product import create_product
from service.email import send_email
from service.message import send_message
from service import log
from domain.email import Email
from domain.message import Message
from flask import Flask

app = Flask(__name__)


@app.get('/product')
def make_product(create_product_request: CreateProductRequest) -> None:
    product = create_product(create_product_request)
    log.info(f'成功创建产品:{product}')
    email = Email(
        subject=f'成功创建产品{product.name}',
        body=f'成功创建产品{product.name}',
        sender='admin@local',
        receiver='consumer@local'
    )
    send_email(email)

    message = Message(
        phone_number='17700000000',
        body=f'成功创建产品{product.name}',
        subject=f'成功创建产品{product.name}',
        sender='17700000000',
    )
    send_message(message)
