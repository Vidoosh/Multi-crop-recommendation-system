# import the necessary packages
import time
import board
import adafruit_dht
import psutil

# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

# Initial the dht device, with data pin connected to digital pin 23:
sensor = adafruit_dht.DHT11(board.D23)

# Loop forever and print the temperature and humidity
while True:
    try:
        # Print the values to the serial port
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
    # Errors happen fairly often, DHT's are hard to read, just keep going
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    # Exit the program cleanly
    except Exception as error:
        sensor.exit()
        raise error
    # Wait a second before continuing
    time.sleep(2.0)