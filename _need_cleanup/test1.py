

















user_input = raw_input("Which direction you want me to move in?=")
user_input1 = raw_input("and for how long (in secs)=")
 
t=int(user_input1)  

if user_input == "r":
   turn_right(t)

elif user_input=="l":
   turn_left(t)  
   
elif user_input=="f":
   forward(t) 

elif user_input=="b":
   reverse(t)

else:
 print "wrong input. Please type f,b,r or l"




 user_input
print user_input1
