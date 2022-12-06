#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f"Sorry! This program requires Python >= 3.6 😅"

"""speedtest-mqtt.py: Monitor the internet connection speed."""

import json
import os
import speedtest
import time
import paho.mqtt.client as paho
from dotenv import load_dotenv, find_dotenv
# set custom .env file-path if your file isn't found
load_dotenv(find_dotenv())

app_mode = os.getenv("app_mode")
interval = int(os.getenv("interval"))
broker = os.getenv("broker")
port = int(os.getenv("port"))
topic = os.getenv("topic")
user = os.getenv("user")
password = os.getenv("password")
test_server = [] if os.getenv("test_server") == "False" else [int(os.getenv("test_server"))]


def testDownSpeed():
	if app_mode == 'debug':
		print("Starting Download test...")
	start = time.time()
	speedtester = speedtest.Speedtest()
	speedtester.get_servers(test_server)
	best_server = speedtester.get_best_server()
	speed = round(speedtester.download() / 1000 / 1000)
	end = time.time()
	total_elapsed_time = (end - start)
	if app_mode == 'debug':
		print("Publishing Download result {} to MQTT...".format(speed))
	publishToMqtt('down', speed)
	publishToMqtt('name', best_server["sponsor"])


def testUpSpeed():
	if app_mode == 'debug':
		print("Starting Upload test...")
	start = time.time()
	speedtester = speedtest.Speedtest()
	speedtester.get_servers(test_server)
	speedtester.get_best_server()
	speed = round(speedtester.upload() / 1000 / 1000)
	end = time.time()
	total_elapsed_time = (end - start)
	if app_mode == 'debug':
		print("Publishing Upload result {} to MQTT...".format(speed))
	publishToMqtt('up', speed)


def on_publish(client,userdata,result):
    pass


def publishToMqtt(test, speed):
	mqtt = paho.Client("speedtest")
	mqtt.username_pw_set(user, password=password)
	mqtt.on_publish = on_publish
	mqtt.connect(broker,port)
	ret= mqtt.publish(topic+"{}".format(test),speed)
	mqtt.disconnect()


def main(interval):
	while True:
		if app_mode == 'debug':
			print("Starting Network Tests....")
		testDownSpeed()
		testUpSpeed()
		if app_mode == 'debug':
			print("Tests Completed...")
		if interval > 0:
			print("Time to sleep for {} seconds\n".format(interval))
			time.sleep(interval)
		else:
			if app_mode == 'debug':
				print("No Interval set...exiting...\n")
			sys.exit()


if __name__ == "__main__":
    main(interval)


__author__ = "Rodney Smith"
__copyright__ = "Copyright 2022"
__license__ = "GPL"
__version__ = "1.0.0"
__contact__ = "rodney.delauer@gmail.com"
__status__ = "Development"
