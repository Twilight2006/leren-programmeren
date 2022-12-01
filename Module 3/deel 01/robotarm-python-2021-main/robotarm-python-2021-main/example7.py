from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
for i in range(6):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

robotArm.wait()