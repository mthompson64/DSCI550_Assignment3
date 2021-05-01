import json
import pandas as pd
import re
import math


def get_days(dates):
    day_dict = {}
    
    for d in dates:

        if d in day_dict:
            day_dict[d] += 1
        else:
            day_dict[d] = 1
    
    return day_dict


# read in corpus
with open('fraudulent_emails_v3.json') as f:
    messages = json.load(f)

messages = messages['emails']

sent_dates = []
time_series = {}
times = []
for message in messages[1:]:
    # try statements for each of the from values containing sent timestamps

    try:
        date = message['MboxParser-from'].strip("  ").split(" ")[2]
        month = message['MboxParser-from'].strip("  ").split(" ")[3]
        if len(message['MboxParser-from'].strip("  ").split(" ")[4]) > 1:
            day = message['MboxParser-from'].strip("  ").split(" ")[4]
            time = message['MboxParser-from'].strip("  ").split(" ")[5]
            year = message['MboxParser-from'].strip("  ").split(" ")[6]
        else:
            day = message['MboxParser-from'].strip("  ").split(" ")[5]
            time = message['MboxParser-from'].strip("  ").split(" ")[6]
            year = message['MboxParser-from'].strip("  ").split(" ")[7]

        time = int(time.split(":")[0])
    
        sent_dates.append(date)
        times.append([date,time])
    
        if year in time_series.keys():
            time_series[year].append([month, day])
        else:
            time_series[year] = [month, day]
        
    except (IndexError,KeyError):
        date = None
        month = None
	
######
times_dict = {}

days = {"Mon":1, "Tue":2, "Wed":3, "Thu":4, "Fri":5, "Sat":6, "Sun":7}
for t in times:
    k = t[0] + " " + str(t[1])
    day = t[0]
    
    for key,value in days.items():
        if key == day:
            day_value = value
        else:
            continue
        
    if k in times_dict.keys():
        times_dict[k]['freq'] += 1
    else:
        times_dict[k] = {}
        times_dict[k]["freq"] = 1
        times_dict[k]["day"] = t[0]
        times_dict[k]["day_value"] = day_value
        times_dict[k]["time"] = t[1]

# dict to use for html
with open('final_day_hour.json', 'w') as text_out:
    json.dump(times_dict, text_out)

day_week = get_days(sent_dates)    # use function to get dictioary of day of weeks

df_day = pd.DataFrame.from_dict(day_week, orient= 'index', columns = ['Freq'])

# sort freq in desc order to get most frequent to least frequent
df_result = df_day.sort_values(['Freq'], ascending = False)

# assign score from 0-6 to each day of week
score = range(0, len(df_day['Freq']))

df_result['Score'] = score
df_result = df_result[0:7]


out_dict = df_result.to_dict('index')

with open('dates.json', 'w') as text_out:
    json.dump(out_dict, text_out)
