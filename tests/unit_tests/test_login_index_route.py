from tests.unit_tests.conftest import client, app, captured_templates


def test_login_index_route_return_index_page(client, captured_templates):
    """
    GET request to '/' should return index page.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "index.html"