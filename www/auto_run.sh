#!/bin/sh
cd /home/pi/mjpg-streamer-master/mjpg-streamer-experimental/
sudo ./mjpg_streamer -i "./input_raspicam.so" -o "./output_http.so -w ./www"  &
sh  /home/pi/sunny/net.sh &
cd /home/pi/mjpg-streamer-master/mjpg-streamer-experimental/www/
sudo python3 /home/pi/mjpg-streamer-master/mjpg-streamer-experimental/www/GetPage.py &

