from django.shortcuts import render

# Create your views here.
def ecdc(request):
    return render(request, 'encode_decode.htm',{})