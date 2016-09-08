from django.shortcuts import render

# Create your views here.
def startpage(request):
	return render(request, "quiz/startpage.html")

def quiz(request):
	return render(request, "quiz/quiz.html")

def question(request):
	return render(request, "quiz/question")

def completed(request):
	return render(request, "quiz/completed.html")