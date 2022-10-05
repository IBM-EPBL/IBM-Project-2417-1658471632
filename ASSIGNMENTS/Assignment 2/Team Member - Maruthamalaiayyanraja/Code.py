import time
import random
i=0
while(i<=2000):
    i=i+1
    time.sleep(2) #2 SEC DELAY
    temp=random.randint(0,50)
    humid=random.randint(1,100)
    if temp>35:
        print("Temperature:",temp,"°C\n Temperature is High\n !!! ALERT HIGH TEMPERATURE !!!")
    else:
        print("Temperature:",temp,"°C\n Temperature is Normal")
    if humid>50:
        print("Humidity:",humid,"\nHumidity is high")
    else:
        print("Humidity:",humid,"\nHumidity is low")
