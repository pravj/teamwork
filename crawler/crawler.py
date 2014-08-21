import os
import sys
import json

try:
    import requests
except ImportError:
    raise Exception('unable to load requests module')


class Crawler:

    def __init__(self, org):
        self.org = org
        self.members = []

    # checks GitHub user type for 'Organization' or 'User' type
    #
    # return [boolean]
    def is_org(self):
        user_url = "https://api.github.com/users/%s" % (self.org)
        res = requests.get(user_url)

        if (res.status_code == requests.codes.ok):
            return (res.json()['type'] == u'Organization')
        else:
            print res.json()['message']
            sys.exit(0)

    # collects public members for a GitHub organization
    def collect_members(self, attempt=1):
        members_url = "https://api.github.com/orgs/%s/public_members?page=%d"\
            % (self.org, attempt)
        res = requests.get(members_url)

        if (len(res.json()) == 0):
            if (attempt == 1):
                print "no public members for organization '%s'" % (self.org)
                sys.exit(0)
            else:
                return self.members
        elif (res.status_code == requests.codes.ok):
            self.members = self.members + res.json()
            self.collect_members(attempt=attempt + 1)
        else:
            print res.json()['message']
            sys.exit(0)

    # saves members in 'members.json' inside 'data' directory
    def add_members(self):
        self.collect_members()
        members = []
        for member in self.members:
            members.append(member['login'])
        self.members = members

        path = os.path.join(os.path.dirname(__file__), '../raw/members.json')
        members_file = os.path.abspath(path)

        with open(members_file, 'w') as f:
            f.write(json.dumps(members))
            f.close()

    def collect_repos(self):
        repo_url = "https://api.github.com/orgs/%s/repos" % (self.org)
        try:
            repo_detail = requests.get(repo_url)
        except Exception, e:
            raise e

        if (repo_detail.status_code == requests.codes.ok):
            self.repos = repo_detail.text
        else:
            sys.exit(0)

    def add_repo_detail_in_file(self):
        self.collect_repos()

        path = os.path.join(os.path.dirname(__file__), '../raw/repo.json')
        repos_file = os.path.abspath(path)

        with open(repos_file, 'w') as f:
            f.write(self.repos.encode('utf-8'))
            f.close()
