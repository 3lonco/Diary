import world
import Agent
import IdealRobot
import Robot
import numpy as np
import math

# 描画用のロボット
w = world.World(30, 0.1, debug=False)

# 円運動させるAgent
circling = Agent.Agent(0.2, 10 / 180 * math.pi)

# biasなしのロボット
nobias_robot = IdealRobot.IdealRobot(
    np.array([0, 0, 0]).T, sensor=None, agent=circling, color="gray"
)
print("Created nobias_robot")
w.append(nobias_robot)
print("appended nobias_robot in the world")
biased_robot = Robot.Robot(
    np.array([0, 0, 0]).T,
    sensor=None,
    agent=circling,
    color="red",
    noise_per_meter=0,
    bias_rate_stds=(0.2, 0.2),
)
w.append(biased_robot)
w.draw()
