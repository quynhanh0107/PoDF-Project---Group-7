from machine import Pin
import time
import utime
from time import sleep
from servo import Servo
import random

LED_PIN = 0
SWITCH_PIN = 13
SERVOHAND_PIN = 18
SERVOHEAD_PIN = 16
TRIGGER_PIN = 5
ECHO_PIN = 4
MOTOR1_PIN = 15
MOTOR2_PIN = 14
ENABLE_MOTOR_PIN = 17

led = Pin(LED_PIN, Pin.OUT)
switch = Pin(SWITCH_PIN, Pin.IN, Pin.PULL_UP)
servoHand = Servo(SERVOHAND_PIN)
servoHead = Servo(SERVOHEAD_PIN)
trigger = Pin(TRIGGER_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)
motor1 = Pin(MOTOR1_PIN, Pin.OUT)
motor2 = Pin(MOTOR2_PIN, Pin.OUT)
enable_motor = Pin(ENABLE_MOTOR_PIN, Pin.OUT)

handDown = 110
handUp = 40
handMiddle = (handDown + handUp) // 2
handThirds = (handDown - handUp) // 3


headDown = 50
headUp = 15
headMiddle = (headDown + headUp) // 2


speed = (0.02, 0.01, 0.005, 0.002, 0.001)
superSlowSpeed = 0.05

switchCount = 0
sensorCount = 0
func11Count = 0

func10Amount = 2
func11Amount = 7

#servo's starting position
servoHand.write(handDown)
servoHead.write(headDown)
#can rotate servo by giving angle, and speed
def rotate_servo(curServo, angle, speed):
    curAngle = int(curServo.read())
    direction = 1
    if curAngle > angle:
        direction = -1
    
    for i in range(curAngle, angle, direction):
        curServo.write(i)
        sleep(speed)
    curServo.write(angle)
    sleep(0.05)

def wiggle_servo(curServo, downPos, upPos, speed, length):
    for i in range(0,length):
        if i%2 == 0:
            rotate_servo(curServo, upPos, speed)
        else:
            rotate_servo(curServo, downPos, speed)
            
        
        
def ultra():
    trigger.low()
    utime.sleep_us(2)

    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    while echo.value() == 0:
        signaloff = utime.ticks_us()

    while echo.value() == 1:
        signalon = utime.ticks_us()
    
    timepassed = signalon - signaloff

    distance = (timepassed* 0.0342 / 2)
    
    sleep(0.01)
    return distance

def forward():
    print("forward")
    motor1.high()
    motor2.low()
    
def backward():
    print("backward")
    motor1.low()
    motor2.high()

def stop():
    motor1.low()
    motor2.low()

def move_box(direction, duration):
    
    print("move")
    direction()
    sleep(duration)
    stop()

def func1():
    rotate_servo(servoHead, headUp, speed[2])
    
    rotate_servo(servoHand, handUp, speed[2])
    led.off()
    rotate_servo(servoHand, handDown, speed[2])
    rotate_servo(servoHead, headDown, speed[2])

def rand_func():
    sleep_list = [0, 0, 0, 0, 0.05, 1, 2]
    sleep_time = random.choice(sleep_list)
    if sleep_time != 0:
        sleep(sleep_time)
    rotate_servo(servoHead, headUp, speed[random.randrange(4)])
    sleep_time = random.choice(sleep_list)
    if sleep_time != 0:
        sleep(sleep_time)
    rotate_servo(servoHand, handUp, speed[random.randrange(4)])
    led.off()
    sleep_time = random.choice(sleep_list)
    if sleep_time != 0:
        sleep(sleep_time)
    rotate_servo(servoHand, handDown, speed[random.randrange(4)])
    sleep_time = random.choice(sleep_list)
    if sleep_time != 0:
        sleep(sleep_time)
    rotate_servo(servoHead, headDown, speed[random.randrange(4)])

def func2():
    rotate_servo(servoHead, headUp, speed[3])
    rotate_servo(servoHand, handUp, speed[3])
    led.off()
    rotate_servo(servoHand, handDown, speed[3])
    rotate_servo(servoHead, headDown, speed[3])

