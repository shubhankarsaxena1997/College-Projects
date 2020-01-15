from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from onlinequiz.models import Questions
# Create your views here.

def index(request):
	return render(request,'index.html')

def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('dashboard')
		else:
		 	messages.warning(request,"Username or Password is Incorrect")
		 	return redirect('login')

	return render(request,'login.html')

def register(request):
	if request.method=="POST":

		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		email=request.POST['email']
		password1=request.POST['pswd1']
		password2=request.POST['pswd2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.error(request,'Username Taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.error(request,'Email Already Exists')
				return redirect('register')
			else:								
				user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
				user.save();
				messages.error(request,'Acccount Created Successfully')
				return redirect('login')
		else:
			messages.error(request,'Password and Confirm-Password Not Matching')
			return redirect('register')		

	else:
		return render(request,'register.html')		

def dashboard(request):
	if request.session._session:
		return render(request,'dashboard.html')
	else:
		return render(request,'login.html')	

def logout(request):
	auth.logout(request)
	return redirect('login')		

def menu(request):
		return render(request,'menu.html')	

def manage_users(request):
	if request.session._session:
		users_data=User.objects.all()
		return render(request,'manage_users.html',{'users':users_data})
	else:
		return render(request,'login.html')	

def manage_questions(request):
	if request.session._session:
		a=Questions.objects.all()		
		return render(request,'manage_questions.html',{'questions':a})
	else:
		return render(request,'login.html')		

def change_password(request):
	if request.method=='POST':
		form=PasswordChangeForm(request.user,request.POST)
		if form.is_valid():
			user=form.save()
			update_session_auth_hash(request,user)
			messages.success(request,'Your Password was Successfully changed')
			return redirect('login')
		else:
			messages.error(request,'Please correct the error below')
	else:					
		form=PasswordChangeForm(request.user)
	return render(request,'change_password.html',{'form':form})
	
def add_question(request):
	return render(request,'add_question.html')

def delete_users(request,pk):
	User.objects.filter(id=pk).delete()	
	messages.success(request,"Data deleted successfully")
	return redirect('manage_users')

def delete_ques(request,pk):
	Questions.objects.filter(id=pk).delete()	
	messages.success(request,"Question deleted successfully")
	return redirect('manage_questions')		

def add_question_data(request):
	if request.session._session:
		if request.method=="POST":
			question=request.POST['question']
			choice1=request.POST['choice1']
			choice2=request.POST['choice2']
			choice3=request.POST['choice3']
			choice4=request.POST['choice4']	
			right_answer=request.POST['right_answer']
			question_data=Questions(questions=question,choice1=choice1,choice2=choice2,choice3=choice3,choice4=choice4,correct_answer=right_answer)
			question_data.save()
			messages.success(request,"Question Added successfully")
			return redirect('manage_questions')
		# return redirect(request,'add_question.html')	
	else:
		return render(request,'login.html')	

def edit_ques(request,pk):
	
	Question=Questions.objects.filter(id=pk).values()

	return render(request,'edit_ques.html',{'quest':Question})

def update_ques_data(request):
	if request.method=="POST":
		question_id=request.POST['question_id']
		question_data=Questions.objects.get(id=question_id)
		question_data.questions=request.POST['questions']
		question_data.choice1=request.POST['choice1']
		question_data.choice2=request.POST['choice2']
		question_data.choice3=request.POST['choice3']
		question_data.choice4=request.POST['choice4']
		question_data.correct_answer=request.POST['right_answer']
		question_data.save()
		messages.success(request,'Questions Updated Successfully')
		return redirect('manage_questions')
	else:
		return redirect('manage_questions')	


def edit_user(request,pk):

	Users=User.objects.filter(id=pk).values()

	return render(request,'edit_user.html',{'users':Users}) 		


def update_user_data(request,):
	if request.method=="POST":
		user_id=request.POST['user_id']
		user_data=User.objects.get(id=user_id)
		user_data.first_name=request.POST['first_name']
		user_data.last_name=request.POST['last_name']
		user_data.email=request.POST['email']
		user_data.username=request.POST['username']
		user_data.save()
		messages.success(request,'User Updated Successfully')
		return redirect('manage_users')
	else:
		return redirect('manage_users')	

def quiz(request):
	if request.session._session:
		questions=Questions.objects.all()
		count= Questions.objects.all().count()
		return render(request,'quiz.html',{'questions':questions,'count':count})
	else:
		return render(request,'login.html')

def result(request):
	values=list(request.POST)
	keys=list(request.POST.items())
	n=1
	newlist= values[n:]

	newkey= keys[n:]
	values_data=Questions.objects.filter(pk__in=newlist).values().order_by('id')
	print(values_data)
	print('')
	l=[]
	count=0
	fc=0
	for i in values_data:
		fc=fc+1
		for j in newkey:
			if(int(i['id'])==int(j[0])):
				#i.update({'your_answer':j[1]})
				i['your_answer'] = j[1]
				l.append(i)
				count=count+1
			else:
				pass 
		
	print(l)	
	return render(request,'result.html',{'post_data':l})		
					

																																																		