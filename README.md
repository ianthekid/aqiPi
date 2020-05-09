# aqiPi - Air Quality Monitor

Turn your RaspberryPi into an air quality monitor

## Requirements

* Raspberry Pi
* [SDS011 Sensor](https://aqicn.org/sensor/sds011/)

## Setup

1. Install Nginx

```shell
$ sudo apt-get update
$ sudo apt-get install nginx
```

2. Add the `public` files into the web directory created by Nginx

```shell
$ sudo cp public/* /var/www/html
```

3. Add cronjob to start the air quality sensor reading and readings on startup

```shell
$ crontab -e
```

Add the following lines to the bottom 

```
@reboot /usr/bin/python /home/pi/aqi.py 2>&1
@reboot /usr/bin/python -W ignore /home/pi/chrome.py 2>&1
```


#### Optional settings


```
## /boot/config.txt
disable_splash=1
gpu_mem=320 
```

That's it. Now just reboot your Pi and it should start reading out the PM2.5/10 AQI