def convert_seconds_to_time_since_midnight(seconds_since_midnight: int):
    #Checking whether the argument of an integer
    if not isinstance(seconds_since_midnight, int):
        print("Invalid input. Argument must be of type int")
        return None

    leftover_time = seconds_since_midnight
    time_in_pm = False
    #An hour is 3600 seconds, so divide seconds by 3600 to get hours
    #All divisions made are through integer division as any remainders will be picked up by minutes/seconds
    hours_since_midnight = seconds_since_midnight // 3600
    leftover_time -= hours_since_midnight * 3600
    minutes_since_midnight = leftover_time // 60
    leftover_time -= minutes_since_midnight * 60

    if hours_since_midnight > 24:
        print("Invalid input. Amount of seconds cannot be over a day")
        return None
    elif hours_since_midnight > 12:
        #Converting from 24h clock to 12h clock
        hours_since_midnight = hours_since_midnight - 12
        time_in_pm = True

    #The leftover time is in seconds anyway, so it can be returned alongside everything else
    return f"{hours_since_midnight} {minutes_since_midnight} {leftover_time} {"pm" if time_in_pm else "am"}"

print(convert_seconds_to_time_since_midnight(50000))