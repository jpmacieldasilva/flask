import time


class Timer():
    def __init__(self):
        self.minutes = 1
        self.paused = False
        self.finished = False
        self.time_min = None
        self.time_sec = None

    def countdown(self):
        num_of_secs = self.minutes*3

        while num_of_secs and self.paused == False:
            min, sec = divmod(num_of_secs, 60)
            self.time_min = min
            self.time_sec = sec
            time.sleep(1)
            num_of_secs -= 1
        self.finished = True
        print('Countdown finished.')

    def pause(self):
        self.paused = True

    def play(self):
        self.paused = False
        self.countdown()

    def reset_timer(self):
        self.minutes = self.minutes
        self.paused = False
        self.finished = False
