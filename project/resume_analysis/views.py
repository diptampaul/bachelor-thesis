from django.shortcuts import render
from .models import ResumeAnalysis
from .utils import traindata


# Create your views here.
def resume(request):
    if request.method == 'POST':
        up_resume = request.FILES.get('resume', False)
        resume_obj = ResumeAnalysis(
            uploaded_file = up_resume
        )
        resume_obj.save()
        path = f'media/{resume_obj.uploaded_file}'
        label, value = traindata(path)
        resume = {}
        for i in range(len(label)):
            resume[label[i]] = value[i]
        print(resume)
        return render(request, 'resume.htm', {'resume': resume, 'value': value})

    return render(request, 'resume.htm')