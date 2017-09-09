# -*- coding: utf-8 -*-
import logging
import math

def print_speed(i, t, n):
    """print_speed(index, time, total_iteration)"""
    average_time = t / i
    remaining_time = (n - i) * average_time
    remaining_day = math.floor(remaining_time / 86400)
    remaining_hour = math.floor(remaining_time / 3600 - remaining_day * 24)
    remaining_min = round(remaining_time / 60 - remaining_day * 1440 - remaining_hour * 60)
    logging.info('%d / %d, speed: %.3f s/iter, ETA %d:%02d:%02d (D:H:M)\n' % (i, n, average_time, remaining_day, remaining_hour, remaining_min))
