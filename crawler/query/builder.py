from datetime import date, timedelta
PAST = (date.today() - timedelta(days=365))


class Builder:

    def __init__(self, org):
        self.org = org

    def start(self):
        return "%s-%s-%s 00:00:00" % (PAST.year, PAST.month, PAST.day)

    def build(self, end=None):
        query = """SELECT payload_head, repository_name, repository_language,
        repository_size, repository_pushed_at, actor_attributes_login as user,
        repository_private as is_member
        FROM [githubarchive:github.timeline] WHERE type='PushEvent' AND
        repository_organization='%s' AND
        PARSE_UTC_USEC(created_at)>=PARSE_UTC_USEC('%s')
        ORDER BY repository_pushed_at ASC
        """ % (self.org, self.start())

        if end is not None:
            query += """AND
            PARSE_UTC_USEC(created_at)<=PARSE_UTC_USEC('%s');""" % (end)
        else:
            query += ";"

        return query
