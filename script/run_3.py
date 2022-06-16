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


for i in range(100):
    # biasなしのロボット
    nobias_robot = Robot.Robot(
        np.array([0, 0, 0]).T,
        sensor=None,
        agent=circling,
        color="gray",
        noise_per_meter=0,
        bias_rate_stds=(0.0, 0.0),
        expected_stuck_time=60.0,
        expected_escape_time=60.0,
        expeced_kidnap_time=5,
    )
    w.append(nobias_robot)
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
