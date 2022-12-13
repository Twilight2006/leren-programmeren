from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.grab()
for i in range(8):
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft() 
    robotArm.grab()