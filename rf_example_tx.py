# A micro:bit Firefly.
# By Nicholas H.Tollervey. Released to the public domain.
import radio
from microbit import display, Image, button_a, button_b, sleep


# The radio won't work unless it's switched on.
radio.on()

# Event loop.
while True:
    # Button A sends a "flash" message.
    if button_b.was_pressed():
        radio.send('flash')  # a-ha