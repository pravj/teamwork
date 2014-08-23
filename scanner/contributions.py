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


def contributions(time_series, start, reference='organization'):
    (time_data, commit_data) = commits_data(start)

    for i in range(len(time_series)):
        time_str = time_series[i]['repository_pushed_at'].split(" ")[0]
 
        index = time_data.index(time_str)
        commit_data[index] += 1

    contributions = []
    for i in range(366):
        contributions.append([time_data[i], commit_data[i]])

    total = len(time_series)

    return collect_data(total, contributions, streak(commit_data, time_data), reference)


def streak(commit_data, time_data):
    current, longest, temp_longest, index = 0, 0, 0, 0

    for k in range(366):
        if (commit_data[k] != 0):
            current += 1
            temp_longest += 1

        elif (commit_data[k] == 0 or k == 365):
            current = 0

            if (temp_longest > longest):
                longest = temp_longest
                index = k

            temp_longest = 0

    ranges = streak_range(current, longest, time_data, index)

    return (current, longest, ranges)


def streak_range(current, longest, time_data, index):
    current_range = longest_range = 'Rock - Hard Place'
    total_range = "%s - %s" % (time_data[0], time_data[365])

    if (current > 0):
        current_range = "%s - %s" % (time_data[366-current], time_data[365])
    if (longest > 0):
        longest_range = "%s - %s" % (time_data[index-longest], time_data[index])

    return (current_range, longest_range, total_range)


def collect_data(total, contributions, streak, refrence):
    result = {}

    result['reference'] = refrence
    result['total'] = total
    result['contributions'] = contributions
    result['current_streak'] = streak[0]
    result['longest_streak'] = streak[1]
    result['current_streak_range'] = streak[2][0]
    result['longest_streak_range'] = streak[2][1]
    result['total_streak_range'] = streak[2][2]

    return result
