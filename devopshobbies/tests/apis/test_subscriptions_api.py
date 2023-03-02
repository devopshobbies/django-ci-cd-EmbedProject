import pytest
from django.urls import reverse
from devopshobbies.users.models import BaseUser
from devopshobbies.blog.models import Post
import json


@pytest.mark.django_db
def test_empty_subs_api(api_client, user1, subscription1, profile1, post1):
    url_ = reverse("api:blog:subscribe")

    response = api_client.get(url_, content_type="application/json")
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data.get('results') == []
    assert data.get('limit') == 10 

