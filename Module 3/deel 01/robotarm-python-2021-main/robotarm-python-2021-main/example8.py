from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
for i in range(8):
    for i in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(8):
        robotArm.moveLeft()
    robotArm.grab()
robotArm.wait()