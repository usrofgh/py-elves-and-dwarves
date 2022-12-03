import abc
from abc import ABC


class Player(ABC):
    team = []

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        self.team.append(self)

    @abc.abstractmethod
    def get_rating(self) -> int:
        pass

    @abc.abstractmethod
    def player_info(self) -> str:
        pass
