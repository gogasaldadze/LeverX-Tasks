import argparse
from src.cli.format import ExportFormat


def parse_args():
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
        default=ExportFormat.JSON.value,
        choices=[e.value for e in ExportFormat],
        help="output file format",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="data/output/result.json",
        help="path to the output file",
    )
    return parser.parse_args()
