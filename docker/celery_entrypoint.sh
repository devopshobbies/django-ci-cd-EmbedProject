echo "--> Starting celery process"
celery -A devopshobbies.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
