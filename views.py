from django.shortcuts import render
from .models import Word
import random
import datetime

def word_of_the_day(request):
    words = Word.objects.all()
    if words:
        today = datetime.date.today()
        random.seed(today.year + today.month + today.day)
        random_word = random.choice(words)
    else:
        random_word = None
    
    return render(request, 'word_of_the_day/word_of_the_day.html', {'random_word': random_word})
