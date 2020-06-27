from django.contrib.messages import success
from django.shortcuts import redirect, render

from flashcards.models import Flashcard

def home_page(request):
    return render(request, 'flashcards/home.html')

def create_card(request):
    Flashcard.objects.create(
        title=request.POST['title'],
        front_text=request.POST['front-text'],
        back_text=request.POST['back-text'],
    )
    message = 'Success! Your card, "{}", was submitted.'.format(
        request.POST['title']
    )
    success(request=request, message=message)
    return redirect('flash:home')