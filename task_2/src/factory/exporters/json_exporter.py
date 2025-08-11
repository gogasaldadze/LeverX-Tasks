from .base import Exporter
import json
from dataclasses import asdict


class JsonExporter(Exporter):
    def export(self, data, path):
        rooms_list = []
        for room in data:
            rooms_list.append(asdict(room))

        with open(path, "w") as f:
            json.dump(rooms_list, f, indent=2)
