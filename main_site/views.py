from django.shortcuts import render
from django.utils import timezone

def homepage(request):
    return render(request, 'index.html',
                {
                "year": timezone.now().year,
                "month": timezone.now().strftime("%B"),  # Format month as full name (e.g., "March")
                },
            )


def web_projects(request):
    return render(request, 'web_projects.html')
