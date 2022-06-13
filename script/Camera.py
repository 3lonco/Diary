from IdealCamera import *
from scipy.stats import expon, norm, uniform


class Camera(IdealCamera):  ###camera_second### (initは省略)
    def __init__(
        self,
        env_map,
        distance_range=(0.5, 6.0),
        direction_range=(-math.pi / 3, math.pi / 3),
        distance_noise_rate=0.1,
        direction_noise=math.pi / 90,
    ):
        super().__init__(env_map, distance_range, direction_range)

        self.distance_noise_rate = distance_noise_rate
        self.direction_noise = direction_noise

    def noise(self, relpos):  # 追加
        ell = norm.rvs(loc=relpos[0], scale=relpos[0] * self.distance_noise_rate)
        phi = norm.rvs(loc=relpos[1], scale=self.direction_noise)
        return np.array([ell, phi]).T

    def data(self, cam_pose):
        observed = []
        for lm in self.map.landmarks:
            z = self.observation_function(cam_pose, lm.pos)
            if self.visible(z):
                z = self.noise(z)  # 追加
                observed.append((z, lm.id))

        self.lastdata = observed
        return observed
