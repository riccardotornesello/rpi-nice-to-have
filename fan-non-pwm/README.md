# Fan non PWM

This script allows you to control the turning on and off of a non-pwm fan based on the CPU temperature of the Raspberry Pi.

## Hardware

Picture TBD

A transistor is needed to control the current flow to the fan.

## The code

Details TBD

## Installation

1. Copy the python script `fan.py` contained in this folder.
2. Configure it (more details in the previous section)
3. Copy the `fan.service` file from this folder in `/etc/systemd/system/fan.service`
4. Replace `ExecStart` with the location of `fan.py`
5. Run `sudo systemctl daemon-reload`, `sudo systemctl enable fan.service` and `sudo systemctl start fan.service`
