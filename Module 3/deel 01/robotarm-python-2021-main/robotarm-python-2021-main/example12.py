from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
for i in range(14):    
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for i in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(8):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()

robotArm.wait()