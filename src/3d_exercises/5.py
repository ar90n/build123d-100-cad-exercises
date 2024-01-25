# %%
import math
import numpy as np
from build123d import *
from ocp_vscode import show, show_object

# %%
height = 30 # ??????
with BuildPart() as part5:
    with BuildSketch():
        with BuildLine():
            RadiusArc((-18.0, 15.0), (-18.0, -15.0), 15.0,False)
            Polyline(*[
                (-18.0, -15.0),
                (0.0, -15.0),
                (0.0, 15.0),
                (-18.0, 15.0)
            ])
        make_face()
    extrude(amount = height)
    topf = part5.faces().sort_by(Axis.Z).last
    with Locations(topf.location):
        with Locations((-18.0, 0, 0)):
            Hole(7.5)

    with BuildSketch():
        with BuildLine():
            Polyline(*[
                (0.0, 15.0),
                (33.0, 15.0),
                (42, 6.0),
                (42, -6.0),
                (33, -15.0),
                (0.0, -15.0),
                (0.0, 15.0),
            ])
        make_face()
    f2 = extrude(amount = 9.0)

    topf2 = f2.faces().sort_by(Axis.Z).last
    with Locations(topf2.bounding_box().center()):
        Box(42.0, 7.0, height - 9.0, align=[Align.CENTER, Align.CENTER, Align.MIN])

    d0 = np.array((42, 0, 9)) - np.array((0, -3.5, height))
    d1 = np.array((42, 0, 9)) - np.array((0, 3.5, height))
    n = np.cross(d0, d1)
    p = Plane(origin=(0, 3.5, height), z_dir=n)
    split(part5.part, p)

show(part5)
# %%
