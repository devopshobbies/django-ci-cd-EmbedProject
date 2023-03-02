import pytest
from devopshobbies.blog.selectors.posts import get_subscribers, post_list


@pytest.mark.django_db
def test_get_subscribers(user2, user1, subscription1, profile1, post1):
    a = get_subscribers(user = user1)
    assert a.count() == 0

@pytest.mark.django_db
def test_post_list(user2, user1, subscription1, profile1, post1):
    a = post_list(user = user1)
    assert a.first() == post1

