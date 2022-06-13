import IdealCamera
import math


class Camera(IdealCamera):
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
        self.direction_range = direction_noise
