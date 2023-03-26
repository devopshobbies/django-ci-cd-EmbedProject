import pytest
from devopshobbies.blog.services.post import create_post


@pytest.mark.django_db
def test_create_post(user2, user1, subscription1, profile1, post1):
    a = create_post(user = user1, title="pooo", content="CCCContent")

    assert a.author == user1
    assert a.title == "pooo"
    assert a.content == "CCCContent"

