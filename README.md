# palestra_iot
código apresentado na palestra sobre IOT

https://docs.google.com/presentation/d/1XE3g4SLHyy9Y8WbTIzfTV1Hqn3x61cO1njFGQo-b6cQ/edit?usp=sharing

Para teste do broker mqtt via cliente mosquitto em desktop ubuntu:

$ sudo apt-get install mosquitto-clients

$ mosquitto_pub -h "m11.cloudmqtt.com" -p 15034 -t "hello/world" -q 1 -m "1" -u "oyqmvonl" -P "eCPIJkxVFWBU"

$ mosquitto_sub -h "m11.cloudmqtt.com" -p 15034 -t "hello/world" -q 1 -u "oyqmvonl" -P "eCPIJkxVFWBU"
