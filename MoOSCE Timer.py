import time 
from playsound import playsound

# define the countdown func. 
def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    print('Time over!') 
  
  
## input time in seconds if required
#prep = input("Enter the time in seconds: ") 

##pre-set timers:
prep = 115
station = 715
feedback = 175

print("Welcome to the MoOSCE timer.")
print("\n")
print("The programme runs after you type \'start\' and will repeat four times")
print("You can then type \'start\' again for another loop, or \'exit\' to quit.")
print("Should you need to cancel or restart, please press CTRL+C.")
print("\n")

#input("Press enter to start.") 
# function call 
def loop():
    for i in range(1,5):
        print("Rotation number " + str(i))
        playsound('Bell.wav')
        print("Start preparation (2 minutes)")
        countdown(int(prep))
        playsound('Bell.wav')
        print("Move on to station (12 minutes)")
        countdown(int(station))
        playsound('fbkgong.wav')
        print("Feedback time (3 minutes)")
        countdown(int(feedback))
    playsound('Bell.wav')
    print("This was the last station. Well done!")
    print("\n")

running = True

while running == True:
    strt = input("Please type \'start\' or \'exit\'")

    if strt == "start":
        loop()
    elif strt == "exit":
        running = False
    else:
        strt = input("Please type \'start\' or \'exit\'")
