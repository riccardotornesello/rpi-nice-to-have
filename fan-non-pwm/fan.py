#!/usr/bin/python

import os
import sys
import time
import RPi.GPIO as GPIO


# CONFIGURATION
PIN = 23
MAX_TEMP = 65
TEMP_OFFSET = 10

# STATUS
fan_on = True

# UTILITIES
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return float(res.replace("temp=","").replace("'C\n",""))

def powerPin(turn_on: bool):
    global fan_on

    print('Changing fan status:', 'on' if turn_on else 'off')
    fan_on = turn_on
    return GPIO.output(PIN, turn_on)

# SCRIPT
if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)

    powerPin(True)

    while True:
        try:
            temp = getCPUtemperature()
            if fan_on and temp < MAX_TEMP - TEMP_OFFSET:
                powerPin(False)
            elif not fan_on and temp > MAX_TEMP:
                powerPin(True)

        except KeyboardInterrupt:
            powerPin(True)
            print("Exiting")
            sys.exit(0)
        except Exception as e:
            print("Unknown exception:", e)

        time.sleep(2)
