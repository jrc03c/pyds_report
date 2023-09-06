from .report_item import ReportItem


class Section(ReportItem):
    def __init__(self, children=[]):
        super().__init__()
        self.children = []
        self.addChildren(children)
        self.tagName = "section"

    def addChild(self, child):
        child.parent = self
        self.children.append(child)
        return self

    def removeChild(self, child):
        child.parent = None
        self.children.remove(child)
        return self

    def addChildren(self, children):
        for child in children:
            self.addChild(child)

        return self

    def removeChildren(self, children):
        for child in children:
            self.removeChild(child)

        return self

    def render(self):
        return (
            self.leftTag
            + ("").join([child.render() for child in self.children])
            + self.rightTag
        )
