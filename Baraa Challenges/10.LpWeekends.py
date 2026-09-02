days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
weekend = ['sat', 'sun']
for day in days:
    if day in  weekend:
        continue
    print('Days:- ', day)