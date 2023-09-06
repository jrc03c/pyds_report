class ReportItem:
    def __init__(self):
        self.parent = None
        self.id = None
        self.classes = []
        self.attributes = {}
        self.tagName = "unknown"

    @property
    def depth(self):
        return 0 if self.parent is None else self.parent.depth + 1

    @property
    def leftTag(self):
        out = "<" + self.tagName

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
        return "</" + self.tagName + ">"

    def render(self):
        return self.leftTag + self.rightTag
