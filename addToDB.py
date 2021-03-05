from peewee import *
from datetime import datetime as dt
import os,binascii

class User(Model):
    Client_id = CharField()
    Client_secret = CharField()
    Email = CharField()
    Administrator = IntegerField(default=0)

    class Meta:
        database = SqliteDatabase('Users.db')

class Oauth_Token(Model):
    Client_id = CharField()
    Client_secret = CharField()
    Authorization_code_id = CharField()
    Authorization_code = CharField()
    Access_token = CharField()
    Refresh_token = CharField()
    User_information = CharField()

    class Meta:
        database = SqliteDatabase('Oauth_token_google.db')

class Given_Assignment(Model):
    Assignment_Name = CharField()
    Due_at = DateTimeField()
    End_at = DateTimeField()
    Visible_at = DateTimeField(default=dt.now())
    Start_at = DateTimeField()

    class Meta:
        database = SqliteDatabase('Given_Assignment_information')

class Student_Assignment(Model):
    Key = CharField()
    Client_id = CharField()
    Assignment_Name = CharField()
    Submission_time = DateTimeField(default=dt.now())
    Filename = CharField()
    File_address = CharField()
    Score = FloatField(default=-1)

    class Meta:
        database = SqliteDatabase('Student_Assignment_information.db')


def addUser(clientID, clientSecret, email, admin):

    newUser = User.create(Client_id=clientID, Client_secret=clientSecret, Email=email, Administrator=admin)

    newUser.save()

    return 0

def addOauthToken(clientID, clientSecret, authCodeID, authCode, accessToken, refreshToken, userInfo):

    newTokens = Oauth_Token.create(Client_id=clientID, Client_secret=clientSecret,
                                   Authorization_code_id=authCodeID, Authorization_code=authCode,
                                   Access_token=accessToken, Refresh_token=refreshToken, User_information=userInfo)

    newTokens.save()

    return 0


def addAssignment(name, start, due, end, visible):

    newAssignment = Given_Assignment.create(Assignment_Name=name, Due_at=due, End_at=end,
                                            Visible_at=visible, Start_at=start)

    newAssignment.save()

    return 0


def addSubmission(id, assignmentName, file):

    path, filename = saveFile(file) #assumes there is a saveFile method that returns the
                                    # path of the file as well as the name of the file

    #we talked about making the key assignmentName + ' ' + id
    key = assignmentName + ' ' + id

    #or we could just use a random hexadecimal number
    key = binascii.b2a_hex(os.urandom(15)) #gets random number from the os which is more secure if we care about that

    newSubmission = Student_Assignment.create(Key=key, Client_id=id, Assignment_Name=assignmentName,
                                              Submission_time=dt.now(), Filename=filename,
                                              File_address=path, Score=-1)

    newSubmission.Score = grade(path) #assumes there is a grade function that grades the assignment

    newSubmission.save()

    return 0



