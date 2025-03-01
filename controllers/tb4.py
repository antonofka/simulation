import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
target_directory = os.path.join(current_directory, '..', 'api')
sys.path.append(target_directory)

import traceback
import controller
import robot
import turtlebot

robot_controller = controller.Robot()
turtlebot.Robot._robot = robot_controller
spinner = robot.Robot(turtlebot.Robot())

while robot_controller.step(32) != -1:
    try:
        spinner.spin()
    except Exception:
        print(traceback.format_exc())
