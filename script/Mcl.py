import numpy as np
import Particle
import math
from scipy.stats import multivariate_normal


class Mcl:  ###Mcl3 (1,2,5行目以降を記載)
    def __init__(self, init_pose, num, motion_noise_stds):
        self.particles = [Particle.Particle(init_pose) for i in range(num)]

        v = motion_noise_stds
        # v = variation, n = nu, o = omega
        c = np.diag([v["nn"] ** 2, v["no"] ** 2, v["on"] ** 2, v["oo"] ** 2])
        self.motion_noise_rate_pdf = multivariate_normal(cov=c)

    def motion_update(self, nu, omega, time):
        print(self.motion_noise_rate_pdf.cov)

    def draw(self, ax, elems):  # 追加
        xs = [p.pose[0] for p in self.particles]
        ys = [p.pose[1] for p in self.particles]
        vxs = [math.cos(p.pose[2]) for p in self.particles]
        vys = [math.sin(p.pose[2]) for p in self.particles]
        elems.append(ax.quiver(xs, ys, vxs, vys, color="blue", alpha=0.5))



