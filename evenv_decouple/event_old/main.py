from api.product import make_product
from api.statistics import do_update_statistics
from dto.product import CreateProductRequest


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
    main()
