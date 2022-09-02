from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    subject: str
    body: str
    sender: str
    receiver: str
