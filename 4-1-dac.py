import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
for elem in dac:
    GPIO.setup(elem, GPIO.OUT)

try:
    while True:
        answer = input("Number or q for exit: ")
        if answer == 'q':
            break
        if answer.isdigit() == 0:
            print("Try again")
        else:
            num = int(answer)
            if num < 0 or num > 255:
                print("Number very big")
         
            else:
                num_arr = []
                num_arr = decimal2binary(num)
                for i in range(len(dac)):
                    GPIO.output(dac[i], num_arr[i])
                V = 3.3 / 2**len(dac) * num
                print(V)
                time.sleep(3)
    
finally:
    for elem in dac:
        GPIO.output(elem, 0)

    GPIO.cleanup()





