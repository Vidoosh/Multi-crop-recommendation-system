# Setup the Raspberry Pi
Update Raspberry Pi OS and install & update python3
```shell
sudo apt update
sudo apt full-upgrade
sudo apt install python3-pip
sudo pip3 install --upgrade setuptools
sudo reboot
```
Install required Adafruit libraries
 
```shell
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
```
```shell
pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2
```