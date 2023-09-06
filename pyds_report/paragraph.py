from .report_item import ReportItem


class Paragraph(ReportItem):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.tagName = "p"

    def render(self):
        return self.leftTag + self.text + self.rightTag
