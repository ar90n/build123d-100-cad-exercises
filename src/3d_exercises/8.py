# %%
import math
import numpy as np
from build123d import *
from ocp_vscode import show, show_object

# %%
depth = 60.0
base_width = 100.0
base_height = 100.0
base_depth = 12.0
pillar_width = 40.0
pillar_height = 40.0
pillar_depth = depth - base_depth
support_width = 10.0

# %%
with BuildPart() as part8:
    Box(base_width / 2.0, base_height / 2.0, base_depth, align=[Align.MAX, Align.MAX, Align.MIN])

    base_topf = part8.faces().sort_by(Axis.Z).last
    with BuildSketch(base_topf):
        with BuildLine():
            Polyline(*[
                (-base_width / 4.0, base_height / 4.0),
                (-base_width / 4.0, base_height / 4.0 - support_width / 2.0),
                (base_width / 4.0 - pillar_width / 2.0 , base_height / 4.0 - support_width / 2.0),
                (base_width / 4.0 - pillar_width / 2.0 , base_height / 4.0 - pillar_height / 2.0),
                (base_width / 4.0 - support_width / 2.0 , base_height / 4.0 - pillar_height / 2.0),
                (base_width / 4.0 - support_width / 2.0 , -base_height / 4.0),
                (base_width / 4.0, -base_height / 4.0),
                (base_width / 4.0, base_height / 4.0),
                (-base_width / 4.0, base_height / 4.0),
            ])
        make_face()
    extrude(amount = pillar_depth)

    e0_0 = np.array((-base_width / 2.0, 0.0, base_depth)) - np.array((-pillar_width / 2.0, 0.0, depth))
    e0_1 = np.array((-base_width / 2.0, 0.0, base_depth)) - np.array((-pillar_width / 2.0, -support_width / 2.0, depth))
    n0 = np.cross(e0_0, e0_1)
    cut_plane0 = Plane(origin=(-pillar_width / 2.0, 0.0, depth), z_dir=n0)
    split(part8.part, cut_plane0)

    e1_0 = np.array((0.0, -base_height / 2.0, base_depth)) - np.array((0.0 , -pillar_width / 2.0, depth))
    e1_1 = np.array((0.0, -base_height / 2.0, base_depth)) - np.array((-support_width / 2.0, -pillar_width / 2.0, depth))
    n1 = np.cross(e1_0, e1_1)
    cut_plane1 = Plane(origin=(0.0, -pillar_width / 2.0, depth), z_dir=-n1)
    split(part8.part, cut_plane1)

    mirror(about=Plane.XZ)
    mirror(about=Plane.YZ)

show(part8)