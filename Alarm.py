from tkinter import *
import datetime
import time


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        currentTime = datetime.datetime.now()
        now = currentTime.strftime("%H:%M:%S")
        date = currentTime.strftime("%d/%d/%Y")
        print("The Set Date is:", date)
        print(now)

        if now == set_alarm_timer:
            print("UP UP UP")
            # FIXME add playsound MP3 file
            break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


clock = Tk()

clock.title("PyAlarm Clock")
clock.geometry("400x200")

timeFormat = Label(clock, text="Enter the time in 24h format!", fg="red", bg="black", font="Arial").place(x=60, y=120)
addTime = Label(clock, text="Hour  Min  Sec", font=60).place(x=110)
setAlarm = Label(clock, text="When to wake up", fg="blue", relief="solid", font=("Helevetica", 7, "bold")).place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock, textvariable=hour, bg="pink", width=15).place(x=110, y=30)
minTime = Entry(clock, textvariable=min, bg="pink", width=15).place(x=150, y=30)
secTime = Entry(clock, textvariable=sec, bg="pink", width=15).place(x=200,y=30)

submit = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time).place(x=110, y=70)

clock.mainloop()
