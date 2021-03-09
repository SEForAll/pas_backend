from datetime import datetime as dt
from database import *

def addUser(clientID, clientSecret, email, admin):

    newUser = User.create(client_id=clientID, Client_secret=clientSecret, Email=email, Admin=admin)

    newUser.save()

    return 0

def addOauth(clientID, clientSecret, authCodeID, authCode, accessToken, refreshToken, userInfo):

    newTokens = Oauth.create(client_id=clientID, Client_secret=clientSecret,
                                   Authorization_code_id=authCodeID, Authorization_code=authCode,
                                   Access_token=accessToken, Refresh_token=refreshToken, User_information=userInfo)

    newTokens.save()

    return 0


def addAssignment(name, start, due, end, visible, expectedIn, expectedOut, makefile):

    newAssignment = Assignment.create(Assignment_Name=name, Due=due, End=end,
                                      Start=start, Visible_date=visible, Expected_output_file=expectedOut,
                                      Expected_input_file=expectedIn, Makefile=makefile)

    newAssignment.save()

    return 0


def addSubmission(id, assignmentName, file):

    path, filename = saveFile(file) #assumes there is a saveFile method that returns the
                                    # path of the file as well as the name of the file

    assignmentID = assignmentName + ' ' + id

    newSubmission = Submission.create(Assignment_id=assignmentID, Client_id=id, Assignment_Name=assignmentName,
                                      Submission_time=dt.now(), Filename=filename,
                                      Fileadd=path, Score=-1)

    newSubmission.Score = grade(path) #assumes there is a grade function that grades the assignment

    newSubmission.save()

    return 0



