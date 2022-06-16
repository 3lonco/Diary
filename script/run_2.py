import numpy as np
import Agent
import world
import math
import Robot
import copy

w = world.World(30, 0.1, debug=False)
for i in range(100):
    circling = Agent.Agent(0.2, 10.0 / 180 * math.pi)
    r = Robot.Robot(pose=np.array([0, 0, 0]).T, sensor=None, agent=circling)
    w.append(r)
    print(i)

print("start draw")
w.draw()
