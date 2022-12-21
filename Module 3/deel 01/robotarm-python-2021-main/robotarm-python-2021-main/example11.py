from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
for i in range(8):
    robotArm.moveRight()

for i in range(9):
    robotArm.grab()
    scan = robotArm.scan()
    if scan == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()

robotArm.wait()