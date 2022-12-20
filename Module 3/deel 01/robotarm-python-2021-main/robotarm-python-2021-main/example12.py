from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
x = 9
y = 8

for i in range (9):
    robotArm.grab()
    colour = robotArm.scan()
    if colour == 'red':
        for i in range (x):
            robotArm.moveRight()
        robotArm.drop()
        for i in range (y):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
    x = x - 1
    y = y - 1 
    
robotArm.wait()