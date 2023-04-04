from tests.unit_tests.conftest import client, info_clubs, info_comp


class TestPurchasesPlace:

    def test_valid_points_should_book(self, client, info_clubs, info_comp):
        """
        GIVEN point valide du club pour reserver des places de compétition
        WHEN l'utilisateur entre des points valide
        THEN l'utilisateur reserves des places de compétition

        """
        club = info_clubs['name']
        comp = info_comp['name']
        places = "4"
        response = client.post('/purchasePlaces', data={'club': club, 'competition': comp, 'places': places})
        assert response.status_code == 200
        assert 'booking complete' in response.data.decode()

    def test_invalid_points_should_return_error_message_redirect_to_book_html(self, client, info_clubs, info_comp):
        """
        GIVEN point invalide redirection vers 'book.html'
        WHEN l'utilisateur entre des points invalide
        THEN l'utilisateur, est redirigé vers book.html

        """
        club = info_clubs['name']
        comp = info_comp['name']
        response = client.post('/purchasePlaces', data={'club': club, 'competition': comp, 'places': -1}, follow_redirects=True)
        assert response.status_code == 200
        error_message = "vous ne pouvez pas entrer un nombre négatif"
        assert error_message in response.data.decode()

    def test_shouldnt_book_when_0_points(self, client, info_clubs):
        email = info_clubs['email']
        #point = info_clubs['zeroPoint']
        response = client.post('/showSummary', data={"email": email})
        if info_clubs["points"] == 0:
            assert "vous n'avez plus de point pour faire des reservations!" in response.data.decode()
