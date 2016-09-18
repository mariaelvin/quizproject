from django.shortcuts import redirect
from django.shortcuts import render
from quiz.models import Quiz

# Create your views here.
def startpage(request):
	context = {
	"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/startpage.html", context)

def quiz(request,quiz_number):
	context = {
	"quiz": Quiz.objects.get(quiz_number=quiz_number),
	"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, quiz_number, question_number):
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	questions = quiz.questions.all()
	question = questions[int(question_number) - 1]
	context = {
	"question_number": question_number,
	"question": question.question,
	"answer1": question.answer1,
	"answer2": question.answer2,
	"answer3": question.answer3,
	"quiz": quiz,
	"quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)

def question_answer(request, quiz_number, question_number):
	saved_answers = request.session.get(quiz_number,{})
	answer = int(request.POST["answer"])
	saved_answers[question_number] = answer
	request.session[quiz_number] = saved_answers

	answer = int(request.POST["answer"])
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	questions = quiz.questions.all()
	question = questions[int(question_number)-1]
	correct_answer = question.correct
	if correct_answer==1:
		answer_=question.answer1
	elif correct_answer==2:
		answer_=question.answer2
	elif correct_answer==3:
		answer_=question.answer3

	if correct_answer==answer:
		context={
		"question": question.question,
		"answer1": question.answer1,
		"answer2": question.answer2,
		"answer3": question.answer3,
		"answertext":"Helt rätt!", 
		"answer":answer_,
		"quiz":quiz,
		"question_number":question_number,
		 }
		return render(request,"quiz/question_answer.html", context)
	else:
		context={
		"question": question.question,
		"answer1": question.answer1,
		"answer2": question.answer2,
		"answer3": question.answer3,
		"answertext":"Tyvärr, det var fel.",
		"answer":answer_,
		"quiz":quiz,
		"question_number":question_number,}
		return render(request,"quiz/question_answer.html", context)

def answer(request, quiz_number,question_number):
	question_number = int(question_number)
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	num_questions = quiz.questions.count()
	if num_questions <= question_number:
		return redirect("completed_page", quiz_number)
	else:
		return redirect("question_page", quiz_number, question_number + 1)

def completed(request, quiz_number):
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	questions = quiz.questions.all()
	saved_answers = request.session.get(quiz_number, {})
	num_correct_answers = 0
	for question_number, answer in saved_answers.items():
		correct_answer = questions[int(question_number) - 1].correct
		if correct_answer == answer:
			num_correct_answers += 1
	context = {
	"correct": num_correct_answers,
	"total": questions.count(),
	}
	return render(request, "quiz/completed.html", context)