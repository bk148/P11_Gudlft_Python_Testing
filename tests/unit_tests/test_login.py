from tests.unit_tests.conftest import client


class TestShowSummary:

    def test_valid_email_should_return_welcome_page(self, client):
        """
        GIVEN email du club
        WHEN un mail valid est entrée
        THEN l'utilisateur accède avec succès à la page 'welcome.html'
        """
        valid_email = 'john@simplylift.co'
        response = client.post('/showSummary', data={'email': valid_email})
        assert response.status_code == 200
        assert valid_email in response.data.decode()

    def test_invalid_email_should_return_index_html_with_errorMessage(self, client):
        """
        GIVEN email du club
        WHEN un mail invalid est entrée
        THEN l'utilisateur reçois un message d'erreur et reste sur la page 'index.htm'
        """
        invalid_email = 'errorgMail@club.com'
        response = client.post('/showSummary', data={"email": invalid_email})
        assert response.data.decode()
        assert 'message' in response.data.decode()