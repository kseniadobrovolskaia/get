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
    for i in range (8):
        
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
    

       
    # for i in range(256):
            
    #         signal = num2dac(i)
    #         time.sleep(0.01)
    #         compval = GPIO.input(comp)
    #         if compval == 0:
    #             print("ADC VALUE = {:^3} -> {} input voltage = {:.2f}".format(i, signal, volt))
    #             break
    # return i


GPIO.setmode(GPIO.BCM)
for elem in dac:
    GPIO.setup(elem, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)


try:
    while True:
        adc()
        
        
finally:
    for elem in dac:
        GPIO.output(elem, 0)
    GPIO.output(troyka, 0)

    GPIO.cleanup()


