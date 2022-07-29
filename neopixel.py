import time
import board
import neopixel

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 5

pixels = neopixel.NeoPixel(board.GP0, num_pixels)
pixels.brightness = 0.5

while True:
    pixels.fill((255, 0, 0))
    time.sleep(0.5)
    pixels.fill((0, 255, 0))
    time.sleep(0.5)
    pixels.fill((0, 0, 255))
    time.sleep(0.5)