import RPi.GPIO as GPIO
import time

input_c = 7
output_c = 5
mode = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(output_c, GPIO.OUT)

try:
  while True:
    if mode:
      GPIO.output(output_c, GPIO.HIGH)
      mode = 0
    else:
      GPIO.output(output_c, GPIO.LOW)
      mode = 1
    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()
