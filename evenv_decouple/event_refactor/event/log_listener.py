from event.event import EventType, subscribe
from domain.product import Product
from service import log


def handle_create_product_event(product: Product = None) -> None:
    log.info(f'记录日志: 创建新产品成功:{product}')


def handle_update_statistics_event() -> None:
    log.info('记录日志: 更新统计信息成功')


def initialize_log_handlers() -> None:
    subscribe(EventType.CREATE_PRODUCT, handle_create_product_event)
    subscribe(EventType.UPDATE_STATISTICS, handle_update_statistics_event)
