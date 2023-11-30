#This should be in a separate file called 'scripts.py'
import csv
from word_of_the_day.models import Word


def run():
    with open('Arabic.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        Word.objects.all().delete()

        for row in reader:
            print(row)

            words = Word(arabic_word=row[0], english_word=row[4])
            
            words.save()