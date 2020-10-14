
class OnlineshopFunction:
    def __init__(self, details):
        self.administrative = details['administrative']  # {'administrative': 0}['administrative'] = 0
        self.administrative_duration = details['administrative_duration']  # {'administrative_duration': 0}['administrative_duration'] = 0
        self.informational = details['informational']
        self.informational_duration = details['informational_duration']
        self.productrelated = details['productrelated']
        self.productrelated_duration = details['productrelated_duration']
        self.bouncesrates = details['bouncerates']
        self.exitrates = details['exitrates']
        self.pagevalues = details['pagevalues']
        self.specialday = details['specialday']
        self.month = details['month']
        self.operatingsystems = details['operatingsystems']
        self.browser = details['browser']
        self.region = details['region']
        self.traffictype = details['traffictype']
        self.visitortype = details['visitortype']
        self.weekend = details['weekend']
        self.revenue = details['revenue']