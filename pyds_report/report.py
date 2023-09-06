import os
import subprocess

from .header import Header
from .image import Image
from .paragraph import Paragraph
from .report_item import ReportItem
from .section import Section
from .table import Table

with open(os.path.join(os.path.dirname(__file__), "index.html")) as file:
    template = file.read()


class Report:
    Header = Header
    Image = Image
    Paragraph = Paragraph
    ReportItem = ReportItem
    Section = Section
    Table = Table

    def __init__(self, items=[]):
        self.items = items
        self.savePaths = []

    def addItem(self, item):
        self.items.append(item)
        return self

    def removeItem(self, item):
        self.items.remove(item)
        return self

    def addItems(self, items):
        for item in items:
            self.addItem(item)

        return self

    def removeItems(self, items):
        for item in items:
            self.removeItem(item)

        return self

    def render(self):
        return template.replace(
            "{{ content }}", ("").join([item.render() for item in self.items])
        )

    def save(self, path):
        with open(path, "w") as file:
            file.write(self.render())

        self.savePaths.append(path)
        return self

    def show(self, path=None):
        if path is None:
            path = self.savePaths[-1]

        try:
            subprocess.run(["open", path])

        except:
            try:
                subprocess.run(["xdg-open", path])

            except:
                print(
                    (
                        "We couldn't find a way to open the report file! You'll have to open it manually. It's here: file://{}"
                    ).format(os.path.abspath(path))
                )

        return self
