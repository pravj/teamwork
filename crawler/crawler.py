import os
import sys
import json
import requests


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

    # saves members in 'members.json' inside 'raw/members.json'
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

    # collects general information about organization
    def collect_info(self):
        info_url = "https://api.github.com/users/%s" % (self.org)
        res = requests.get(info_url)

        info = {}

        if (res.status_code == requests.codes.ok):
            info['name'] = res.json()['name']
            info['avatar_url'] = res.json()['avatar_url']
            info['public_repos'] = res.json()['public_repos']
            info['blog'] = res.json()['blog']

            return info
        else:
            print res.json()['message']
            sys.exit(0)

    # saves organizatioin information inside 'raw/info.json'
    def add_info(self):
        info = self.collect_info()

        path = os.path.join(os.path.dirname(__file__), '../raw/info.json')
        info_file = os.path.abspath(path)

        with open(info_file, 'w') as f:
            f.write(json.dumps(info))
            f.close()
