traffic_speed=int(input("enter traffic speed"))
traffic_speed_limit=80
if(traffic_speed <= traffic_speed_limit):
    print("no traffic violation")
else:
    print("violated traffic speed limit")