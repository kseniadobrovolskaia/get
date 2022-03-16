import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)


try:
    k = 0
    while True:
        
        p = GPIO.PWM(22, 1000)
        p.start(k)
        k = int(input("Koefficient: "))
        p.stop()

finally:
    GPIO.output(22, 0)
    GPIO.cleanup()