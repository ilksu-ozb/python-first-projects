import datetime, time, winsound
import sys

def set_timer():
    current = datetime.datetime.now() #hem tarih hem saat # %H -> Saat (00-23) # %M -> Dakika (00-59)
    print(f"It's {current.strftime('%H:%M')} right now.")

    while True:
        alarm = input("What time do you want to set an alarm for? (hh:mm) \n")
        parts = alarm.split(":")

        if len(parts) != 2 :
            print("Please check time format. (hh:mm)")
            continue
        

        try:
            if 0 <= int(parts[0]) <= 23 and 0 <= int(parts[1]) <= 59:
                print(f"Alarm set for {alarm}")
                break
            else:
                print("Invalid time! Hour must be 0-23, minute 0-59.")

        except ValueError, TypeError:
            sys.exit("Please enter valid numbers, not letters.")

    return int(parts[0]), int(parts[1])



def main():
    alarm_hour, alarm_minute = set_timer()
    while True:
        current = datetime.datetime.now()
        current_hour = current.hour
        current_minute = current.minute
        print("Waiting for alarm...")
        if alarm_hour == current_hour and alarm_minute == current_minute:
            print(f"It's {alarm_hour}:{alarm_minute}!!!")
            winsound.Beep(1000, 2000)
            break
        time.sleep(10)




if __name__ == "__main__":
    main()