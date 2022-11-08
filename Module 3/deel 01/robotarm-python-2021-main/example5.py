from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')


for i in range(7):
    robotArm.moveRight()

robotArm.grab()

for i in range(2):
    robotArm.moveRight()

robotArm.drop()

for i in range(7):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()

robotArm.wait()