from collections import deque
import random
import time

"""
Project 1: IoT Sensor Network – Smart Room Temperature Alert System
## Step-by-Step Plan:
1. Simulate real-time temperature sensor readings.
2. Use a sliding window with deque to track recent values.
3. Calculate average, detect if new reading is >20% deviation.
4. Raise alerts in real-time.
"""

WINDOW_SIZE=5  # maximum size of single window
THREEDOLD=0.2  # temperature deviationa allow

window=deque(maxlen=WINDOW_SIZE)  # use deque to create window so can use sliding window to measure real time temp deviation

def get_fake_temperature():
    """semulate sensor temperature (could be 20-30*C """
    return random.uniform(19,35)  # this will create temperature

def check_temperature(reading,window):
    if len(window) == WINDOW_SIZE:  # check window size
        avg=sum(window)/len(window)   # calculate average of temperature
        deviation=abs(reading - avg)/avg  # calculate deviation
        if deviation > THREEDOLD:   # ig feviation greater that 0.2 raise alert
            print(f"⚠️ Alert! Temp: {reading:.2f}°C | Average : {avg:.2f}°C | Daviation : {deviation*100:.2f}%.")
        else:
            print(f"✅ Normal Temp: {reading:.2f}°C | Average : {avg:.2f}°C")
    window.append(reading) # update temperature reading, by removing first value and adding new value (FIFO)

for _ in range(15): # iterate 15 times
    temp=get_fake_temperature()
    check_temperature(temp,window)
    time.sleep(0.5)


"""
✅ Normal Temp: 24.41°C | Average : 26.62°C
✅ Normal Temp: 30.30°C | Average : 26.44°C
✅ Normal Temp: 32.36°C | Average : 28.33°C
✅ Normal Temp: 24.11°C | Average : 29.42°C
✅ Normal Temp: 32.38°C | Average : 27.74°C
⚠️ Alert! Temp: 22.88°C | Average : 28.71°C | Daviation : 20.32%.
✅ Normal Temp: 32.37°C | Average : 28.41°C
⚠️ Alert! Temp: 22.98°C | Average : 28.82°C | Daviation : 20.26%.
✅ Normal Temp: 24.01°C | Average : 26.94°C
✅ Normal Temp: 21.90°C | Average : 26.93°C
"""

"""
same idea can be applied for below projects
1. IoT Sensor Networks
2. Healthcare Monitoring
3. Server Monitoring
4. Fraud Detection
"""