import RPi.GPIO as GPIO
import time

power = 7
output_c = 5
switch = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(output_c, GPIO.OUT)
GPIO.setup(power, GPIO.OUT)
GPIO.output(power, GPIO.HIGH)

GPIO.setup(switch, GPIO.IN)
def switch_callback(gpio_pin):
  print(gpio_pin)
  GPIO.output(output_c, GPIO.HIGH)
GPIO.add_event_detect(switch, GPIO.FALLING, bouncetime=100)
GPIO.add_event_callback(switch, switch_callback)

try:
  while True:
    GPIO.output(output_c, GPIO.LOW)
    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()
