import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    'route_name',
    [
        'blog:index',
        'pages:about',
        'pages:rules',
    ]
)
def test_static_routes_are_available(client, route_name):
    response = client.get(reverse(route_name))
    assert response.status_code == 200


def test_post_detail_uses_post_id(client):
    response = client.get(reverse('blog:post_detail', args=[0]))
    assert response.status_code == 200
    assert 'РћСЃС‚СЂРѕРІ РѕС‚С‡Р°СЏРЅСЊСЏ' in response.content.decode()


def test_missing_post_returns_404(client):
    response = client.get(reverse('blog:post_detail', args=[10]))
    assert response.status_code == 404


def test_category_slug_is_rendered(client):
    response = client.get(reverse('blog:category_posts', args=['personal']))
    assert response.status_code == 200
    assert 'РџСѓР±Р»РёРєР°С†РёРё РІ РєР°С‚РµРіРѕСЂРёРё - personal' in response.content.decode()
