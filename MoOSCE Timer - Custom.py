import time 
from playsound import playsound

##pre-set variables:
#prep = 1 #115
#station = 1 #715
#feedback = 1 #175
#num_stations = 1 #4

#Function definitions below. get int, setup, timer, loop
def get_int(x):
    while True:
        try:
            return int(x)
        except ValueError:
            x = input("Try again - please enter a number: ")
            

def setup():    
    print("Input time in seconds as required.")
    print("As a guide: 60 seconds = 1 minute, 120 = 2 mins; 180 = 3 mins; 720 = 12 mins.")
    print("Minimum time for each is 30 seconds.")

    prep = get_int(input("Enter preparation time in seconds: "))
    station = get_int(input("Enter station time in seconds: "))
    feedback = get_int(input("Enter feedback time in seconds: "))
    num_stations = get_int(input("Enter number of stations: "))

    if num_stations < 1:
        print("There will be one station - this is the minimum.")
        num_stations = 1

#Setting minimums
    if prep < 30:
        prep = 30
    if station < 30:
        station = 30
    if feedback < 30:
        feedback = 30

    print(f"Your timings are as follows: preparation will be {prep} seconds, stations are {station} seconds, and feedback is {feedback} seconds")
    print(f"There will be {num_stations} stations.")

    #Remove 5 seconds off each to accout for slight delay after sound is played.
    prep -= 5
    station -= 5
    feedback -=5

    return prep, station, feedback, num_stations


def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    print('Time over!') 


def loop(num_stations):
    num_stations += 1
    for i in range(1,num_stations):
        print("Rotation number " + str(i))
        print(f"Start preparation: {prep + 5} seconds")
        playsound('Bell.wav')
        countdown(prep)
        print(f"Move on to station: {prep + 5} seconds")
        playsound('Bell.wav')
        countdown(station)
        print(f"Feedback time {feedback + 5} seconds")
        playsound('fbkgong.wav')
        countdown(feedback)
    playsound('Bell.wav')
    print("This was the last station. Well done!")
    print("\n")

print("Welcome to the MoOSCE timer.")
print("\n")
print("The programme runs after you type \'start\', it will ask you")
print("how many stations there are, and how much time")
print("you want to allocate for preparation, stations, and feedback")
print("After each loop, you can type \'start\' again for another loop, or \'exit\' to quit.")
print("Should you need to cancel or restart, please press CTRL+C.")
print("\n")


full_setup = setup()
prep = full_setup[0]
station = full_setup[1]
feedback = full_setup[2]
num_stations = full_setup[3]

running = True

while running == True:
    strt = input("Please type \'start\', \'setup\', or \'exit\' >>> ").lower()

    if strt == "start":
        loop(num_stations)
    elif strt == "setup":
        full_setup = setup()
    elif strt == "exit":
        running = False
    else:
        strt = input("Please type \'start\', \'setup\', or \'exit\' >>> ").lower()
