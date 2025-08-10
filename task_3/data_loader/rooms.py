from .base import BaseDataLoader
import json


class RoomsDataLoader(BaseDataLoader):

    def load(self):
        with open("data/rooms.json", "r") as f:
            rooms = json.load(f)

        return rooms
