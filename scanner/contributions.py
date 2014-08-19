import json
from datetime import date, timedelta
from time import mktime, gmtime, strftime, strptime


def commits_data(start):
    time_data, commit_data = [], []

    for i in range(366):
        _date = start + timedelta(days=i+1)
        _time = (_date.year, _date.month, _date.day, 0, 0, 0, 0, 0, 0)

        time_str = strftime("%Y-%m-%d", gmtime(mktime(_time)))

        time_data.append(time_str)
        commit_data.append(0)

    return (time_data, commit_data)


def contributions(time_series, start):
    (time_data, commit_data) = commits_data(start)

    for i in range(len(time_series)):
        time_str = time_series[i]['repository_pushed_at'].split(" ")[0]
        
        index = time_data.index(time_str)
        commit_data[index] += 1

    contributions = []

    for i in range(366):
        contributions.append([time_data[i], commit_data[i]])

    return contributions
