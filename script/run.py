import world
import IdealRobot
import map
import Landmark
import numpy as np
import math
import Agent
import IdealCamera

w = world.World(10, 1, debug=False)
straight = Agent.Agent(0.2, 0.0)
circling = Agent.Agent(0.2, 10.0 / 180 * math.pi)
m = map.Map()
m.append_landmark(Landmark.Landmark(2, -2))
m.append_landmark(Landmark.Landmark(-1, -3))
m.append_landmark(Landmark.Landmark(3, 3))
w.append(m)
cam = IdealCamera.IdealCamera(m)
robot1 = IdealRobot.IdealRobot(
    np.array([2, 3, math.pi / 6]).T, agent=straight, sensor=IdealCamera.IdealCamera(m)
)
robot2 = IdealRobot.IdealRobot(
    np.array([-2, -1, math.pi / 5 * 6]).T,
    agent=circling,
    sensor=IdealCamera.IdealCamera(m),
    color="red",
)
robot3 = IdealRobot.IdealRobot(np.array([0, 0, 0]).T, color="blue")
w.append(robot1)
w.append(robot2)
w.append(robot3)
w.draw()
