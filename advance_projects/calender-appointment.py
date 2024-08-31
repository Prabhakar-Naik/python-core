import calendar
import datetime

class Test:
    def __init__(self):
        # Dictionary to store booked slots with date as key and a list of booked times as value
        self.booked_slots = {}

    def slot_booking(self, date, time):
        """
        Books a slot for a given date and time.
        """
        if date in self.booked_slots:
            if time in self.booked_slots[date]:
                print(f"Slot on {date} at {time} is already booked.")
            else:
                self.booked_slots[date].append(time)
                print(f"Slot on {date} at {time} has been booked.")
        else:
            self.booked_slots[date] = [time]
            print(f"Slot on {date} at {time} has been booked.")

    def display_slot(self, date, time):
        """
        Displays whether a slot on a given date and time is booked.
        """
        if date in self.booked_slots and time in self.booked_slots[date]:
            print(f"Slot on {date} at {time} is booked.")
        else:
            print(f"Slot on {date} at {time} is available.")

    def display_slot_by_date(self, date):
        """
        Displays all booked slots for a given date.
        """
        if date in self.booked_slots:
            print(f"Booked slots on {date}: {', '.join(self.booked_slots[date])}")
        else:
            print(f"No slots booked on {date}.")

    def display_slot_by_month(self, month):
        """
        Displays all booked slots for a given month.
        """
        booked_in_month = {}
        for date, times in self.booked_slots.items():
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
            if date_obj.month == month:
                booked_in_month[date] = times

        if booked_in_month:
            for date, times in booked_in_month.items():
                print(f"Booked slots on {date}: {', '.join(times)}")
        else:
            print(f"No slots booked in month {calendar.month_name[month]}.")

    def display_slot_by_day(self, day):
        """
        Displays all booked slots for a specific day of the week (e.g., Monday).
        """
        day_name = day.capitalize()
        booked_on_day = {}
        for date, times in self.booked_slots.items():
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
            if calendar.day_name[date_obj.weekday()] == day_name:
                booked_on_day[date] = times

        if booked_on_day:
            for date, times in booked_on_day.items():
                print(f"Booked slots on {date} ({day_name}): {', '.join(times)}")
        else:
            print(f"No slots booked on {day_name}.")

    def display_slot_by_week(self, week):
        """
        Displays all booked slots for a given week of the year.
        """
        booked_in_week = {}
        for date, times in self.booked_slots.items():
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
            if date_obj.isocalendar()[1] == week:
                booked_in_week[date] = times

        if booked_in_week:
            for date, times in booked_in_week.items():
                print(f"Booked slots in week {week} on {date}: {', '.join(times)}")
        else:
            print(f"No slots booked in week {week}.")

Test = Test()

# Example usage
Test.slot_booking("2023-05-01", "10:00")
Test.slot_booking("2023-05-01", "11:00")
Test.slot_booking("2023-05-01", "11:00")