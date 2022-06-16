import numpy as np
import math


class IdealCamera:
    def __init__(
        self,
        env_map,
        distance_range=(0.5, 6.0),
        direction_range=(-math.pi / 3, math.pi / 3),  # -120 < Θ <120
    ):
        self.map = env_map
        self.lastdata = []

        self.distance_range = distance_range
        self.direction_range = direction_range

    def visible(self, polarpos):  # ランドマークが計測できる条件
        if polarpos is None:
            return False

        return (
            self.distance_range[0] <= polarpos[0] <= self.distance_range[1]
            and self.direction_range[0] <= polarpos[1] <= self.direction_range[1]
        )

    def data(self, cam_pose):
        observed = []
        for Im in self.map.landmarks:
            z = self.observation_function(cam_pose, Im.pos)
            if self.visible(z):
                observed.append((z, Im.id))

        self.lastdata = observed
        return observed

    def draw(self, ax, elems, cam_pose):
        for Im in self.lastdata:
            x, y, theta = cam_pose
            distance, direction = Im[0][0], Im[0][1]
            lx = x + distance * math.cos(direction + theta)
            ly = y + distance * math.sin(direction * theta)
            elems += ax.plot([x, lx], [y, ly], color="pink")

    @classmethod
    def observation_function(cls, cam_pose, obj_pos):
        diff = obj_pos - cam_pose[0:2]
        phi = math.atan2(diff[1], diff[0]) - cam_pose[2]
        while phi >= np.pi:
            phi -= 2 * np.pi
        while phi < -np.pi:
            phi += 2 * np.pi
        return np.array([np.hypot(*diff), phi]).T
