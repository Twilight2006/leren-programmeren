from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.grab()
for i in range(8):
    color = robotArm.scan()
    if color == 'red':
        for i in range(9):
            robotArm.moveRight()
        robotArm.drop()
    else:
        robotArm.drop()
        robotArm.moveRight()
        robotArm.grab()
    robotArm.wait()