from termin import aachen_hbf_termin, superc_termin
import os
import datetime
import subprocess as sb
audio = "/home/karnada/Downloads/Trash/mixkit-slot-machine-payout-alarm-1996.wav"
website = "https://termine.staedteregion-aachen.de/auslaenderamt/select2?md=1"
say = "new appointment avaialable."*5
date_already_booked = datetime.datetime(2026, 8, 26)
min_date = datetime.datetime(2025, 8, 1)


def extract_date_from_string(res_string: str) -> datetime.datetime:
    """Extracts the date from the appointment availability string."""
    # The res is of the format:
    # Service Name:
    # Day, DD.MM.YYYY
    # We need to extract the date from the string which is the 2nd line
    date_line = res_string.split('\n')[1]
    date_str = date_line.split(',')[1].strip()
    return datetime.datetime.strptime(date_str, '%d.%m.%Y')

def trigger_alarm():
    # Play an alarm sound
    # os.system(f"xdg-open {audio}")
    sb.run(["spd-say", say])
    os.system(f"xdg-open {website}")

# trigger_alarm()
while True:
    # Check for appointments in hbf
    # for team in ['Team 1', 'Team 2', 'Team 3']:
    #     is_available, res = aachen_hbf_termin(team)
    #     print(f"{team}: {res}")
    #     if is_available:
    #         # make an alarm sound
    #         print("Alarm!")
    #         print(res)
    #         date_available = extract_date_from_string(res)
    #         # check that the date is earlier than 25.09.2024
    #         if date_available > min_date and date_available < date_already_booked:
    #             trigger_alarm()
    #             exit(0)

    # Check for appointments in SuperC
    is_available, res = superc_termin(0)  # 0 for student
    if is_available:
        print("Alarm!")
        print(res)
        date_available = extract_date_from_string(res)
        if date_available > min_date and date_available < date_already_booked:
            trigger_alarm()
            exit(0)