def func3():
    rotate_servo(servoHead, headUp, speed[0])
    rotate_servo(servoHand, handUp, speed[0])
    led.off()
    rotate_servo(servoHand, handDown, speed[3])
    rotate_servo(servoHead, headDown, speed[3])

def func4():
    rotate_servo(servoHead, headUp, speed[0])
    sleep(1)
    rotate_servo(servoHand, handUp, speed[0])
    led.off()
    sleep(1)
    rotate_servo(servoHand, handDown, speed[0])
    sleep(1)
    rotate_servo(servoHead, headDown, speed[0])

def func5():
    rotate_servo(servoHead, headUp, speed[1])
    sleep(1)
    rotate_servo(servoHead, headDown, speed[1])
    rotate_servo(servoHead, headUp, speed[3])
    rotate_servo(servoHand, handUp, speed[3])
    
    led.off()
    rotate_servo(servoHand, handDown, speed[3])
    rotate_servo(servoHead, headDown, speed[3])

funcList1 = [func2, func3, func4, func5, rand_func, rand_func, rand_func, rand_func]
list1Length = len(funcList1)

def func6():
    wiggle_servo(servoHead, headDown, headUp, speed[3], 30)
    func2()
    

def func7():
    rotate_servo(servoHead, headUp, speed[1])
    rotate_servo(servoHand, handUp, speed[1])
    led.off()
    rotate_servo(servoHand, handDown, speed[1])
    rotate_servo(servoHead, headMiddle, speed[1])
    rotate_servo(servoHead, headUp, speed[4])
    rotate_servo(servoHand, handUp, speed[4])
    sleep(1)
    rotate_servo(servoHand, handDown, speed[0])

    rotate_servo(servoHead, headMiddle, speed[0])
    rotate_servo(servoHead, headUp, speed[4])

    rotate_servo(servoHand, handUp, speed[4])
    sleep(1)
    rotate_servo(servoHand, handDown, speed[4])
    rotate_servo(servoHand, handUp, speed[4])
    rotate_servo(servoHand, handDown, speed[4])
    rotate_servo(servoHand, handUp, speed[4])
    rotate_servo(servoHand, handUp, speed[4])
    rotate_servo(servoHand, handDown, speed[4])
    rotate_servo(servoHand, handUp, speed[4])
    rotate_servo(servoHand, handUp, speed[4])
    rotate_servo(servoHand, handDown, speed[4])
    rotate_servo(servoHand, handUp, speed[4])

    sleep(1)
    rotate_servo(servoHand, handDown, speed[0])
    rotate_servo(servoHead, headMiddle, speed[0])
    rotate_servo(servoHead, headUp, speed[4])
    sleep(2)
    rotate_servo(servoHead, headDown, speed[0])

def func8():
    rotate_servo(servoHead, headUp, speed[1])
    sleep(10)
    for i in range(1,4):
        rotate_servo(servoHand, handDown - handThirds * i, superSlowSpeed)
        if i == 3:
            led.off()
        sleep(3)
    
    rotate_servo(servoHand,handDown, speed[4])
    rotate_servo(servoHead, headDown, speed[4])

def func9():
    wiggle_servo(servoHead, headDown, headMiddle, speed[3], 50)
    wiggle_servo(servoHead, headMiddle, headUp, speed[3], 50)
    rotate_servo(servoHead, headUp, speed[4])

    for i in range(0, 25):
        wiggle_servo(servoHead, headMiddle, headUp, speed[3], 2)
        wiggle_servo(servoHand, handDown, handMiddle, speed[3], 2)
    for i in range(0, 25):
        wiggle_servo(servoHead, headMiddle, headUp, speed[3], 2)
        wiggle_servo(servoHand, handMiddle, handUp, speed[3], 2)
        led.off()
    
    for i in range(0, 25):
        wiggle_servo(servoHead, headMiddle, headUp, speed[3], 2)
        wiggle_servo(servoHand, handDown, handMiddle, speed[3], 2)
        
    rotate_servo(servoHand, handDown, speed[3])
    wiggle_servo(servoHead, headDown , headMiddle, speed[3], 50)
    rotate_servo(servoHead, headDown, speed[3])


