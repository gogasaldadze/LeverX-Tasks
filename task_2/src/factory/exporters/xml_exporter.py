from .base import Exporter
import xml.etree.ElementTree as ET


class XmlExporter(Exporter):
    def export(self, data, path):

        root = ET.Element("rooms")
        for room in data:
            room_elem = ET.SubElement(root, "room", id=str(room.id))
            ET.SubElement(room_elem, "name").text = room.name
            students_elem = ET.SubElement(room_elem, "students")
            for student in room.students:
                student_elem = ET.SubElement(
                    students_elem, "student", id=str(student.id)
                )
                ET.SubElement(student_elem, "name").text = student.name
        ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)
