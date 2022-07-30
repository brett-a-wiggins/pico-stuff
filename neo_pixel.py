import board
import neopixel
import time
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import RED, GREEN, BLACK

NUM_PIXELS = 5
pixels = neopixel.NeoPixel(board.GP0, NUM_PIXELS, brightness=0.1)

def pixel_fill(colour, size):
    index = 0
    while index < size:
        pixels[index] = colour
        index += 1
    while index < NUM_PIXELS:
        pixels[index] = BLACK
        index += 1

def display_health(colour, level, delay=0.0):
    print("display_health(): {0} {1} {2}".format(colour, level, delay))
    pixels.brightness = 0.5
    pixel_fill(colour, level)
    time.sleep(delay)

"""
    blink = Blink(pixels, speed=1, color=RED)
    animations = AnimationSequence(blink, auto_clear=True)
    animations.animate()
    time.sleep(delay)
"""

# TODO: Make sure health level > zero
def take_damage(level, damage):
    print("take_damage(): {0} {1}".format(level, damage))
    display_health(RED, level, 0.5)
    level = level - damage
    display_health(GREEN, level)
    return level

health_level = 5
display_health(BLACK, health_level, 0.5)
display_health(GREEN, health_level, 0.5)
# TODO: while loop !
health_level = take_damage(health_level, 1)
