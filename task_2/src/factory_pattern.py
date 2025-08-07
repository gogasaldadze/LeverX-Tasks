from src.exporters.json_exporter import JsonExporter
from src.exporters.xml_exporter import XmlExporter


class ExporterFactory:
    """Creates the approprioate exporter based on the format
    Note: default value is in json format which is indicated in cli command"""

    @staticmethod
    def create(format):
        if format == "json":
            return JsonExporter()
        elif format == "xml":
            return XmlExporter()

        raise NotImplementedError
