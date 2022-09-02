from event.event import emit, EventType
from service.statistics import update_statistics


def do_update_statistics() -> None:
    update_statistics()
    emit(EventType.UPDATE_STATISTICS)
