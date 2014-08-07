import sys

try:
    import requests
except ImportError:
    raise Exception('unable to load requests module')


class Crawler:

    def __init__(self, org):
        self.org = org

    def isOrg(self):
        url = "https://api.github.com/users/%s" % (self.org)
        res = requests.get(url)

        if (res.status_code == 200):
            return (res.json()['type'] == u'Organization')
        else:
            print res.json()['message']
            sys.exit(0)
