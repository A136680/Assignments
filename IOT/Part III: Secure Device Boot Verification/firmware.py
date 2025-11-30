from machine import Pin
import time

led = Pin(2, Pin.OUT)   # built-in LED on many ESP32 boards

def main_loop():
    print("Firmware main loop is running...")
    while True:
        led.value(1)    # LED on
        time.sleep(0.5)
        led.value(0)    # LED off
        time.sleep(0.5)
