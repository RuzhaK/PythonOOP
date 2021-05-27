class Time:
    max_hours=23
    max_minutes=59
    max_seconds=59
    def __init__(self,hours,minutes,seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

    def set_time(self,hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        hh = str(self.hours).zfill(2)
        mm = str(self.minutes).zfill(2)
        ss = str(self.seconds).zfill(2)
        return f"{hh}:{mm}:{ss}"
    def next_second(self):
        self.seconds=(self.seconds+1)%60
        self.minutes=(self.minutes+int(self.seconds==0))%60
        self.hours=(self.hours+int(self.minutes==0 and self.seconds==0))%24
        # if self.seconds<Time.max_seconds:
        #     self.seconds+=1
        # elif self.minutes<Time.max_minutes:
        #     self.minutes+=1
        #     self.seconds=0
        # elif self.hours<Time.max_hours:
        #     self.hours+=1
        #     self.minutes=0
        #     self.seconds=0
        # else:
        #     self.hours =0
        #     self.minutes = 0
        #     self.seconds = 0

        return self.get_time()

t = Time(0, 0, 0)
print(t.next_second())

