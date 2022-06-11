
import world
import IdealRobot
import numpy as np
import math

w = world.World()
robot1 = IdealRobot.IdealRobot(np.array([2,3,math.pi/6]).T)
w.append(robot1)
w.draw()