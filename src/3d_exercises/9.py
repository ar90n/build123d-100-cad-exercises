# %%
import math
from build123d import *
from ocp_vscode import show, show_object
# %%
l = 180.0
d = 120.0
# %%
with BuildPart() as holder_shape:
    with BuildSketch(Plane.YZ):
        with BuildLine():
            Polyline(
                (0.0, 0.0),
                (40.0, 0.0),
                (40.0, 55.0),
            )
            RadiusArc(
                (40.0, 55.0),
                (-40.0, 55.0),
                40.0,
                short_sagitta=False
            )
            Polyline(
                (-40.0, 55.0),
                (-40.0, 0.0),
                (0.0, 0.0),
            )
        make_face()
    extrude(amount=125.0)

with BuildPart() as holder:
    add(holder_shape)
    with BuildSketch(Plane.YZ):
        with Locations((0.0, 75.0)):
            Circle(15.0)
    extrude(amount=125.0, mode=Mode.SUBTRACT)

    with BuildSketch(Plane.YZ):
        with Locations((0.0, 25.0)):
            Rectangle(80.0, 15.0, align=[Align.CENTER, Align.MIN])
    extrude(amount=15.0, mode=Mode.SUBTRACT)
show(holder)
# %%
with BuildPart() as part9:
    with BuildSketch(Plane.XZ):
        Rectangle(l, 90.0, align=[Align.MIN, Align.MAX])
    extrude(amount=d / 2.0)

    short_f = part9.faces().sort_by(Axis.X).first
    with BuildSketch(short_f):
        with Locations((-(45 - 20.0), -(d / 4 - 20.0))):
            Circle(10.0)
    extrude(amount=-l, mode=Mode.SUBTRACT)


    long_f = part9.faces().sort_by(Axis.Z).last
    with BuildSketch(long_f):
        with Locations(((l / 2 - 20.0),-(d / 4 - 20.0))):
            Circle(10.0)
    extrude(amount=-90.0, mode=Mode.SUBTRACT)
    mirror(about=Plane.XZ)

    add(holder_shape, rotation=(0.0, 45.0, 0.0), mode=Mode.SUBTRACT)
    add(holder, rotation=(0.0, 45.0, 0.0))

    with BuildSketch(Plane.XZ):
        with Locations((25.0, -25.0)):
            Rectangle(l - 25.0, 90.0 - 25.0, align=[Align.MIN, Align.MAX])
    extrude(amount=d / 2, mode=Mode.SUBTRACT, both=True)

    fillet(part9.faces().sort_by(Axis.X).last.edges().filter_by(Axis.Z), radius=25.0)
    fillet(part9.faces().sort_by(Axis.Z).first.edges().filter_by(Axis.X), radius=25.0)
show(part9)