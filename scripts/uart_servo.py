import HiwonderServoController as servo
import time

servo.setConfig('/dev/ttyUSB0', 1)
# servo.moveServo(1, 400, 500)
# servo.moveServo(2, 400, 500)
# servo.moveServo(3, 400, 500)
# servo.moveServo(4, 400, 500)
# servo.moveServo(5, 400, 500)
# servo.moveServo(6, 400, 500)
# servo.moveServo(7, 400, 500)
# servo.moveServo(8, 400, 500)
# servo.moveServo(9, 400, 500)
# servo.moveServo(10, 400, 500)
# servo.moveServo(11, 400, 500)
# servo.moveServo(12, 400, 500)
# servo.moveServo(13, 400, 500)
# servo.moveServo(14, 400, 500)
# servo.moveServo(15, 400, 500)
# servo.moveServo(16, 400, 500)
# servo.moveServo(17, 400, 500)
# servo.moveServo(18, 400, 500)
# time.sleep(2)
servo.moveServo(1, 500, 500)
servo.moveServo(2, 500, 500)
servo.moveServo(3, 600, 500)

servo.moveServo(4, 500, 500)
servo.moveServo(5, 450, 500)
servo.moveServo(6, 400, 500)

servo.moveServo(7, 500, 500)
servo.moveServo(8, 520, 500)
servo.moveServo(9, 600, 500)

servo.moveServo(10, 500, 500)
servo.moveServo(11, 500, 500)
servo.moveServo(12, 400, 500)

servo.moveServo(13, 500, 500)
servo.moveServo(14, 500, 500)
servo.moveServo(15, 600, 500)

servo.moveServo(16, 500, 500)
servo.moveServo(17, 500, 500)
servo.moveServo(18, 400, 500)

# print(servo.getBatteryVoltage())
# list = [1, 2, 3]
# print(servo.multServoPosRead(list))