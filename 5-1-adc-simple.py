import RPi.GPIO as GPIO
import time


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal


GPIO.setmode(GPIO.BCM)
for elem in dac:
    GPIO.setup(elem, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)


try:
    while True:
        for i in range(256):
            
            signal = num2dac(i)
            time.sleep(0.01)
            volt = i / 256 * 3.3
            compval = GPIO.input(comp)
            if compval == 0:
                print("ADC VALUE = {:^3} -> {} input voltage = {:.2f}".format(i, signal, volt))
                break
finally:
    for elem in dac:
        GPIO.output(elem, 0)
    GPIO.output(troyka, 0)

    GPIO.cleanup()






