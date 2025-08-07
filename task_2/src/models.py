from dataclasses import dataclass
from typing import List


@dataclass
class Student:
    id: int
    name: str
    room: int


@dataclass
class Room:
    id: int
    name: str
    students: List[Student]
