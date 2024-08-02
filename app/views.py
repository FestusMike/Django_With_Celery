from django.shortcuts import render
from app.tasks import add

result = add.delay(5,5)


