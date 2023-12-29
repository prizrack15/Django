from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

dct = {
        'monday': 'в понедельник я жалею себя',
        'tuesday': 'во вторник - глазею в пропасть',
        'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
        'thursday': 'в четверг - зарядка',
        'friday': 'ужин с собой, нельзя снова его пропускать',
        'saturday': 'в субботу - борьба с презрением к себе',
        'sunday': 'в воскресенье - иду на рождество'
    }

def day_of_week(request, days: str):

    if days.lower() in dct:
        return HttpResponse(dct[days.lower()])
    return HttpResponse(f"Неизвестный день недели {days}")


def Glav_str_week_days(request):
    return HttpResponse('Дни недели')


def get_info_about_day_of_week(request, days: int):
    week = list(dct)
    if days > len(week):
        return HttpResponseNotFound(f"Неверный номер дня - {days}")
    else:
        name_week = week[days - 1]
        return HttpResponseRedirect(f'/week_days/{name_week}')
