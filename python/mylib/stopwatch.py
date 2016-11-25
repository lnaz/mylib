# -*- coding: utf-8 -*-
import time

class StopWatch():
    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        self.elapsed_time = int(self.end_time - self.start_time)
        return self.elapsed_time

    def format(self):
        h = int(self.elapsed_time / (60 * 60))
        m = int((self.elapsed_time - (h * 60 * 60)) / 60)
        s = int(self.elapsed_time - (h * 60 * 60) - (m * 60))
        formatted_elapsed_time = '{0:02d}:{1:02d}:{2:02d}'.format(h, m, s)
        return formatted_elapsed_time

    def format_print(self):
        formatted_elapsed_time = self.format()
        print (formatted_elapsed_time)
