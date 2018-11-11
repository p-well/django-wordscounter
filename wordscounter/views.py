import re
from collections import Counter, OrderedDict

from django.http import HttpResponse  # Allows to return some information as Http response
from django.shortcuts import render


def render_home(request):
    return render(request, 'home.html', {'testing':'hola amigos!'})


def count_words(request):
    input_text = request.GET['fulltext'] #  объект fulltext прилетает из формы в темплите
    print(request.GET['most_common_words_qty'])
    print(type(request.GET['most_common_words_qty']))
    if len(request.GET['most_common_words_qty']) == 0:
        print('Gotcha!')
    common_words_to_show_qty = int(request.GET['most_common_words_qty'])
    stripped_text = re.sub(
        r'\d+',
        '',
        (re.sub(r'[^\w\s]','',input_text))
    )
    separated_words = re.findall(r'\w+', stripped_text)
    separated_lowered_words = [word.lower() for word in separated_words]
    words_data_list = (
        Counter(separated_lowered_words).most_common(common_words_to_show_qty))
    fulltext_words_qty = len(separated_words)  # punctuation already stripped
    words_data_dict = OrderedDict(words_data_list)
    context = {
        'original_text': input_text, #  в html-тепмлит передаётся весь контекст, а конкретный объект доступен в нём через ключ словаря
        'quantity': fulltext_words_qty, #  вот так: {{ quantity }}
        'words_data': words_data_dict.items(), #  {{ words_data }}
         }  # сам объект context самостоятельно в темплит явным образом не подружается - реализовано как-то под капотом джанго
    print(request)
    return render(request, 'count.html', context)


def render_about(request):
    return HttpResponse('This is about project page')
