from termin import aachen_hbf_termin
import os
import datetime
audio = "/home/karnada/Downloads/Trash/mixkit-slot-machine-payout-alarm-1996.wav"
website = "https://termine.staedteregion-aachen.de/auslaenderamt/select2?md=1"
say = "new appointment avaialable."*15
while True:
    for team in ['Team 1', 'Team 2', 'Team 3']:
        is_available, res = aachen_hbf_termin(team)
        print(f"{team}: {res}")
        if is_available:
            # make an alarm sound
            print("Alarm!")
            print(res)
            # The res is of the format:
            # New appointments are available now at HBF Team 3!
            # Mittwoch, 25.09.2024
            # We need to extract the date and time from the string which is the 2nd line
            res = res.split('\n')[1]
            date_available = res.split(',')[1].strip()
            date_available = datetime.datetime.strptime(date_available, '%d.%m.%Y')
            # check that the date is earlier than 25.09.2024
            date_already_booked = datetime.datetime(2024, 8, 26)
            if date_available < date_already_booked:
                #os.system(f"xdg-open {audio}")
                os.system(f"spd-say {say}")
                os.system(f"xdg-open {website}")
                exit(0)
