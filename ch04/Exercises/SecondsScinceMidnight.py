## The program takes inputs three integers for (hours, mins, seconds)
## and outputs the the Total Seconds passed from MIDNIGHT

def secondsSinceMidnight(h, m, s):
    hours_in_seconds = h * 60 * 60
    minutes_in_seconds = m * 60
    total_seconds = hours_in_seconds + minutes_in_seconds + s

    return (f'It is {total_seconds} seconds passed from MIDNIGHT.')

res = secondsSinceMidnight(13, 30, 45)
print(res)