from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406359853',
        'name': 'Helven Marcia',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)