import numpy as np
import math
import world
import Agent
import map
import Agent
import Landmark
import Robot
import Camera


w = world.World(30, 0.1)
# add three Landmarks after creating an instance of Map
m = map.Map()
m.append_landmark(Landmark.Landmark(-4, 2))
m.append_landmark(Landmark.Landmark(3, 3))
m.append_landmark(Landmark.Landmark(3, 3))
w.append(m)

# Create an instance of Robot Class with Agent that let the instace move move in a circumferential direction
circling = Agent.Agent(0.2, 10.0 / 180 * math.pi)
r = Robot.Robot(np.array([0, 0, 0]).T, sensor=Camera.Camera(m), agent=circling)
w.append(r)

w.draw()
