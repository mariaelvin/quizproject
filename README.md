# quizproject
Det här är mitt quiz som jag byggde på #100Tjejerkodar i Barcelona 2016.

Mimsen is on a roll!

----
Tutorial: Torsdag: Django

Dags att jobba!
Uppgiften är att ta de fyra sidor ni gjorde i tisdags, och bygga en 
Django-sajt av dem
#1 *Skapa ett nytt repository som heter quizproject
Börja med att göra ett nytt repository på Github. Lättast är att göra det på webbplatsen, och sedan kör clone till en egen mapp precis som förut.
Github.com -> Skapa ett repo med plustecknet längst upp till höger
Hitta på ett namn, välj att du vill ha en README och se till att du får med .gitignore för python!
Starta sedan Github-programmet, och välj plustecknet uppe till vänster
Välj clone, välj ditt repo, och välj var på hårddisken du vill lägga filerna
#2 *Skapa ett projekt*
Starta en terminal
Gå till mappen som du nyss checkade ut från Github
Installera Django: pip3 install django
Skapa ett projekt: django-admin startproject quizsite . (missa inte punkten efteråt!)
#3 *Se till att databasen skapas som den ska* (vi ska prata mer i detalj hur detta fungerar senare)
python3 manage.py migrate
Vi vill inte checka in databasen till Github, då skulle ju alla våra testgrejer komma med. Därför vill vi se till att den ignoreras:
Starta Github-programmet och gå in på quizsite-projektet
I listan på filer som har ändrats finns db.sqlite3 i listan
Högerklicka (klicka med två fingrar på Mac) på den filen och välj ignore
"db.sqlite3" läggs nu till i en fil som heter .gitignore. Det innebär att Git helt kommer att ignorera alla ändringar i databasen, så vi kan ha en helt egen testdatabas på vår egen dator jämfört med den vi använder när vi sen går live.
#4 *Starta utvecklingsservern*
python3 manage.py runserver
Öppna din webbläsare och surfa till http://127.0.0.1:8000
Det går också bra att surfa till "localhost:8000" om du tycker det är lättare att komma ihåg
Ska visa: "It worked!"
Om du vill stänga servern igen kan du trycka "Ctrl+C", annars kan du öppna en ny flik eller fönster och ha den körande där medan du testar
#5 *Commit:a koden du har hittills till Github*
I Github-programmet, se till att alla filer är markerade i mittenkolumnen
Skriv en sammanfattning på det du skickar in, t.ex. "Generated a new Django project" eller liknande
Klicka på "Commit"-knappen
Klicka på "Sync" längst upp till höger i programmet för att skicka allt till Github
Kontrollera att allt fungerade genom att titta på ditt projekt på http://github.com
Från och med nu vill jag att du gör commit efter varje steg i listan nedan! Det gör att du får en logg och enkelt kan gå tillbaka om något går fel.
#6 *Skapa en Django-app*
python3 manage.py startapp quiz
Öppna Sublime Text och välj quizproject-mappen som du clonade från Github. Du ser nu alla filer i projektet till vänster i Sublime.
Lägg till namnet på den app du just skapade i quizproject/quizsite/settings.py under INSTALLED_APPS
"quiz" <- lägg till längst ner i listan
#7 *Vi ska nu kopiera in HTML-sidorna som du gjorde tidigare till detta projekt och bygga vidare på dem*
Skapa en ny mapp som heter "templates" i quizproject/quiz
Skapa en ny mapp som heter "quiz" i quizproject/quiz/templates
Lägg in dina fyra templates där
#8 *Lägg in dina CSS-filer (inklusive bootstrap) och bilder*
Skapa en ny mapp direkt under quizproject som du kallar "static"
Lägg din CSS-fil och bilder i den mappen
För att Django ska hitta din mapp behöver du också göra en ändring i quizproject/quizsite/settings.py, lägg till:
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, "static"),
)
Ändra sökvägen till din CSS i alla fyra HTML-filer, sökvägen ska nu se ut såhär:
 	<link rel="stylesheet" href="/static/style.css">
	(Om du har kallat din CSS-fil något annat, skriv det namnet istället, t.ex. /static/testsida.css)
