#!/bin/bash
python myApp.py --port=10443 --mongodbip=192.168.0.188 --mongodbport=27017 > dataCollectorWebServer.log 2>&1 &
