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


def getnum(arr):
    num = 0
    for i in range(8):
        num += arr[i] * (2 ** (7 - i))
    return num


def adc():
    arr = [0, 0, 0, 0, 0, 0, 0, 0]
    num = 0
    for i in range(8):

        arr[i] = 1
        num = getnum(arr)

        if i == 8:
            return

        num2dac(num)
        time.sleep(0.01)

        compval = GPIO.input(comp)

        if (compval == 0):
            arr[i] = 0
    print(num / 256 * 3.3)
    return num

GPIO.setmode(GPIO.BCM)
for elem in dac:
    GPIO.setup(elem, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        number = adc()
        num_arr = []
        num_arr = decimal2binary(number)
        for i in range(len(dac)):
            GPIO.output(dac[i], num_arr[i])
        V = 3.3 / 2 ** len(dac) * number
        print(V)
        time.sleep(3)


finally:
    for elem in dac:
        GPIO.output(elem, 0)
    GPIO.output(troyka, 0)

    GPIO.cleanup()
