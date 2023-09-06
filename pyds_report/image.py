import os

import __main__

from .report_item import ReportItem


class Image(ReportItem):
    def __init__(self, src):
        super().__init__()
        self.attributes["src"] = src
        self.tagName = "img"

    def render(self):
        return (
            ("<a href='{}' target='_blank'>").format(self.attributes["src"])
            + self.leftTag
            + "</a>"
        )
