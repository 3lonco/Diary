import world
import IdealRobot
import map
import Landmark
import numpy as np
import math
import Agent

w = world.World(10, 1, debug=False)
straight = Agent.Agent(0.2, 0.0)
circling = Agent.Agent(0.2, 10.0 / 180 * math.pi)
robot1 = IdealRobot.IdealRobot(np.array([2, 3, math.pi / 6]).T, straight)
robot2 = IdealRobot.IdealRobot(np.array([-2, -1, math.pi / 5 * 6]).T, circling, "red")
robot3 = IdealRobot.IdealRobot(np.array([0, 0, 0]).T, color="blue")
m=map.Map()
m.append_landmark(Landmark.Landmark(2,-2))
m.append_landmark(Landmark.Landmark(-1,-3))
m.append_landmark(Landmark.Landmark(3,3))
w.append(m)

w.append(robot1)
w.append(robot2)
w.append(robot3)
w.draw()
