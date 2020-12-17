from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
import secrets
from docxtpl import DocxTemplate
from django.contrib import auth
from datetime import date

import json   

def generate_token():
    return secrets.randbits(100)
     

def resumeAuthor(request):
    try:
        current = request.user
    except User.DoesNotExist:
        current = None
    if current.id is not None:
        if request.method=='POST':
            resumeName = request.POST['resumeName']
            dateOfCreation  = date.today()
            tokenSend = generate_token()
            request.session['token'] = tokenSend
            resume = resumeAuthorModel.objects.create(resumeName=resumeName,dateOfCreation=dateOfCreation,user=current,token=tokenSend)
            resume.save()
            return redirect('resumeAuthor')
        else:
            resumes = resumeAuthorModel.objects.filter(user = current).all()
            context  = {
                'resumes':resumes
            }
        return render(request,"resumeAuthor.html",context)

    else:
        return redirect('login')



   

def acadmic(request,tokenRec):

    try:
        current = request.user
    except User.DoesNotExist:
        current = None
    if current.id is not None:
        try:
            resume = resumeAuthorModel.objects.get(token=tokenRec,user=current)
        except:
            resume=None
        
        if resume is None:
            return redirect('error')
        
        acadmics  = academicModel.objects.filter(resume=resume).all()
        context={
                'tokenRec' : tokenRec,
                'acadmics':acadmics
                
            }
        return render(request,'acadmic.html',context)
    else:
        return redirect('login')

def addAcadmic(request,tokenRec):
    try:
        current = request.user
    except User.DoesNotExist:
        current = None
    if current.id is not None:
        try:
            resume = resumeAuthorModel.objects.get(token=tokenRec,user=current)
        except:
            resume=None
        
        if resume is None:
            return redirect('error')
        else:
            if request.method=='POST':
                instituionName = request.POST['institutionName']
                degreeName = request.POST['degreeName']        
                degreeType = request.POST['degreeType']
                startingDate = request.POST['startingDate']
                endingDate = request.POST['endingDate']
                context={
                        'tokenRec' : tokenRec,
                        
                    }
                xx = academicModel.objects.create(institutionName=instituionName,degreeName=degreeName,degreeType=degreeType,startingDate=startingDate,endingDate=endingDate,resume=resume)
                return redirect('acadmic',tokenRec)

            return render(request,'addAcadmic.html',context)
    else:
        return redirect('login')
    

def workExp(request,tokenRec):

    try:
        current = request.user
    except User.DoesNotExist:
        current = None
    if current.id is not None:
        try:
            resume = resumeAuthorModel.objects.get(token=tokenRec,user=current)
        except:
            resume=None
        
        if resume is None:
            return redirect('error')
        
        work  = workExpModel.objects.filter(resume=resume).all()
        context={
                'tokenRec' : tokenRec,
                'work':work
                
            }
        return render(request,'workExp.html',context)
    else:
        return redirect('login')
    


def addWorkExp(request,tokenRec):
    try:
        current = request.user
    except User.DoesNotExist:
        current = None
    if current.id is not None:
        try:
            resume = resumeAuthorModel.objects.get(token=tokenRec,user=current)
        except:
            resume=None
        
        if resume is None:
            return redirect('error')
        else:
            if request.method=='POST':
                companyName = request.POST['companyName']
                role = request.POST['role']        
                designation = request.POST['designation']
                description = request.POST['description']
                startingDate = request.POST['startingDate']
                endingDate = request.POST['endingDate']
                context={
                        'tokenRec' : tokenRec,
                        
                    }
                xx = workExpModel.objects.create(resume=resume,startingDate=startingDate,endingDate=endingDate,companyName=companyName,role=role,designation=designation,description=description)
                
                return redirect('workExp',tokenRec)
            return render(request,'addWorkExp.html',context)
    else:
        return redirect('login')



def additionalDetails(request,tokenRec):

    try:
        current = request.user
    except User.DoesNotExist:
        current = None
    if current.id is not None:
        try:
            resume = resumeAuthorModel.objects.get(token=tokenRec,user=current)
        except:
            resume=None
        
        if resume is None:
            return redirect('error')
        
        additional  = additionalDetailsModel.objects.filter(resume=resume).all()
        context={
                'tokenRec' : tokenRec,
                'additional':additional
                
            }
        return render(request,'additionalDetails.html',context)
    else:
        return redirect('login')


def addAdditionalDetails(request,tokenRec):
    try:
        current = request.user
    except User.DoesNotExist:
        current = None
    if current.id is not None:
        try:
            resume = resumeAuthorModel.objects.get(token=tokenRec,user=current)
        except:
            resume=None
        
        if resume is None:
            return redirect('error')
        else:
            if request.method=='POST':
                email = request.POST['email']
                contactNumber = request.POST['contactNumber']        
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                address = request.POST['address']
                profilePic = request.POST['profilePic']
                context={
                        'tokenRec' : tokenRec,
                        
                    }
                xx = additionalDetailsModel.objects.create(resume=resume,email=email,contactNumber=contactNumber,first_name=first_name,last_name=last_name,address=address)

                return redirect('additionalDetails',tokenRec)
            return render(request,'addAdditionalDetails.html',context)
    else:
        return redirect('login')

