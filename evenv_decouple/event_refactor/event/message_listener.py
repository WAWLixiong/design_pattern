from event.event import EventType, subscribe
from domain.product import Product
from domain.message import Message
from service.message import send_message


def handle_create_product_event(product: Product = None) -> None:
    message = Message(
        phone_number='17700000000',
        body=f'成功创建产品{product.name}',
        subject=f'成功创建产品{product.name}',
        sender='17700000000',
    )
    send_message(message)


def handle_update_statistics_event() -> None:
    message = Message(
        phone_number='17700000000',
        body='成功更新产品统计信息',
        subject='成功更新产品统计信息',
        sender='17700000000',
    )
    send_message(message)


def initialize_message_handlers() -> None:
    subscribe(EventType.CREATE_PRODUCT, handle_create_product_event)
    subscribe(EventType.UPDATE_STATISTICS, handle_update_statistics_event)
