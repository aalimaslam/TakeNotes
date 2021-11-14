from django.http.response import Http404
from django.shortcuts import render, redirect, Http404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Note
import smtplib
# Create your views here.

note_req =  ""

def update(request):
    
    notes = list(Note.objects.filter(user = str(request.user)))
    
    context = {"notes":notes}

    for i in context['notes']:

        if i.title == note_req:

            deets= {"note":i}

            if request.method == "POST":

                newTitle = request.POST.get("title")

                newNote = request.POST.get("note")

                print(newTitle, newNote)

                i.title = newTitle

                i.note = newNote

                i.save()

                return redirect('/')

    return render(request, "Update.html", deets)



def home(request):
    
    if request.user.is_anonymous == True:
    
        return render(request,'index.html')
    
    else:
    
        return redirect("/list")



def signUp(request):
    
    if request.user.is_anonymous == True:
    
        if request.method == 'POST':
    
            firstName = request.POST.get('firstName')
    
            lastName = request.POST.get('lastName')
    
            userName = request.POST.get('Username')
    
            Email = request.POST.get('email')

            passWord = request.POST.get('password')

            Confirm_passWord = request.POST.get('confirmPassword')
            
            userlist = User.objects.all()

            print(userlist,"44")
        
            if User.objects.filter(username = userName).exists():

                messages.info(request,"Username is already Taken")
            
            else:

                if passWord == Confirm_passWord:

                    user = User.objects.create_user(userName,Email,password=passWord )

                    user.first_name = firstName

                    user.last_name = lastName

                    user.is_active = True

                    user.is_staff = 1

                    user.save()

                    return redirect("/signin")

                else:

                    messages.info(request,"Passwords Does'nt match!!")

        return render(request,"signup.html")

    else:

        return redirect("/")



def signin(request):

    if request.user.is_anonymous == 1:

        if request.method == 'POST':

            userName = request.POST.get("loginUsername")

            PassWord = request.POST.get("loginPassword")

            user = auth.authenticate(username = userName, password = PassWord)

            if user is not None:

                auth.login(request,user)

                return redirect('/')

            else:

                messages.info(request,'Username or Password incorrect')

        return render(request,'login.html')

    else:

        return redirect("/")



def create(request):

    if request.method == "POST":

        Note_title = request.POST.get("title")

        Note_note = request.POST.get("note")

        UserNote = Note.objects.create(user = str(request.user),title = Note_title, note = Note_note)

        print(Note_title,Note_note)

        UserNote.save()

        return redirect("/")

    return render(request,'addNote.html')



def see(request):

    if request.user.is_anonymous == False:
    
    # lIST OF THE NOTES
    
        notes = list(Note.objects.filter(user = str(request.user)))
    
        context = {"notes":notes}
    
        if request.method == 'POST':
    
            # GET THE NOTE REQUESTED
    
            global note_req
            
            note_req = request.POST.get("note_req")
    
            if request.POST.get("form_type") == note_req:
    
                # CHECK THE DETAILS OF THE NOTED
    
                for i in context['notes']:
    
                    if i.title == note_req:
    
                        deets = {'note': i}
    
                        return render(request,'read.html',deets)
    
            # Updating the note

            elif request.POST.get("form_type") == "EDIT":

                print("Editing", )

                for i in context['notes']:

                    if i.title == note_req:

                        deets = {"note":i}
                    
                return redirect("/update")

                #missing Update



            # Deleting the note

            elif request.POST.get("form_type") == "DELETE":

                 for i in context['notes']:

                    if i.title == note_req:

                        i.delete()

                        return redirect("/")

        return render(request,'UserIndex.html',context)

    else:

        return redirect("/")



def profile(request):

    if request.user.is_anonymous == 0:

        if request.method == "POST":

            auth.logout(request)

            return redirect("/signin")

        return render(request,"profile.html")

    else:

        return redirect("/")




def ChangePassword(request):
    if request.user.is_anonymous == False:
        
        return render(request, "changePassword.html")
    
    else:

        return redirect("/")


