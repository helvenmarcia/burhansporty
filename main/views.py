from django.shortcuts import render

def show_main(request):
    context = {
        'app' : "BurhanSporty",
        'npm' : '2406359853',
        'name': 'Helven Marcia',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)