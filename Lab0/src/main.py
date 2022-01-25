"""!
@file main.py
This file contains code which cycles through a sawtooth waveform LED pattern. 

@details The main script calls the led_setup and led_brightness functions 
repeatedly in a loop to make the LED brightness slowly increase from 0 to maximum 
over 5 seconds, then go back to 0 and repeat the process indefinitely until someone 
cuts off the power or presses Ctrl-C.

@author Nishka Chawla
@author Ronan Shaffer
@date   12-Jan-2022
@copyright (c) Released under GNU Public License
"""

import pyb
import time
import utime
import math

def led_setup ():
    """!
    This function prepares the PWM timer and channel.
    """
    ## Pin A1 object set as an output. 
    pinA1 = pyb.Pin (pyb.Pin.board.PA1, pyb.Pin.OUT_PP)
    ## Pin A0 object set as an output. 
    pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    ## Timer object used to define timer number and timer frequency.
    tim2 = pyb.Timer (2, freq=20000)
    ## Channel object used to define channel number, PWM mode, and pin object.
    ch2 = tim2.channel (1, pyb.Timer.PWM_INVERTED, pin=pinA0)

def led_brightness ():
    """!
    This function sets the PWM duty cycle.
    """
    ## Pin A1 object set as an output. 
    pinA1 = pyb.Pin (pyb.Pin.board.PA1, pyb.Pin.OUT_PP)
    ## Pin A0 object set as an output. 
    pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    ## Timer object used to define timer number and timer frequency.
    tim2 = pyb.Timer (2, freq=20000)
    ## Channel object used to define channel number, PWM mode, and pin object.
    ch2 = tim2.channel (1, pyb.Timer.PWM_INVERTED, pin=pinA0)
    ## Instantiation of current time variable. 
    current_time = utime.ticks_ms()
    # Instantiation of variable used to find the difference between the start time and current time.
    time_diff = utime.ticks_diff(current_time,start_time)
    # Scales time into microseconds.
    time_diff = time_diff/1000

    ch2.pulse_width_percent (20*(time_diff%5.0))
       

if __name__ == "__main__":
    import pyb
    import time
    ## Instantiation of start time variable. 
    start_time = utime.ticks_ms()
    
    while True:
        led_setup()
        led_brightness()
        
        


