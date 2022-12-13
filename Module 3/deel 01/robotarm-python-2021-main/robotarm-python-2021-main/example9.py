from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.grab()
for i in range(9):
    robotArm.moveRight()
robotArm.drop()
for i in range(2):
    for i in range(8):
        robotArm.moveLeft()
    robotArm.grab()
    for i in range(7):
        robotArm.moveRight()
    robotArm.drop()

    robotArm.wait()