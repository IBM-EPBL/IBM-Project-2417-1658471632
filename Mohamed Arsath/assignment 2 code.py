import time
import random
i=0
while(i<=2000):
    i=i+1
    time.sleep(1) #5 SEC DELAY
    temp=random.randint(0,50)
    humid=random.randint(1,100)
    if temp>35:
        print("Temperature:",temp,"Temperature is High\n ALARAM IS ON")
    else:
        print("Temperature:",temp,"Temperature is Normal")
    if humid>50:
        print("Humidity:",humid,"Humidity is high")
    else:
        print("Humidity:",humid,"Humidity is low")
