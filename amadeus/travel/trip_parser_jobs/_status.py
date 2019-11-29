from amadeus.client.decorator import Decorator


class TripParserStatus(Decorator, object):
    def __init__(self, client, job_id):
        Decorator.__init__(self, client)
        self.job_id = job_id

    def get(self, **params):
        return self.client.get('/v2/travel/trip-parser-jobs/{0}'.format(self.job_id),  **params)