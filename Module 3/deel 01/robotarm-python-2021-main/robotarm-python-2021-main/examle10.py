from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
aantal = 1       

for i in range (4):
    robotArm.moveRight()
for x in range (5):
    robotArm.grab()
    for j in range(aantal):
        robotArm.moveRight()
    robotArm.drop()
    for m in range(aantal+1):
        robotArm.moveLeft()
    aantal = aantal + 2
robotArm.wait()