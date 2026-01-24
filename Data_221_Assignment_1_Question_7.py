def convert_seconds_to_time_since_midnight(time: int):
    if not isinstance(time, int):
        print("Invalid input. Argument must be of type int")
        return None

    leftover_time = time
    time_in_pm = False
    hours_since_midnight = time // 3600
    leftover_time -= hours_since_midnight * 3600
    minutes_since_midnight = leftover_time // 60
    leftover_time -= minutes_since_midnight * 60
    seconds_since_midnight = leftover_time

    if hours_since_midnight > 24:
        print("Invalid input. Amount of seconds cannot be over a day")
        return None
    elif hours_since_midnight > 12:
        hours_since_midnight = hours_since_midnight - 12
        time_in_pm = True

    return f"{hours_since_midnight} {minutes_since_midnight} {seconds_since_midnight} {"pm" if time_in_pm else "am"}"

print(convert_seconds_to_time_since_midnight(50000))