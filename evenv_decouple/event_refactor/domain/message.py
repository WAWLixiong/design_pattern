from dataclasses import dataclass


@dataclass(frozen=True)
class Message:
    phone_number: str
    body: str
    subject: str
    sender: str
