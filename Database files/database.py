from peewee import *

db = SqliteDatabase("autog.sqlite3")


class User(Model):
    client_id = CharField()
    Client_secret = CharField()
    Email = CharField()
    Admin = CharField()

    class Meta:
        database = db


class Oauth(Model):
    client_id = CharField()
    Client_secret = CharField()
    Authorization_code_id = CharField()
    Authorization_code = CharField()
    Access_token = CharField()
    Refresh_token = CharField()
    User_information = CharField()

    class Meta:
        database = db


class Assignment(Model):
    Assignment_name = CharField()
    Due = DateTimeField()
    End = DateTimeField()
    Start = DateTimeField()
    Visible_date = DateTimeField()
    Expected_output_file = CharField()
    Expected_input_file = CharField()
    Makefile = CharField()

    class Meta:
        database = db


class Submission(Model):
    Client_id = CharField()
    Assignment_name = CharField()
    Assignment_id = CharField()
    Submission_time = DateTimeField()
    Filename = CharField()
    Fileadd = CharField()
    Score = IntegerField()

    class Meta:
        database = db