def skills(request,tokenRec):

    try:
        current = request.user
    except User.DoesNotExist:
        current = None
    if current.id is not None:
        try:
            resume = resumeAuthorModel.objects.get(token=tokenRec,user=current)
        except:
            resume=None
        
        if resume is None:
            return redirect('error')
        
        skillsDet  = skillsModel.objects.filter(resume=resume).all()
        context={
                'tokenRec' : tokenRec,
                'skillsDet':skillsDet
                
            }
        return render(request,'skills.html',context)
    else:
        return redirect('login')



def addSkills(request,tokenRec):
    try:
        current = request.user
    except User.DoesNotExist:
        current = None
    if current.id is not None:
        try:
            resume = resumeAuthorModel.objects.get(token=tokenRec,user=current)
        except:
            resume=None
        
        if resume is None:
            return redirect('error')
        else:
            if request.method=='POST':
                nameOfSkill = request.POST['nameOfSkill']
                selfRating = request.POST['selfRating']        
                context={
                        'tokenRec' : tokenRec,
                        
                    }
                xx = skillsModel.objects.create(resume=resume,nameOfSkill=nameOfSkill,selfRating=selfRating)


                return redirect('skills',tokenRec)
            return render(request,'addSkills.html',context)
    else:
        return redirect('login')

def awards(request,tokenRec):

    try:
        current = request.user
    except User.DoesNotExist:
        current = None
    if current.id is not None:
        try:
            resume = resumeAuthorModel.objects.get(token=tokenRec,user=current)
        except:
            resume=None
        
        if resume is None:
            return redirect('error')
        
        awardDet  = awardsAchievementHobbiesModel.objects.filter(resume=resume).all()
        context={
                'tokenRec' : tokenRec,
                'awardDet':awardDet
                
            }
        return render(request,'awards.html',context)
    else:
        return redirect('login')



def addAward(request,tokenRec):
    try:
        current = request.user
    except User.DoesNotExist:
        current = None
    if current.id is not None:
        try:
            resume = resumeAuthorModel.objects.get(token=tokenRec,user=current)
        except:
            resume=None
        
        if resume is None:
            return redirect('error')
        else:
            if request.method=='POST':
                nameOfaward = request.POST['nameOfaward']
                description = request.POST['description']        
                context={
                        'tokenRec' : tokenRec,
                        
                    }
                xx = awardsAchievementHobbiesModel.objects.create(resume=resume,nameOfaward=nameOfaward,description=description)


                return redirect('awards',tokenRec)
            return render(request,'addAwards.html',context)
    else:
        return redirect('login')






def error(request):
    return render(request,'error.html')

def showTemplates(request,tokenRec):
    try:
        current = request.user
    except User.DoesNotExist:
        current = None
    if current.id is not None:
        try:
            resume = resumeAuthorModel.objects.get(token=tokenRec,user=current)
        except:
            resume=None
        
        if resume is None:
            return redirect('error')
        else:
            totalResumes = resumeTemplatesModel.objects.all()
            context ={
                'tokenRec':tokenRec,
                'totalResumes': totalResumes

            }
            return render(request,'showTemplates.html',context)



def selectTemplate(request,resumeId,tokenRec):
    print(request.user)
    resumeSelected = resumeTemplatesModel.objects.get(id = resumeId)
    doc_back = resumeSelected.doc
    doc = DocxTemplate(doc_back)
    context = getResumeData(tokenRec)
    doc.render(context)
    
    doc.save("generated_doc.docx")

    return HttpResponse('HELLOo')

    
    
def getResumeData(token):
    resumeToSend = resumeAuthorModel.objects.get(token=token)
    context  ={

    }
    try:
        acad = academicModel.objects.filter(resume = resumeToSend).all()
    except:
        acad = None
    try:
        work = workExpModel.objects.filter(resume=resumeToSend).all()
    except:
        work = None
    try: 
        skill = skillsModel.objects.filter(resume=resumeToSend).all()
    except:
        skill = None
    try:

        award = awardsAchievementHobbiesModel.objects.filter(resume=resumeToSend).all()
    except:
        award = None
    try:
        additional = additionalDetailsModel.objects.filter(resume=resumeToSend).all()
    except:
        additional = None

    if acad is not None:
        context['acad'] = acad
    
    if work is not None:
        context['work'] = work
    if skill is not None:
        context['skill'] = skill
    if award is not None:
        context['award'] = award
    if additional is not None:
        context['additional'] = additional
    
    return context




def register(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        
        if password==confirmPassword:
            try:
                user = User.objects.get(username = email)
            except:
                user = None

            if user is None:
                User.objects.create_user(username=email,password = password,email=email)
                return redirect('login')
            else:
                return redirect('register')
        else:
            return redirect('register')
    return render(request,'register.html')

def login(request):
    try:
        current = request.user

    except User.DoesNotExist:
        current=None

    print(current.id)
    if current.id is not None:
        return redirect('resumeAuthor')
    else:
        if request.method=='POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(username=email,password = password)
            if user is not None:
                auth.login(request,user)
                return redirect('resumeAuthor')
            else:
                return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')






            






    














            

    







    
