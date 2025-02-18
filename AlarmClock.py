import time

def set_alarm(hour, minute):
    alarm_time = f"{hour:02d}:{minute:02d}"
    current_time = time.strftime("%H:%M")

    while current_time != alarm_time:
        current_time = time.strftime("%H:%M")
        time.sleep(1)

    print("Alarm! Wake up!")

# Example usage
alarm_hour = int(input("Enter alarm hour (24-hour format): "))
alarm_minute = int(input("Enter alarm minute: "))
set_alarm(alarm_hour, alarm_minute)