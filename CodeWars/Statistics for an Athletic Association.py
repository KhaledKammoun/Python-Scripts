import re
from datetime import time
def second_to_hour(total_seconds):
    hours, remainder = divmod(int(total_seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    microseconds = int((total_seconds - int(total_seconds)) * 1e6)
    return time(hours, minutes, seconds, microseconds)

def stat(strg):
    time_data = []
    result = re.split(r'[,\s]+', strg)
    for c in result :
        hours, minutes, seconds = map(int, c.split('|'))
        total_seconds = (hours * 3600) + (minutes * 60) + seconds
        time_data.append(total_seconds)
    
    if not time_data:
        return "00|00|00"
    
    sorted_time_data = sorted(time_data)

    len_time_data = len(time_data)
    Range = sorted_time_data[-1] - sorted_time_data[0]
    Mean = sum(time_data) / len_time_data



    if len(time_data)%2 == 0 :
        Median = (sorted_time_data[len_time_data//2] + sorted_time_data[(len_time_data - 1)//2]) / 2
    else :
        Median = sorted_time_data[len_time_data//2]

    Range_time = second_to_hour(Range)
    Mean_time = second_to_hour(Mean)
    Median_time = second_to_hour(Median)

    return "Range: {} Average: {} Median: {}".format(
        Range_time.strftime("%H|%M|%S"),
        Mean_time.strftime("%H|%M|%S"),
        Median_time.strftime("%H|%M|%S")
    )