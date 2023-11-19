# num_months = 12
# num_weeks = 4

# calendar = []
# for i in range(num_months):
#     month = []
#     for j in range(num_weeks):
#         week = []
#         month.append(week)
#     calendar.append(month)

# for month_idx, month in enumerate(calendar, start=1):
#     for week_idx, week in enumerate(month, start=1):
#         print(f"Month {month_idx}, Week {week_idx}: {week}")


month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
num_weeks = 4
calendar = {}

for month_idx, month_name in enumerate(month_names, start=1):
    calendar[month_name] = {f"Week {week_idx}": []
                            for week_idx in range(1, num_weeks + 1)}

calendar["July"]["Week 2"].append("Summer vacation")

event_description = calendar["July"]["Week 2"][0]
print(f"Event in the second week of July: {event_description}")
