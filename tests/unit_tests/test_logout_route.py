from tests.unit_tests.conftest import client, app, captured_templates, info_club


def test_logout(client, captured_templates):
    """
    On se connecte, puis on se déconnecte et nous sommes sur la page d'index
    """
    club = info_club()[0]
    response = client.post('/showSummary', data={'email': club['email']})
    assert response.status_code == 200

    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200

    template, context = captured_templates[1]
    assert template.name == "index.html"
