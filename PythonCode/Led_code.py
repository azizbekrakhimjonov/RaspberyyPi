from gpiozero import LED          
from gpiozero import Button        

led = LED(4)
button = Button(17)

while True:
        button.wait_for_press()
        led.on()
        button.wait_for_release()
        led.off()



# from gpiozero import LEDBoard

# leds = LEDBoard(2, 3, 4, 5, 6)
# leds.on()




# from gpiozero import LEDBoard

# leds = LEDBoard(2, 3, 4, 5)
# leds.on()      # turn on all LEDs
# leds.off(0)    # turn off the first LED (pin 2)
# leds.off(-1)   # turn off the last LED (pin 5)
# leds.off(1, 2) # turn off the middle LEDs (pins 3 and 4)
# leds.on()      # turn on all LEDs




# from gpiozero import LEDBoard

# leds = LEDBoard(2, 3, 4, 5)
# leds.on(0)    # turn on the first LED (pin 2)
# leds.on(-1)   # turn on the last LED (pin 5)
# leds.on(1, 2) # turn on the middle LEDs (pins 3 and 4)
# leds.off()    # turn off all LEDs
# leds.on()     # turn on all LEDs