funcList2 = [func6, func7, func8, func9]
list2Length = len(funcList2)

def func10():
    while ultra() < 10:
        if servoHand.read() > handUp:
            rotate_servo(servoHead, headUp, speed[4])
            rotate_servo(servoHand, handUp, speed[4])
            print("if")
        sleep(1)
        print("while")
    print("out")
    if servoHead.read() < headDown:
        rotate_servo(servoHand, handDown, speed[0])
        rotate_servo(servoHead, headDown, speed[0])
        
def func11():
    global func11Count
    while ultra() < 10 and func11Count < 50:
        if servoHand.read() > handUp:
            rotate_servo(servoHead, headUp, speed[4])
            rotate_servo(servoHand, handMiddle, speed[4])
            print("whiif")
            sleep(0.05)
        print("while")
        sleep(0.05)
        func11Count = 0
    func11Count += 1
    if func11Count > 50:
        rotate_servo(servoHand, handDown, speed[4])
        rotate_servo(servoHead, headDown, speed[4])
        func11Count = 0
    print(func11Count)
def func12():
    global func11Count
    if servoHand.read() > handUp:
        rotate_servo(servoHead, headUp, speed[4])
        rotate_servo(servoHand, handUp, speed[4])
        sleep(0.05)
        rotate_servo(servoHand, handMiddle, speed[4])
    func11Count = 0
    sleep(0.4)

sleep(0.1)

def func13():
    while ultra() < 10:
        move_box(random.choice([forward, backward]), random.uniform(0.0, 2.0))
        sleep(0.05)
def func14():
    move_box(forward, 0.5)
    move_box(backward, 0.5)
    move_box(forward, 0.5)
    move_box(backward, 0.5)
    move_box(forward, 0.5)
    move_box(backward, 0.5)
    rand_func()
    
def func15():
    move_box(forward, 5)
    rand_func()
    
funcList3 = [func14, func15]
list3Length = len(funcList3)
while True:
    if switch.value():
        led.on()
        
        if switchCount == 0:
            func1()
            print("first")
        elif switchCount <= list1Length:
            print("funclist1: ", len(funcList1))
            funcIndex = random.randrange(len(funcList1))
            funcList1[funcIndex]()
            funcList1.pop(funcIndex)
            
        elif switchCount <= list2Length + list1Length:
            print("funclist2: ", len(funcList2))
            funcIndex = random.randrange(len(funcList2))
            funcList2[funcIndex]()
            funcList2.pop(funcIndex)
        elif switchCount <= list2Length + list1Length + func10Amount:
            print("fourth")
            rand_func()
        elif switchCount <= list2Length + list1Length + func10Amount + func11Amount:
            print("fifth")
            func12()
        elif switchCount <= list2Length + list1Length + func10Amount + func11Amount + list3Length:
            funcIndex = random.randrange(len(funcList3))
            funcList3[funcIndex]()
            funcList3.pop(funcIndex)
        else:
            funcList1 = [func2, func3, func4, func5, rand_func,rand_func,rand_func,rand_func] 
            funcList2 = [func6, func7, func8, func9]
            funcList3 = [func14, func15]
            switchCount = 0

        switchCount += 1
        print(switchCount)
        
        
        #rotate_servo(servoHead, headUp, speed[0])
        #rotate_servo(servoHand, handUp, speed[0])
    else:
        led.off()
        #print(ultra())

        #rotate_servo(servoHand, handDown, speed[0])
        #rotate_servo(servoHead, headDown, speed[0])
        
        if list2Length + list1Length < switchCount <= list2Length + list1Length + func10Amount:
            func10()
            #print("first else")
        elif list2Length + list1Length + func10Amount < switchCount <= list2Length + list1Length + func10Amount + func11Amount:
            func11()
            #print("second else")
        elif list2Length + list1Length + func10Amount + func11Amount < switchCount <= list2Length + list1Length + func10Amount + func11Amount + list3Length:
            func13()
        else:
            rotate_servo(servoHand, handDown, speed[3])
            rotate_servo(servoHead, headDown, speed[3])
        
    sleep(0.1)