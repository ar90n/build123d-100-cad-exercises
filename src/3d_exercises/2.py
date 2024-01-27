# %%
import math
from build123d import *
from ocp_vscode import show, show_object
# %%
with BuildPart() as part2:
    with BuildSketch():
        RegularPolygon(radius=10.0, side_count=5)
    extrude(amount=0.5)

    topf = part2.faces().sort_by(Axis.Z).last
    with BuildSketch(topf):
        outer = RegularPolygon(radius=10.0, side_count=5)
        RegularPolygon(radius=10.0 - 0.4, side_count=5, mode=Mode.SUBTRACT)
        star = RegularPolygon(radius=3.9, side_count=5, rotation=180.0)
        ses = star.edges()
        oes = outer.edges()[2:] + outer.edges()[:2]
        for se, oe in zip(ses, oes):
            with BuildLine():
                Polyline(se @ 0, oe @ 1, se @ 1, se @ 0)
            make_face()

    extrude(amount=0.5)
show(part2)