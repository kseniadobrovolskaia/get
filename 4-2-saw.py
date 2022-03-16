import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = (26, 19, 13, 6, 5, 11, 9, 10)
GPIO.setmode(GPIO.BCM)
for elem in dac:
    GPIO.setup(elem, GPIO.OUT)

try:
    period = int(input("Period: "))
    t = period / 510
    for i in range(510):
        num = i
        if i > 255:
            num = 510 - i
        num_arr = decimal2binary(num)
        for i in range(len(dac)):
            GPIO.output(dac[i], num_arr[i])
        time.sleep(t)
        for elem in dac:
            GPIO.output(elem, 0)

finally:
    for elem in dac:
        GPIO.output(elem, 0)
    GPIO.cleanup()