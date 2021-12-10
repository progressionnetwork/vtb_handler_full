from celery import shared_task

from Config.celery import app as celery_app


@celery_app.task(name='api.tasks.example_task', queue='solo_task', routing_key='solo_task')
def example_task():
    pass


@shared_task(name='main.tasks.update_all_portfolios', queue='ml_task', routing_key='ml_task')
def example_shared_task():
    pass
