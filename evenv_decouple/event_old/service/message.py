from domain.message import Message


def send_message(message: Message) -> None:
    print(f'发送消息:{message}')
