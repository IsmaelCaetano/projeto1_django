from django.shortcuts import render


# http request
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Ismael',
    })  # return http response
