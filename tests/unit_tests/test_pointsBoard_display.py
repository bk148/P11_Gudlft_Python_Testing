from tests.conftest import info_club


def test_get_Board_page_should_display_board_html(client, captured_templates):
    response = client.get('/pointsBoard')
    assert response.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "board.html"


def test_correct_points_should_display_in_board_html(client):
    """
    Vérifier si les nombres de points corrects des clubs s'affichent correctement
    """
    club = info_club()[0]
    response = client.get('/pointsBoard')
    assert response.status_code == 200
    assert club['name'] in response.data.decode()
    assert club['points'] in response.data.decode()
