from datetime import date
TODAY = date.today()


class Builder:

    def __init__(self):
        pass

    def build(self, org, member, end=None):
        start = "%s-%s-%s 00:00:00" % (TODAY.year, TODAY.month, TODAY.day)

        query = """SELECT payload_head, repository_name, repository_language,
        repository_size, repository_pushed_at FROM
        [githubarchive:github.timeline] WHERE type='PushEvent' AND
        repository_organization='%s' AND actor_attributes_login='%s' AND
        PARSE_UTC_USEC(created_at)>=PARSE_UTC_USEC('%s')
        """ % (org, member, start)

        if end is not None:
            query += """AND
            PARSE_UTC_USEC(created_at)<=PARSE_UTC_USEC('%s');""" % (end)
        else:
            query += ";"

        return query
