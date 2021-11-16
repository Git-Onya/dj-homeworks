from django.http import request, HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}


def rec_calc(request, recipe_name):
    if recipe_name in DATA:
        servings = request.GET.get('servings')
        if servings:
            for ingredient, amount in DATA[recipe_name].items():
                DATA[recipe_name][ingredient] = amount * int(servings)
        context = {'recipe': DATA[recipe_name]}
        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse('Такого рецепта еще не знаю')
