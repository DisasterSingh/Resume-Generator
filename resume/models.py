from django.db import models
from django.contrib.auth.models import User


class resumeAuthorModel(models.Model):
    resumeName = models.CharField(max_length=10000)
    dateOfCreation  = models.DateField()
    token = models.CharField(max_length=10000000)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.resumeName


class academicModel(models.Model):
    institutionName = models.CharField(max_length=1000)
    degreeType = models.CharField(max_length=1000)
    degreeName = models.CharField(max_length=1000)
    startingDate  = models.DateField()
    endingDate  = models.DateField()

    resume = models.ForeignKey(resumeAuthorModel,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.degreeType



class workExpModel(models.Model):
    companyName = models.CharField(max_length=1000)
    role = models.CharField(max_length=1000)
    designation  = models.CharField(max_length = 1000)
    startingDate  = models.DateField()
    endingDate  = models.DateField()
    description = models.CharField(max_length=100000)
    resume = models.ForeignKey(resumeAuthorModel,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.companyName


class additionalDetailsModel(models.Model):
    email = models.CharField(max_length=10000)
    contactNumber  = models.IntegerField()
    first_name = models.CharField(max_length=10000)
    last_name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    profilePic = models.FileField(upload_to='profilePics/')
    
    resume = models.ForeignKey(resumeAuthorModel,on_delete=models.DO_NOTHING)
    

    def __str__(self):
        return self.email




class skillsModel(models.Model):
    nameOfSkill = models.CharField(max_length=10000)
    selfRating = models.IntegerField()
    resume = models.ForeignKey(resumeAuthorModel,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.nameOfSkill
    

class awardsAchievementHobbiesModel(models.Model):
    nameOfaward = models.CharField(max_length=10000)
    description = models.CharField(max_length=100000)
    resume = models.ForeignKey(resumeAuthorModel,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.nameOfaward



class resumeTemplatesModel(models.Model):
    nameOfResume = models.CharField(max_length=1000)
    doc = models.FileField(upload_to = "doc/")
    image = models.FileField(upload_to='image/')
    
    def __str__(self):
        return self.nameOfResume


    


    











