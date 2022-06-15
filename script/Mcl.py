import Particle
import math


class Mcl:  ###Mcl3 (1,2,5行目以降を記載)
    def __init__(self, init_pose, num):
        self.particles = [Particle.Particle(init_pose) for i in range(num)]

    def draw(self, ax, elems):  # 追加
        xs = [p.pose[0] for p in self.particles]
        ys = [p.pose[1] for p in self.particles]
        vxs = [math.cos(p.pose[2]) for p in self.particles]
        vys = [math.sin(p.pose[2]) for p in self.particles]
        elems.append(ax.quiver(xs, ys, vxs, vys, color="blue", alpha=0.5))
