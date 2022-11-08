from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

robotArm.moveRight()
robotArm.grab()

for i in range(5):
    color = robotArm.scan()
    if color == 'red':
        robotArm.moveRight()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
        robotArm.grab()

    elif color == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.grab()

robotArm.moveRight()
robotArm.moveRight()
robotArm.drop()

robotArm.wait()