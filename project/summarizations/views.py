from django.shortcuts import render
from transformers import pipeline

# Create your views here.
def summary(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        max_l = request.POST.get('max_l')
        min_l = request.POST.get('min_l')

        #pipeline
        summarizer = pipeline("summarization")
        print(text)
        summary = summarizer(text, max_length=int(max_l), min_length=int(min_l), do_sample=False)[0]['summary_text']
        return render(request, 'summary.htm', {'summary': summary})


    return render(request, 'summary.htm', {})