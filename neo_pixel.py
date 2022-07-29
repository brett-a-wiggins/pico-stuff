import board
import neopixel
import time
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import RED


    
def health_meter(health):
    num_pixels = health
    pixels = neopixel.NeoPixel(board.GP0, num_pixels, brightness=0.1)
    pixels.brightness = 0.5
    pixels.fill((0,255,0))
    time.sleep(3)
    blink = Blink(pixels, speed=1, color=RED)
    animations = AnimationSequence(
    blink,
    auto_clear=True)
    animations.animate()
    time.sleep(0.3)
    pixels.deinit()
    return health - 1

health = 5
health = health_meter(health)
health = health_meter(health)



