from celery import shared_task
from .services import profile_count_update as update_profile_count


@shared_task
def profile_count_update():
    update_profile_count()

@shared_task
def hello2():
    print("HIIIIIII")
