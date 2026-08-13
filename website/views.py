from django.shortcuts import render

def home(request):
    institution_info = {
        "name": "Datatec Skill Academy",
        "tagline": "Empowering Future Innovators",
        "announcements": [
            "Admissions Open for Academic Year 2026–2027",
            "Annual Tech Symposium scheduled for October 15th",
            "New AI & Data Science lab inaugurated"
        ]
    }
    return render(request, 'index.html', {'info': institution_info})
