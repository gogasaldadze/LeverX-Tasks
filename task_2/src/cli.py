import argparse
import json
from .models import Student
from .merger import Merger
from .factory_pattern import ExporterFactory


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--students",
        "-s",
        required=True,
        default="data/input/students.json",
        help="path to students json file",
    )
    parser.add_argument(
        "--rooms",
        "-r",
        required=True,
        default="data/input/rooms.json",
        help="path to rooms json file",
    )
    parser.add_argument(
        "--format",
        "-f",
        default="json",
        choices=["json", "xml"],
        help="output file format",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="data/output/result.json",
        help="path to the output file ",
    )

    args = parser.parse_args()

    with open(args.students) as f:
        students = [Student(**s) for s in json.load(f)]

    with open(args.rooms) as f:
        rooms = json.load(f)

    merged_data = Merger.merge(students, rooms)

    exporter = ExporterFactory.create(args.format)
    exporter.export(merged_data, args.output)
