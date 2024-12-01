from machine import Pin

# Setup of output pin; pin 25 controls onboard LED
onboardLED = Pin(25, Pin.OUT)
onboardLED.value(0)