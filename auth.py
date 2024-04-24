import uuid
from client import Client


class AuthorizationStorage:
    def __init__(self):
        self.clients: list[Client] = []

    def authorizeNewClient(self, client: Client) -> Client | None:
        if self.getClientByName(client.name) is not None:
            return None

        self.clients.append(client)
        if client.api_token == "":
            client.api_token = str(uuid.uuid4())
        return client

    def confirmClient(self, client: Client, confirmation_token: str) -> Client | None:
        if self.getClientByName(client.name) is None:
            return None

        client.confirm(confirmation_token)
        return client

    def getClientByName(self, name: str) -> Client | None:
        client_found = [client for client in self.clients if client.name == name]
        if len(client_found) == 0:
            return None
        return client_found[0]

