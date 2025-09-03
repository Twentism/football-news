from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406365364',
        'name' : 'Melanton Gabriel Siregar',
        'class' : 'PBP KI'
    }

    return render(request, "main.html", context)