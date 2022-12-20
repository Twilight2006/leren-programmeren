from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
    
rechts = 9
links = 9
robotarm = True
while robotarm == True:
    robotArm.grab()
    if robotArm.scan() == '':
        robotarm = False
    else:
        for j in range (rechts):
            robotArm.moveRight()
        robotArm.drop()
        for x in range (links):
            robotArm.moveLeft()
        rechts -= 1
        links -= 1
robotArm.wait()