Flytta också in dina tre bootstrap-mappar: css, fonts, och js till static-mappen.
Ändra sökvägen till bootstrap.min.css så att den ser ut såhär:
<link rel="stylesheet" href="/static/css/bootstrap.min.css">
Ändra sökvägen till dina bilder så att dom börjar med /static/, t.ex. /static/bild.jpg - Slashtecknet i börjar är viktigt!
*Du har väl inte glömt att commit:a mellan varje steg?
#9 *Skapa fyra vyer i quiz/views.py*
from django.shortcuts import render
def startpage(request):
return render(request, "quiz/startpage.html")
def quiz(request):
return render(request, "quiz/quiz.html")
def question(request):
return render(request, "quiz/question.html")
def completed(request):
return render(request, "quiz/completed.html")
Ändra namnen på html-filerna så att dom matchar de namn du har på dina filer!
#10 *Skapa URL:er i quizproject/quizsite/urls.py och koppla till vyerna*
Ta bort allt som finns i urls.py och ersätt det med:
from django.conf.urls import url
from quiz import views
urlpatterns = [
	url(r"^$", views.startpage),
	url(r"^quiz/[0-9]+/$", views.quiz),
	url(r"^quiz/[0-9]+/question/[0-9]+/$", views.question),
	url(r"^quiz/[0-9]+/completed/$", views.completed),
]
#11 *Starta utvecklingsservern och testa det du gjort hittills*
python3 manage.py runserver
http://127.0.0.1:8000/
http://127.0.0.1:8000/quiz/1/
http://127.0.0.1:8000/quiz/1/question/1/
http://127.0.0.1:8000/quiz/1/completed/
Fungerar alla fyra sidor som du har gjort? Kan man surfa till dem nu?
*Du har väl inte glömt att commit:a mellan varje steg?
#12 *Lägg in lite testdata som vi kan använda tills vi har lagt till en databas*
Direkt under import-raderna, men innan dina fyra vyer, i views.py lägg in detta:
quizzes = [
	{
		"quiz_number": 1,
   		"name": "Klassiska böcker",
	   	"description": "Hur bra kan du dina klassiker?"
	},
	{
		"quiz_number": 2,
   	   	"name": "Största 1slagen",
	   	"description": "Kan du dina lag?"
	},
	{
		"quiz_number": 3,
   	    	"name": "Världens mest kända hackare",
	    	"description": "Hackerhistoria är viktigt, kan du den?"	},
]
#13 *Gör så att startsidan använder datan*
Ändra definitionen av startpage i quizproject/quiz/views.py
def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/startpage.html", context)
*Se till att den nya datan används i quizproject/quiz/templates/quiz/startpage.html*
Lägg in följande inne i <body>-taggen där du vill ha din lista med quizzes:
{% for quiz in quizzes %}
	<p>{{ quiz.name }}</p>
{% endfor %}
Testa att allt fungerar genom att gå till http://127.0.0.1:8000/ (om det inte fungerar försök komma på varför genom att titta på felmeddelandet)
#14 *Gör så att quizsidan använder datan*
Ändra definitionen av quiz i quiz/views.py
def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[int(quiz_number) - 1],
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)
(quizzes[int(quiz_number) - 1] eftersom: quizzes är en lista, och om man hämtar ut quiz_number=1 så vill man förmodligen ha den första i listan, dvs den på position 0)
I quiz kommer "quiz_number" med som parameter, för att det ska fungera behöver du ändra i quizsite/urls.py så att det skickas med från URL:en. Detta görs genom att du sätter en parentes runt det som ska skickas med, ändra till:
url(r"^quiz/([0-9]+)/$", views.quiz), <- Notera parentesen!
Se till att datan används i quizproject/quiz/templates/quiz/quiz.html Lägg in följande inne i <body>-taggen där du vill ha din rubrik och beskrivning:
	<h1>{{ quiz.name }}</h1>
	<p>{{ quiz.description }}</p>
