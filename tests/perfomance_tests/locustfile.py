from locust import HttpUser, task, between
from tests.conftest import info_club, info_comp


class ProjectperfTest(HttpUser):

    wait_time = between(0, 1)
    club = info_club()[0]
    comp = info_comp()[2]

    def on_start(self):
        self.client.post('/showSummary', data={'email': self.club['email']})

    @task
    def home(self):
        self.client.get("/")

    @task(2)
    def booking(self):
        self.client.get("/book/%s/%s" % (self.competition['name'], self.club['name']))

    @task(2)
    def purchase(self):
        self.client.post('/purchasePlaces', data={'places': "3",
                                                  'club': self.club['name'],
                                                  'competition': self.competition['name']
                                                  }

                             )



