import RPi.GPIO as GPIO 
import time #from pointsDisplay import pts
import pointsDisplay as pts

BTNPIN = 13 #GPIO 27 
DISPLAYPIN = 11 #GPIO 17
counter = 0
ispressed = 0
#Method to check if the btn is 
#pressed and increases the counter if it is
     

def main(): 
    global counter
    counter = 0
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)    
        # Button setup
    GPIO.setup(BTNPIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.add_event_detect(BTNPIN, GPIO.RISING, callback=pressed)
        
            
def pressed(channel):
    global ispressed
    print('GOT PRESSED')
    ispressed += 1
    print(ispressed)
    pts.numberDisplay(ispressed)
    time.sleep(0.4)
    
    
    
if __name__ == "__main__":
    try:
        pts.TM1638_init() 
        main()
    except KeyboardInterrupt:
        pts.numberDisplay(0)
        GPIO.cleanup()
