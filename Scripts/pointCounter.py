import RPI.GPIO as GPIO 
import time 
import pointsDisplay as pts
BTNPIN = 13 #GPIO 27 
DISPLAYPIN = 15 #GPIO 22
counter = 0
#Method to check if the btn is 
#pressed and increases the counter if it is
def checkIfPush(): 
    while GPIO.input(BTNPIN): 
        counter += 1

     

def main(): 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BTNPIN, GPIO.IN)
    time.sleep(2)
    while True:     
        try:         
            checkIfPush()
        except KeyboardInterrupt: 
            counter = 0
            GPIO.cleanup()
if __name__ == "__main__": 
    main()
    

