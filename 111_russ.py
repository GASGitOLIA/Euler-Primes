# original way

vi = 2;
a = 0.2;
#dt = 0.1;
dt = 0.199999999;
t = 0;

formatString = "Time is: %8.2f [s]  Distance:  %8.2f [m]";
 
print(); print("russ's way!"); print();
 
while t <= 2:
    d = vi*t + 0.5*a*t**2;
    print (formatString % (t, d));
    t = t + dt;

# original way with annoying modification...  will iterate one fewer times

t = 0;
dt = 0.200000001;  #notice this will iterate one fewer times...  might be unexpected!

print(); print("russ's way!"); print();
 
while t <= 2:
    d = vi*t + 0.5*a*t**2;
    print (formatString % (t, d));
    t = t + dt;

#method three...  will only iterate num times, in my case 10
    
num=10 #intervals
ti = 0.0000
totalTime = 2.000001 #seconds

print(); print("new more stable way!"); print();

for ii in list(range(0,num+1)):   # num plus 1 is 21, but the list will stop at 20
    currentTime = ti + totalTime * ii / num   #this is your floaty value
    d = vi*currentTime + 0.5*a*currentTime**2
    print (formatString % (currentTime, d));
    
    
