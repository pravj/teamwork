import requests


class Crawler:
    def __init__(self, org):
        self.org = org

    def isOrg(self):
        url = "https://api.github.com/users/%s" % (self.org)
        res = requests.get(url)

        if (res.json()['type'] == u'Organization'):
	    return True
	else:
	    return False
