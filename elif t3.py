signal_light=str(input("Enter the signal_color(red,yellow,green):"))
if(signal_light=="red"):
    print("stop")
elif(signal_light=="green"):
    print("go")
elif(signal_light=="yellow"):
    print("ready")
else:
    print("not recognized")