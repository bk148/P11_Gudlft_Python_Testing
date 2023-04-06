from tests.unit_tests.conftest import client, info_clubs, test_past_comp


class TestShowSummary:

    def test_shouldnt_book_past_competition(self, client, info_clubs, test_past_comp):
        """
        Given: A secretary wishes to book a number of places for a competition
        When: They book a number of places on a competition that has happened in the past
        Then:  They should not be able to book a place on a post-dated competition
        (but past competitions should be visible).
        """

        response = client.post('/showSummary', data={'email': info_clubs['email']})
        assert response.status_code == 200
        assert test_past_comp['name'] in response.data.decode() and "Past competition" in response.data.decode()