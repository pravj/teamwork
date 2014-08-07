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
    def members(self):
        members_url = "https://api.github.com/orgs/%s/public_members"\
            % (self.org)
        res = requests.get(members_url)

        if (res.status_code == requests.codes.ok):
            self.add_members(res.json())
        else:
            print res.json()['message']
            sys.exit(0)

    # saves members in 'members.json' inside 'data' directory
    def add_members(self, response):
        members = []
        for member in response:
            members.append(member['login'])

        path = os.path.join(os.path.dirname(__file__), '../data/members.json')
        members_file = os.path.abspath(path)

        with open(members_file, 'w') as f:
            f.write(json.dumps(members))
            f.close()
