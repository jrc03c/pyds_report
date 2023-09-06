from .report_item import ReportItem


class Header(ReportItem):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.tagName = "h"

    @property
    def rank(self):
        if self.parent is None:
            return 1

        return self.parent.depth + 1

    @property
    def leftTag(self):
        out = "<" + self.tagName + str(self.rank)

        if self.id is not None:
            out += " #" + self.id

        if len(self.classes) > 0:
            out += (" ").join(self.classes)

        if len(self.attributes.keys()) > 0:
            for key in self.attributes.keys():
                out += (" {}='{}'").format(key, self.attributes[key])

        return out + ">"

    @property
    def rightTag(self):
        return "</" + self.tagName + str(self.rank) + ">"

    def render(self):
        return self.leftTag + self.text + self.rightTag
