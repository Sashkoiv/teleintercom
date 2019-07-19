# This is your main script.
from machine import Pin, I2C
import time
import machine

def trololo():
    # construct an I2C bus
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

    return i2c.readfrom(104, 8)   # read 4 bytes from slave device with address 104

def gotosleep(time = 5):
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

    # set RTC.ALARM0 to fire after 10 seconds (waking the device)
    rtc.alarm(rtc.ALARM0, time*1000)

    # put the device to sleep
    machine.deepsleep()


if __name__ == "__main__":
    led = Pin(2, Pin.OUT)
    for i in range(5):
        led.value(not led.value())
        time.sleep(0.5)
        # led.value(1)
        # time.sleep(0.5)
    gotosleep(5)

Complete project details at https://RandomNerdTutorials.com