from tests.conftest import info_club, info_comp



class Test_Booking:

    club = info_club()[0]
    comp = info_comp()[0]

    def test_should_login_and_purchase_competition_places(self, client):

        # LOGIN
        response = client.post('/showSummary', data={'email': self.club['email']}, follow_redirects=True)
        assert response.status_code == 200
        assert f"Welcome, {self.club['email']}" in response.data.decode()

        # purchasing
        response = client.post(
            '/purchasePlaces',
            data={
                'club': self.club['name'],
                'competition': self.comp['name'],
                'places': "10"
            },
            follow_redirects=True
        )
        assert response.status_code == 200
        assert "booking complete" in response.data.decode()
