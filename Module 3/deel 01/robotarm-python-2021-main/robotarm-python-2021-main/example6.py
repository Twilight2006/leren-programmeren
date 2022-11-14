from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

robotArm.moveRight()
robotArm.grab()

for i in range(6):
    print(i)
    color = robotArm.scan()
    if color == 'white':
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
        

    elif color == 'red':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        
    if i < 5:
        robotArm.grab()


robotArm.wait()