from event.event import EventType, subscribe
from domain.product import Product
from domain.email import Email
from service.email import send_email


def handle_create_product_event(product: Product = None) -> None:
    email = Email(
        subject=f'成功创建产品{product.name}',
        body=f'成功创建产品{product.name}',
        sender='admin@local',
        receiver='consumer@local'
    )
    send_email(email)


def handle_update_statistics_event() -> None:
    email = Email(
        subject='成功更新产品统计信息',
        body='成功更新产品统计信息',
        sender='admin@local',
        receiver='consumer@local'
    )
    send_email(email)


def initialize_email_handlers() -> None:
    subscribe(EventType.CREATE_PRODUCT, handle_create_product_event)
    subscribe(EventType.UPDATE_STATISTICS, handle_update_statistics_event)
