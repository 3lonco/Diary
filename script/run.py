import world
import IdealRobot
import numpy as np
import math

w = world.World()
robot1 = IdealRobot.IdealRobot(np.array([2, 3, math.pi / 6]).T)
robot2 = IdealRobot.IdealRobot(np.array([-2, -1, math.pi / 5 * 6]).T, "red")
w.append(robot1)
w.append(robot2)
w.draw()
