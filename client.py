import dataclasses
import uuid
from dataclasses import dataclass


@dataclass
class Confirmation:
    token: str = ""
    confirmed: bool = False

    def __post_init__(self):
        if self.token == "":
            self.token = str(uuid.uuid4())


@dataclass
class Log:
    log: str = ""


@dataclass
class Client:
    name: str
    logs: list[Log] = dataclasses.field(default_factory=list)
    api_token: str = ""
    confirmation: Confirmation = dataclasses.field(default_factory=Confirmation)

    def __post_init__(self):
        print("CLIENT_POST_INIT")

    def confirm(self, confirmation_token: str):
        if confirmation_token == self.confirmation.token:
            self.confirmation.confirmed = True
