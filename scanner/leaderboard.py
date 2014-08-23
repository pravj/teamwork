def repo_frequency(commit_data):
    counts = {}

    for commit in commit_data:
        repo = commit['repository_name']
        counts[repo] = counts.get(repo, 0) + 1

    frequency = []
    for k, v in frequency.iteritems():
        frequency.append({k: v})

    return frequency
