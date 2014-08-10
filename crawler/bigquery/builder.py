class Builder:

    def __init__(self):
        pass

    def build(self, org, member, start, end = None):
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

        print query
