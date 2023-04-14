from tests.conftest import info_comp, info_club


class TestShowSummary:

    club = info_club()[0]
    past_comp = info_comp()[0]

    def test_valid_email_should_return_welcome_page(self, client, captured_templates):
        """
        GIVEN email du club
        WHEN un mail valid est entrée
        THEN l'utilisateur accède avec succès à la page 'welcome.html'
        """
        valid_email = self.club["email"]
        response = client.post('/showSummary', data={'email': valid_email})
        assert response.status_code == 200
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "welcome.html"
        assert valid_email in response.data.decode()

    def test_invalid_email_should_return_index_html_with_errorMessage(self, client, captured_templates):
        """
        GIVEN email du club
        WHEN un mail invalid est entrée
        THEN l'utilisateur reçois un message d'erreur et reste sur la page 'index.htm'
        """
        invalid_email = 'wrong@email.com'
        response = client.post('/showSummary', data={'email': invalid_email}, follow_redirects=True)
        assert response.status_code == 200
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "index.html"
        assert 'error' in response.data.decode()