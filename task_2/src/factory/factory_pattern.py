from src.factory.exporters.json_exporter import JsonExporter
from src.factory.exporters.xml_exporter import XmlExporter
from src.cli.format import ExportFormat


class ExporterFactory:
    """Creates the approprioate exporter based on the format
    Note: default value is in json format which is indicated in cli command"""

    exporter = {ExportFormat.JSON: JsonExporter, ExportFormat.XML: XmlExporter}

    @staticmethod
    def create(format_enum: ExportFormat):
        try:
            return ExporterFactory.exporter[format_enum]()

        except KeyError:
            raise NotImplementedError
