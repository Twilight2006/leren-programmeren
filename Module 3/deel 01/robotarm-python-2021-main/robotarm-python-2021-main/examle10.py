from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
rechts = 1
links = 2        

for i in range (4):
    robotArm.moveRight()
for x in range (5):
    robotArm.grab()
    for j in range(rechts):
        robotArm.moveRight()
    robotArm.drop()
    for m in range(links):
        robotArm.moveLeft()
    rechts = rechts + 2
    links = links + 2
robotArm.wait()