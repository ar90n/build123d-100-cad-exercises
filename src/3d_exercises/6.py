# %%
import math
from build123d import *
from ocp_vscode import show, show_object

# %%
with BuildPart() as part6:
    slope_height = 20.0 / (math.sin(45.0 * math.pi / 180.0) + math.cos(30.0 * math.pi / 180.0)) 
    height = 13.0 + slope_height
    with BuildSketch():
        with BuildLine():
            Polyline(*[
                (0.0, 0.0),
                (56.0, 0.0),
                (56.0, 13.0),
                (56.0 - slope_height * math.sin(45.0 * math.pi / 180.0), height),
                (56.0 - slope_height * math.sin(45.0 * math.pi / 180.0) - 36.0, height),
                (0.0, 13.0),
                (0.0, 0.0)
            ])
        make_face()
    extrude(amount = 9.0)
    with Locations((0, height, 0)):
        Box(56.0, 7.0, 3.0, align=[Align.MIN, Align.MAX, Align.MIN], mode=Mode.SUBTRACT)
    mirror(about=Plane.XY)
show(part6)