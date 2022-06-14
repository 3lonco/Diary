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
        distance_bias_rate_stddev=0.1,
        direction_bias_stddev=math.pi / 90,
        phantom_prob=0.0,
        phantom_range_x=(-5.0, 5.0),
        phantom_range_y=(-5.0, 5.0),
        oversight_prob=0.1
    ):
        super().__init__(env_map, distance_range, direction_range)

        self.distance_noise_rate = distance_noise_rate
        self.direction_noise = direction_noise
        self.distance_bias_rate_std = norm.rvs(scale=distance_bias_rate_stddev)
        self.direction_bias = norm.rvs(scale=direction_bias_stddev)

        # Add phantom
        rx, ry = phantom_range_x, phantom_range_y
        self.phantom_dist = uniform(
            loc=(rx[0], ry[0]), scale=(rx[1] - rx[0], rx[1] - rx[0])
        )
        self.phantom_prob = phantom_prob

        #Add Oversight
        self.oversight_prob=oversight_prob

    def oversight(self,relpos):#add
        if uniform.rvs() < self.oversight_prob:
            return None
        else:
            return relpos

    def phantom(self, cam_pose, relpos):
        if uniform.rvs() < self.phantom_prob:
            pos = np.array(self.phantom_dist.rvs()).T
            return self.observation_function(cam_pose, pos)
        else:
            return relpos

    def bias(self, relpos):
        return (
            relpos
            + np.array([relpos[0] * self.distance_bias_rate_std, self.direction_bias]).T
        )

    def noise(self, relpos):
        ell = norm.rvs(loc=relpos[0], scale=relpos[0] * self.distance_noise_rate)
        phi = norm.rvs(loc=relpos[1], scale=self.direction_noise)
        return np.array([ell, phi]).T

    def data(self, cam_pose):
        observed = []
        for lm in self.map.landmarks:
            z = self.observation_function(cam_pose, lm.pos)
            z = self.phantom(cam_pose, z)
            z = self.oversight(z)
            if self.visible(z):
                z = self.bias(z)
                z = self.noise(z)
                observed.append((z, lm.id))

        self.lastdata = observed
        return observed