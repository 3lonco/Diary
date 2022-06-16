import numpy as np
import math
import world
import Camera
import Robot
import map
import Landmark
import EstimationAgent
import Mcl

w = world.World(30, 0.1, debug=False)
# add three Landmarks after creating an instance of Map
m = map.Map()
for ln in [(-4, 2), (2, 3), (3, 3)]:
    m.append_landmark(Landmark.Landmark(*ln))
w.append(m)


### ロボットを作る ###
initial_pose = np.array([2, 2, math.pi / 6]).T
estimator = Mcl.Mcl(initial_pose, 100)
circling = EstimationAgent.EstimationAgent(0.2, 10.0 / 180 * math.pi, estimator)
r = Robot.Robot(initial_pose, sensor=Camera.Camera(m), agent=circling)
w.append(r)
w.draw()
