# %%
import math
from build123d import *
from ocp_vscode import show, show_object
# %%
with BuildPart() as part1:
    with BuildSketch():
        Circle(45.0)
    extrude(amount=14.2)

    base_topf = part1.faces().sort_by(Axis.Z).last
    with BuildSketch(base_topf):
        Circle(20.0)
    extrude(amount=44.2)

    topf = part1.faces().sort_by(Axis.Z).last
    with BuildSketch(topf):
        Circle(25.0)
    extrude(amount=30.0)
    fillet(part1.faces().sort_by(Axis.Z)[2:-2].edges().filter_by(GeomType.CIRCLE), radius= 1.5)

    topf = part1.faces().sort_by(Axis.Z).last
    with Locations(topf):
        Hole(19.0, 24.0)
        Hole(15.0)
    fillet(part1.faces().sort_by(Axis.Z).last.edges().filter_by(GeomType.CIRCLE), radius= 1.5)
    chamfer(part1.faces().sort_by(Axis.Z).first.edges().filter_by(GeomType.CIRCLE).sort_by(SortBy.RADIUS).first, length= 3.5, length2=3.0)

    with Locations(base_topf):
        with PolarLocations(32.5, 4):
            Hole(6.25)

show(part1)