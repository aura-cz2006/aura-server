from dataclasses import dataclass
from enum import Enum


@dataclass
class Topics(Enum):
    General = 1
    Nature = 2
    Tech = 3
    Food = 4
    Sports = 5

@dataclass
class DiscussionItem:
    id: str
    topic: Topics
    title: str
