def add_time(start, duration, day_of_week=None):
    
    def switch_am_pm(ampm):
        return 'AM' if ampm == 'PM' else 'PM'

    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour + total_minutes // 60
    final_minutes = total_minutes % 60
    days_passed = total_hours // 24
    final_hour = total_hours % 24

    final_period = "AM" if final_hour < 12 else "PM"
    if final_hour == 0:
        final_hour = 12
    elif final_hour > 12:
        final_hour -= 12

    if day_of_week:
        day_of_week = day_of_week.capitalize()
        start_day_index = days_of_week.index(day_of_week)
        end_day_index = (start_day_index + days_passed) % 7
        result_day = days_of_week[end_day_index]
        day_str = f", {result_day}"
    else:
        day_str = ""

    if days_passed == 1:
        day_passed_str = " (next day)"
    elif days_passed > 1:
        day_passed_str = f" ({days_passed} days later)"
    else:
        day_passed_str = ""

    new_time = f"{final_hour}:{final_minutes:02d} {final_period}{day_str}{day_passed_str}"

    return new_time

print(add_time('3:30 PM', '2:12'))
print(add_time('11:55 AM', '3:12'))
print(add_time('2:59 AM', '24:00'))
print(add_time('11:59 PM', '24:05'))
print(add_time('8:16 PM', '466:02'))
print(add_time('3:30 PM', '2:12', 'Monday'))
print(add_time('2:59 AM', '24:00', 'saturDay'))
print(add_time('11:59 PM', '24:05', 'Wednesday'))
print(add_time('8:16 PM', '466:02', 'tuesday'))