from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum([player.get_rating() for player in team])


def elves_concert(team: list[Player]) -> None:
    [player.play_elf_song() for player in team
     if isinstance(player, Elf)]


def feast_of_the_dwarves(team: list[Player]) -> None:
    [player.eat_favourite_dish() for player in team
     if isinstance(player, Dwarf)]
