# %%
import math
from build123d import *
from ocp_vscode import show, show_object
# %%
r = 8.0
l = 50.0
c = 3
N = 2 * c
beta = (c * 2.0 * math.pi) / N

# %%
with BuildPart() as part26:
    with BuildLine():
        t = Helix(l / c, l, r)

    with BuildSketch(Plane(origin=t @ 0, z_dir = t % 0)):
        Circle(1.5)
    sweep()
show(part26)
# %%
