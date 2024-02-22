hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

def calculate_end_time(hour, mins, dura):
    start_total_minutes = hour * 60 + mins
    end_total_minutes = start_total_minutes + dura

    end_hours = end_total_minutes // 60
    end_minutes = end_total_minutes % 60
    end_hours %= 24

    print(f"{end_hours:02d}:{end_minutes:02d}")
    
calculate_end_time(hour, mins, dura)
