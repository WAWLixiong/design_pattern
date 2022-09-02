from api.product import make_product
from api.statistics import do_update_statistics
from dto.product import CreateProductRequest


def bootstrap() -> None:
    from event.log_listener import initialize_log_handlers
    from event.email_listener import initialize_email_handlers
    from event.message_listener import initialize_message_handlers

    initialize_log_handlers()
    initialize_message_handlers()
    initialize_email_handlers()


def main() -> None:
    request = CreateProductRequest(
        name='Apple',
        price=33.3,
        qty=100
    )

    make_product(request)
    print('-' * 100)
    do_update_statistics()


if __name__ == '__main__':
    bootstrap()
    main()
