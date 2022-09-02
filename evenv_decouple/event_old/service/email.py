from domain.email import Email


def send_email(email: Email) -> None:
    print(f'发送电子邮件:{email}')
