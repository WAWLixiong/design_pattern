from service import log
from service.statistics import update_statistics


def do_update_statistics() -> None:
    update_statistics()
    log.info('成功更新产品统计信息！')
