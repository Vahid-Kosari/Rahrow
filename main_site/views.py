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
    return render(request, 'web_projects.html',
                  {
                      "title": "Web Developer",
                      "year": timezone.now().year,
                  })


def eng_projects(request):
    return render(request, 'eng_projects.html',
                  {
                      "title": "Mechanical Engineer",
                      "year": timezone.now().year,
                  })
