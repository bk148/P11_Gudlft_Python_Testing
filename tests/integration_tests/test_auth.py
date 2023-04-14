from tests.conftest import info_club


class TestAuthentication:

    club = info_club()[0]

    def test_should_login(self, client):
        # ACCESS SUCCESS
        response = client.post('/showSummary', data={'email': self.club['email']}, follow_redirects=True)
        assert response.status_code == 200
        message = f"Welcome, {self.club['email']}"
        assert message in response.data.decode()

    def test_should_logout(self, client, captured_templates):
        response = client.post('/showSummary', data={'email': self.club['email']})
        assert response.status_code == 200
        response = client.get('/logout', follow_redirects=True)
        assert response.status_code == 200
        template, context = captured_templates[1]
        assert template.name == "index.html"

    def test_should_return_failed_login(self, client, captured_templates):
        invalid_email = 'wrong@mail.com'
        response = client.post('/showSummary', data={'email': invalid_email}, follow_redirects=True)
        assert response.status_code == 200
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "index.html"
        assert 'error' in response.data.decode()
