from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.htm')

def students(request):
    return render(request, 'student.htm')

def faculty(request):
    return render(request, 'faculty.htm')