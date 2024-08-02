from celery import shared_task

@shared_task
def add (x,y):
    return x + y

@shared_task(name="multiply_two_ints")
def mul (x,y):
    total = x ** y // 3
    return total

@shared_task(name="sum_list_of_numbers")
def sum_numbers(numbers):
    return sum(numbers)