class TestPurchasesPlace:

    @staticmethod
    def client_response(client, club, comp, points):
        return client.post(
            '/purchasePlaces',
            data={
                'club': club,
                'competition': comp,
                'places': points
            },
            follow_redirects=True
        )

    @staticmethod
    def assert_response(response, template_name, mess, captured_templates):
        assert response.status_code == 200
        template, context = captured_templates[0]
        assert template.name == template_name
        assert mess in response.data.decode()

    def test_valid_points_should_book(self, client, captured_templates):
        """
        Données entrées: point valide du club pour réserver des places de compétition
        Quand l'utilisateur entre des points valides
        Alors l'utilisateur reserves des places de compétition et reçoit un message de confirmation

        """
        response = self.client_response(client, "Simply Lift", "Spring Festival", "1")
        self.assert_response(response, "welcome.html", "booking complete", captured_templates)

    def test_invalid_points_valid_club_valid_comp_should_redirect_to_summary_page_with_error(self, client,
                                                                                             captured_templates):
        """
        Données entrées: point club valide, valide point comp, invalides places
        Quand l'utilisateur entre invalide point pour reserver
        Alors il reçoit un message d'erreur et est redirigé vers sur la page "summary"

        """
        places = ["0", "-1", "1000", "xxx"]

        for pl in places:
            response = self.client_response(client, "Simply Lift", "Spring Festival", pl)
            self.assert_response(response, "booking.html", "error", captured_templates)

    def test_valid_points_invalid_club_valid_comp_should_redirect_to_index(self, client, captured_templates):
        """
        Occurs only when user modify form / POST request through dev tools.
        POST Data:
        club: invalid
        comp: valid
        places: valid

        Should return:
        Index page with error message
        """
        response = self.client_response(client, "WrongClub", "Spring Festival", "1")
        self.assert_response(response, "index.html", "error", captured_templates)

    def test_valid_points_valid_club_invalid_comp_should_redirect_to_index(self, client, captured_templates):
        """
        Occurs only when user modify form / POST request through dev tools.
        POST Data:
        club: valid
        comp: invalid
        places: valid

        Should return:
        Index page with error message
        """
        response = self.client_response(client, "Simply Lift", "WrongComp", "1")
        self.assert_response(response, "index.html", "error", captured_templates)

    def test_valid_points_invalid_club_invalid_comp_should_redirect_to_index(self, client, captured_templates):
        """
        Occurs only when user modify form / POST request through dev tools.
        POST Data:
        club: invalid
        comp: invalid
        places: valid

        Should return:
        Index page with error message
        """
        response = self.client_response(client, "WrongClub", "WrongComp", "1")
        self.assert_response(response, "index.html", "error", captured_templates)

    def test_invalid_points_invalid_club_invalid_comp_should_redirect_to_index(self, client, captured_templates):
        """
        Occurs only when user modify form / POST request through dev tools.
        POST Data:
        club: invalid
        comp: invalid
        places: invalid

        Should return:
        Index page with error message
        """
        response = self.client_response(client, "InvalidClub", "InvalidComp", "a")
        self.assert_response(response, "index.html", "error", captured_templates)


