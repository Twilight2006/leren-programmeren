from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
robotArm.grab()
for i in range(9):
    robotArm.moveRight()
robotArm.drop()
for i in range(8):
    robotArm.moveLeft()

robotArm.wait()