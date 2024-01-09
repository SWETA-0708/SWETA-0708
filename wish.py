import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))
print(hour)
# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)


if(hour>0 and hour<12):
    print("GOOD MORNING")
elif(hour>=12 and hour<17):
    print("good afternoon")
elif(hour>=17 and hour<0):
  print("good night")
 
   


