import json
from src.models import Student
from src.merger import Merger
from src.factory.factory_pattern import ExporterFactory
from src.cli.parser import parse_args
from src.cli.format import ExportFormat


def run():
    args = parse_args()

    with open(args.students) as f:
        students = [Student(**s) for s in json.load(f)]

    with open(args.rooms) as f:
        rooms = json.load(f)

    merged_data = Merger.merge(students, rooms)

    format_enum = ExportFormat(args.format)
    exporter = ExporterFactory.create(format_enum)
    exporter.export(merged_data, args.output)
