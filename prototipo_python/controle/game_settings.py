from dataclasses import dataclass


@dataclass
class PlayerCharacter:
    fight_style: str
    genre: str
    category: str
    attack_weapon: str


@dataclass
class GameSettings:
    style: str
    plot: str
    player_character: PlayerCharacter
    assistant_role: str = "Master of an RPG game"
