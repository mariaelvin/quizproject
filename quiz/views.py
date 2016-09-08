from django.shortcuts import render

quizzes = [
	{
		"quiz_number": 1,
   		"name": "Klassiska böcker",
	   	"description": "Hur bra kan du dina klassiker?"
	},
	{
		"quiz_number": 2,
   	   	"name": "Största fotbollslagen",
	   	"description": "Kan du dina lag?"
	},
	{
		"quiz_number": 3,
   	    	"name": "Världens mest kända hackare",
	    	"description": "Hackerhistoria är viktigt, kan du den?"	},
]

# Create your views here.
def startpage(request):
	context = {
	"quizzes":quizzes,
	}
	return render(request, "quiz/startpage.html", context)

def quiz(request,quiz_number):
	context = {
	"quiz": quizzes[int(quiz_number)-1],
	"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
	"question_number": question_number,
	"question": "Hur många bultar har ölandsbron",
	"answer1": "12",
	"answer2": "66 400",
	"answer3": "7 428 954",
	"quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)

def completed(request):
	return render(request, "quiz/completed.html")