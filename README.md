# Speedtest to MQTT
This script was created to provide network speedtest results to a MQTT sensor in  [HomeAssistant](https://home-assistant.io). The python speedtest-cli is resource intensive and is recommended to be run on a system other than your main [HomeAssistant](https://home-assistant.io) instance. The script is constrained by the system's network adapter and network equipment.

## Requirements
* You will need python to execute this script.
* You will need a MQTT sever that you can publish to.

## Installation
* Install the app by cloning this repo
 - `git clone https://github.com/Rodney-Smith/speedtest-mqtt`
* Install the required python libraries:
 - `pip install -r requirements.txt`
* Edit the env-sample and save as .env

## Features
* This script publishes speedtests to the topic of your choice where the test is either `download` or `upload`.
* This script utilizes the python `speedtest-cli` library.
* This script is built to run continuously and will pause for the interval set in the `.env` file.

## Compatibility
This script was tested using python 3.9.6
