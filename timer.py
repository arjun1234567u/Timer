import time
def countdown(t):
    seconds = t * 60
    while seconds:
        mins,secs = divmod(seconds,60)
        timer = f"{mins:02d}:{secs:02d}"
        print (timer,end = '\r')
        time.sleep(1)
        seconds-=1
    print ("time up bye bye")
t = input ("enter time in minutes ")
countdown(int(t))