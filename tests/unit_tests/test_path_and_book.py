from tests.conftest import info_comp, info_club


class Test_Path_Booking:

    club = info_club()[0]
    comp = info_comp()[2]

    @staticmethod
    def assert_response(response, captured_templates):

        assert response.status_code == 200
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "welcome.html"
        assert "error" in response.data.decode()

    def test_valid_comp_valid_club_should_return_booking_page(self, client, captured_templates):
        """
        Données: données valides'
        Quand: nom club et comp sont valides
        Alors: l'utilisateur, est redirigé la page booking avec succès

        """
        response = client.get(f"/book/{self.comp['name']}/{self.club['name']}")
        assert response.status_code == 200
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "booking.html"
        assert f"Booking for {self.comp['name']}" in response.data.decode()

    def test_invalid_comp_invalid_club_should_return_summary_page_with_error(self, client, captured_templates):
        """
        GIVEN données club et comp '
        WHEN nom club et comp sont invalides
        THEN l'utilisateur, est redirigé la page Summary avec un message d'erreur

        """
        response = client.get('/book/invalid_comp/invalid_club')
        self.assert_response(response, captured_templates)
