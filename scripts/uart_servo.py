import HiwonderServoController as servo

servo.setConfig('/dev/ttyUSB0', 1)
servo.moveServo(1, 500, 500)
servo.moveServo(2, 500, 500)
servo.moveServo(3, 200, 500)

print(servo.getBatteryVoltage())
list = [1, 2, 3]
print(servo.multServoPosRead(list))