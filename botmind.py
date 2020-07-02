from random import choice
from datetime import datetime

def chat_reply(word_dict, user_input):
	if user_input in word_dict:
		i = word_dict[user_input]
		return choice(i)
	else:
		clog = open("careerbot.txt","a+")
		now= datetime.now()
		dt_str = now.strftime("%d/%m/%Y %H:%M:%S")
		logdata = "{ date and time :" + dt_str + " \n  log = [ " + user_input + " ] } \n"
		clog.write(logdata)

		clog.close()

		return "Sorry, I don't know about that! I will research about that \n You can call 9737571943 or 8320731105 for more details"

word_dict = {
	"hello":["Hey there!", "Hello", "Hii!"],
	"10": ["You Can study these courses: \n        Study for HSC science A Group \n        Study for HSC Science B Group \n        Study for HSC Arts \n        Study for HSC Commerce \n        Diploma Polytechnic \n        I.T.I. \n        Other(private) \n        Which will You like to do? Please type specific sentence!"],
	"10 pass": ["You Can study these courses: \n        Study for HSC science A Group \n        Study for HSC Science B Group \n        Study for HSC Arts \n        Study for HSC Commerce \n        Diploma Polytechnic \n        I.T.I. \n        Other(private) \n        Which will You like to do? Please type specific sentence!"],
	"10th pass": ["You Can study these courses: \n        Study for HSC science A Group \n        Study for HSC Science B Group \n        Study for HSC Arts \n        Study for HSC Commerce \n        Diploma Polytechnic \n        I.T.I. \n        Other(private) \n        Which will You like to do? Please type specific sentence!"],

	"study for hsc":["Which Stream You like to go? \n        Study Science A group \n        Study Science B group \n        Study Arts \n        Study Commerce \n        Please Type as above(include the word: study)"],
	"study for h.s.c.":["Which Stream You like to go? \n        Study Science A group \n        Study Science B group \n        Study Arts \n        Study Commerce \n        Please Type as above(include the word: study)"],
	"study for class 12":["Which Stream You like to go? \n        Study Science A group \n        Study Science B group \n        Study Arts \n        Study Commerce \n        Please Type as above(include the word: study)"],
	"i want to study class 12":["Which Stream You like to go? \n        Study Science A group \n        Study Science B group \n        Study Arts \n        Study Commerce \n        Please Type as above(include the word: study)"],

	"study for hsc science a group": ["This is a Good choice! \n You can also prepare for JEE/BITSAT/KVPY"],
	"study for h.s.c. science a group": ["This is a Good choice! \n You can also prepare for JEE/BITSAT/KVPY"],
	"study hsc science a group": ["This is a Good choice! \n You can also prepare for JEE/BITSAT/KVPY"],
	"study science a group": ["This is a Good choice! \n You can also prepare for JEE/BITSAT/KVPY"],
	"i want to study science a group": ["This is a Good choice! \n You can also prepare for JEE/BITSAT/KVPY"],
	"i want to study hsc science a group": ["This is a Good choice! \n You can also prepare for JEE/BITSAT/KVPY"],
	"i want to study h.s.c. science a group": ["This is a Good choice! \n You can also prepare for JEE/BITSAT/KVPY"],

	"study for hsc science b group":["Good Idea! You can be Doctor in future. \n You must prepare for NEET"],
	"study science b group":["Good Idea! You can be Doctor in future. \n You must prepare for NEET"],
	"i want to study science b group":["Good Idea! You can be Doctor in future. \n You must prepare for NEET"],
	

	"other":["These courses are private courses governed by private Institutes/Universities \n This is the list of private courses \n      Interior Design \n      Web Design \n      Cyber security \n      Graphics \n      Animation \n      Health Inspector \n      Sanitary Inspector \n      You can call on +910000000000 for more information!"],

	"12": ["Which Stream? \n        Arts \n        Commerce \n        Science \n"],
	"12 pass": ["Which Stream? \n        Arts \n        Commerce \n        Science \n"],
	"12th pass":["Which Stream? \n        Arts \n        Commerce \n        Science \n"],

}