Testa att allt fungerar genom att gå till http://127.0.0.1:8000/quiz/1/ i webbläsaren (om det inte fungerar försök komma på varför genom att titta på felmeddelandet)
*Du har väl inte glömt att commit:a mellan varje steg?
#15 *Lägg till lite data på frågesidan*
Vi kommer skriva riktiga frågor imorgon, men för att ha något att jobba med, ändra definitionen av question i quiz/views.py till:
def question(request, quiz_number, question_number):
	context = {
		"question_number": question_number,
	    	"question": "Hur många bultar har ölandsbron?",
		"answer1": "12",
	   	"answer2": "66 400",
	    	"answer3": "7 428 954",
	    	"quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)
I question kommer "quiz_number" och "question_number" med som parametrar, för att det ska fungera behöver du ändra i quizsite/urls.py så att de skickas med från URL:en. Detta görs genom att du sätter två parenteser runt det som ska skickas med, ändra till:
url(r"^quiz/([0-9]+)/question/([0-9]+)/$", views.question) 
Notera de två extra parenteserna
Se till att datan används i quiz/templates/quiz/question.html. Lägg in följande inne i <body>-taggen där du vill ha din rubrik och beskrivning:
	<h1>{{ question_number }}. {{ question }}</h1>
	<p>{{ answer1 }}</p>
	<p>{{ answer2 }}</p>
	<p>{{ answer3 }}</p>
Testa att allt fungerar genom att gå till http://127.0.0.1:8000/quiz/1/question/1/ (om det inte fungerar försök komma på varför genom att titta på felmeddelandet)
#16 *Lägg nu in lite data på completed-sidan*
Ändra definitionen av completed i quizproject/quiz/views.py till:
def completed(request, quiz_number):
	context = {
	    	"correct": 12,
	    	"total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/completed.html", context)
I completed kommer "quiz_number" med som parameter, för att det ska fungera behöver du ändra i quizproject/quizsite/urls.py så att det skickas med från URL:en. Detta görs genom att du sätter en parentes runt det som ska skickas med, ändra till:
url(r"^quiz/([0-9]+)/completed/$", views.completed)
Se till att datan används i quizproject/quiz/templates/quiz/completed.html. Lägg in följande inne i <body>-taggen där du vill ha din rubrik och beskrivning:
	<h1>Du är klar och fick {{ correct }} av {{ total }}</h1>
Testa att allt fungerar genom att gå till http://127.0.0.1:8000/quiz/1/completed/ i webbläsaren (om det inte fungerar försök komma på varför genom att titta på felmeddelandet)
*Du har väl inte glömt att commit:a mellan varje steg?
#17 Vi ska nu se till att den går att gå från den ena sidan till nästa genom att klicka på länkar istället för att skriva i adressfältet:
Namnge alla URL:er i urls.py enligt följande:
url(r"^$", views.startpage, name="start_page")
url(r"^quiz/([0-9]+)/$", views.quiz, name="quiz_page")
...
Gör samma sak för "question_page" och "completed_page" i urls.py
Django kan nu skapa länkar till olika delar av sajten
Ändra quizproject/quiz/templates/quiz/startpage.html så att du länkar till varje quiz:
{% for quiz in quizzes %}
    <p><a href="{% url 'quiz_page' quiz.quiz_number %}">
        {{ quiz.name }}
    </a></p>
{% endfor %}
Testa att det fungerar genom att gå till startsidan i webbläsaren och klicka på alla tre quizzes
Ändra quizproject/quiz/templates/quiz/quiz.html så att en länk längst ner går till att starta frågesporten:
<p><a href="{% url 'question_page' quiz_number 1 %}">Starta</a></p>
Ändra quiz/templates/quiz/question.html så att det finns en länk längst ner till completed-sidan:
<p><a href="{% url 'completed_page' quiz_number %}">Nästa</a></p>
Ändra quizproject/quiz/templates/quiz/completed.html så att det finns en länk längst ner till startsidan:
<p><a href="{% url 'start_page' %}">Till startsidan</a></p>
Gör en commit och klicka Sync så att allt skickas till Github.
#18 Klicka igenom din sajt och se till att alla länkar fungerar!

Sjukt bra jobbat!
