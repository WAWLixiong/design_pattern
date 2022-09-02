from enum import Enum, auto
from collections import defaultdict


class EventType(Enum):
    CREATE_PRODUCT = auto()
    UPDATE_STATISTICS = auto()


subscribers = defaultdict(list)


def subscribe(event_type: EventType, func) -> None:
    subscribers[event_type].append(func)


def emit(event_type: EventType, *args, **kwargs) -> None:
    for func in subscribers[event_type]:
        func(*args, **kwargs)
