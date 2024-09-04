from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306207543',
        'name': 'Evelyn Depthios',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)