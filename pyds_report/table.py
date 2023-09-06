from copy import deepcopy

from .report_item import ReportItem

# `color_scale`, if used, must come in one of these forms:
# [{"value": min, "color": color}, {"value": max, "color": color}]
# [{"value": min, "color": color}, {"value": value1, "color": color}, ..., {"value": max, "color": color}]
# where `color` is an HSL value in the form {"h": 0, "s": 0, "l": 0}


def lerp(a, b, f):
    return (b - a) * f + a


class Table(ReportItem):
    CorrelationMatrixColorScale = [
        {"value": -1, "color": {"h": 0, "s": 100, "l": 75}},
        {"value": 0, "color": {"h": 0, "s": 100, "l": 100}},
        {"value": 0, "color": {"h": 90, "s": 100, "l": 100}},
        {"value": 1, "color": {"h": 90, "s": 85, "l": 60}},
    ]

    MinMaxColorScale = [
        {"value": 0, "color": {"h": 90, "s": 100, "l": 100}},
        {"value": 1, "color": {"h": 90, "s": 100, "l": 40}},
    ]

    def __init__(self, df, colorScale=None):
        super().__init__()
        self.df = df
        self.tagName = "table"

        if colorScale == Table.MinMaxColorScale:
            self.colorScale = deepcopy(Table.MinMaxColorScale)
            self.colorScale[0]["value"] = df.min().min()
            self.colorScale[1]["value"] = df.max().max()

        else:
            self.colorScale = colorScale

    def render(self):
        out = "<div class='table-container'>"
        out += self.leftTag
        out += "<thead>"
        out += "<tr>"
        out += "<th></th>"

        for col in self.df.columns:
            out += "<th>" + str(col) + "</th>"

        out += "</tr>"
        out += "</thead>"
        out += "<tbody>"

        for i in range(0, self.df.shape[0]):
            out += "<tr>"
            out += "<td>" + str(self.df.index[i]) + "</td>"

            for j in range(0, self.df.shape[1]):
                value = self.df.values[i][j]

                if self.colorScale is not None:
                    left = None
                    right = None

                    for k in range(0, len(self.colorScale) - 1):
                        pair1 = self.colorScale[k]
                        pair2 = self.colorScale[k + 1]

                        if value > pair1["value"] and value < pair2["value"]:
                            left = pair1
                            right = pair2
                            break

                    if left is None and right is None:
                        if value < self.colorScale[0]["value"]:
                            left = self.colorScale[0]
                            right = self.colorScale[1]

                        else:
                            left = self.colorScale[-2]
                            right = self.colorScale[-1]

                    frac = (value - left["value"]) / (right["value"] - left["value"])
                    h = lerp(left["color"]["h"], right["color"]["h"], frac)
                    s = lerp(left["color"]["s"], right["color"]["s"], frac)
                    l = lerp(left["color"]["l"], right["color"]["l"], frac)

                    out += (
                        (
                            "<td style = 'background-color: hsl({}deg, {}%, {}%)'>"
                        ).format(h, s, l)
                        + str(value)
                        + "</td>"
                    )

                else:
                    out += "<td>" + str(value) + "</td>"

            out += "</tr>"

        out += "</tbody>"
        out += self.rightTag
        out += "</div>"
        return out

        # header = (
        #     "<tr>"
        #     "<th></th>"
        #     + ("").join(["<th>" + str(col) + "</th>" for col in self.df.columns])
        #     + "</tr>"
        # )

        # rows = ("").join(
        #     [
        #         "<tr>"
        #         + "<td>"
        #         + str(self.df.index[i])
        #         + "</td>"
        #         + ("").join(
        #             [
        #                 "<td>" + str(self.df.values[i][j]) + "</td>"
        #                 for j in range(0, self.df.shape[1])
        #             ]
        #         )
        #         + "</tr>"
        #         for i in range(0, self.df.shape[0])
        #     ]
        # )

        # return (
        #     "<div class='table-container'>"
        #     + self.leftTag
        #     + "<thead>"
        #     + header
        #     + "</thead>"
        #     + "<tbody>"
        #     + rows
        #     + "</tbody>"
        #     + self.rightTag
        #     + "</div>"
        # )
