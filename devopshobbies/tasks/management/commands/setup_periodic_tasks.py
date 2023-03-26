from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.timezone import get_default_timezone_name

from django_celery_beat.models import IntervalSchedule, CrontabSchedule, PeriodicTask
from devopshobbies.users.tasks import profile_count_update as profile_update_task, hello2 as hello2_task


class Command(BaseCommand):
    help = """
    Setup celery beat periodic tasks.

    Following tasks will be created:

        - ....
    """

    @transaction.atomic
    def handle(self, *args, **kwargs):
        print('Deleting all periodic tasks and schedules...\n')

        IntervalSchedule.objects.all().delete()
        CrontabSchedule.objects.all().delete()
        PeriodicTask.objects.all().delete()

        """
        Example:
        {
            'task': periodic_task_name,
            'name': 'Periodic task description',
            # Everyday at 15:45
            # https://crontab.guru/#45_15_*_*_*
            'cron': {
                'minute': '45',
                'hour': '15',
                'day_of_week': '*',
                'day_of_month': '*',
                'month_of_year': '*',
            },
            'enabled': True
        },
        """
        periodic_tasks_data = [
        {
            'task': hello2_task,
            'name': 'Periodic task description',
            # EveryMinute to everyday
            # https://crontab.guru/#45_15_*_*_*
            'cron': {
                'minute': '*',
                'hour': '*',
                'day_of_week': '*',
                'day_of_month': '*',
                'month_of_year': '*',
            },
            'enabled': True
        },
        {
            'task': profile_update_task,
            'name': 'profile task description',
            # Everyday at 15:45
            # https://crontab.guru/#45_15_*_*_*
            'cron': {
                'minute': '45',
                'hour': '3',
                'day_of_week': '*',
                'day_of_month': '*',
                'month_of_year': '*',
            },
            'enabled': True
        },
 
                ]

        timezone = get_default_timezone_name()

        for periodic_task in periodic_tasks_data:
            print(f'Setting up {periodic_task["task"].name}')

            cron = CrontabSchedule.objects.create(
                timezone=timezone,
                **periodic_task['cron']
            )

            PeriodicTask.objects.create(
                name=periodic_task['name'],
                task=periodic_task['task'].name,
                crontab=cron,
                enabled=periodic_task['enabled']
            )
