# questions and answers
# vote them up or down
# users can edit questions and answers in a fashion similar to wiki
# post new questions


#### Actors
# Non-Member
# Member
# ADMIN
# Moderator
# System

# Constants
import datetime
from abc import ABC


class AccountStatus :
    ACTIVE = "active"

class QuestionStatus:
    OPEN ="open"
    CLOSED ="closed"
    ONHOLD="onhold"
    DELTED =""

class Account:
    def __init__(self,id,password,name,address,email,phone,status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__name = name
        self.__email= email
        self.__phone = phone
        self.__address= address
        self.__status = status
        self.__reputation = 0

    def reset_password (self):
        pass


class Member():
    # Aggregation (may have a account) or Composition
    def __init__(self,account):
        self.__account = account
        self.__badges = []

    def get_reputation(self):
        return self.__account.get_reputation()

    def get_email(self):
        return self.__account.get_email()

    def post_questions(self):
        pass

    def answer(self,question_id):
        pass

    def add_comments(self,question_id):
        pass

    def add_comments(self,answer_id):
        pass

    def upvote_question(self,question_id):
        pass

    def upvote_answer(self,answer_id ):
        pass


class Admin:
    def block(self,member_id):
        pass

    def unblock(self,member_id):
        pass


class Moderator :
    def close(self,question_id):
        pass

    def undelete_question(self,question_id):
        pass


class System:
    def send_notification(self,notification_id ):
        pass



class Question:
    def __init__(self):
        self.__question_id =None
        self.__title =None
        self.__text =None
        self.__tags=[]
        self.__answers =[]
        self.__bounty = None
        self.__up_votes = None
        self.__view_count = None
        self.__down_votes = None
        self.__creation_time = datetime.now()
        self.__update_time= datetime.now()
        self.__status = QuestionStatus.OPEN
    def open(self,question_id):
        pass

    def close(self,question_id):
        pass

    def answer(self,question_id ):
        pass

    def add_tag(self,tag_id ):
        None

    def create_question(self):
        pass

    def publish_question(self):
        pass



class Tag:
    def __init__(self):
        __tag_id  = None
        __tag_text = None
        __tag_description= None
        __daily_asked_frequency = 0
        __weekly_asked_frequency = 0


    def create_tag(self,tag_text, tag_description):
        pass



class Notiification:
    def __init__(self, id ,  content):
        self.__notification_id = id
        self.__created_on = datetime.datetime.now()
        self.content = content

    def send(self):
        pass


class Answer:
    def __init__(self):
        __answer_id = None
        __text = None
        __up_votes=None
        __down_votes=None

    def update(self):
        pass


class QuestionAnswerMapping :
    def __init__(self):
        __question_id = None
        __answer_id  = None



class Photo:
    def __init__(self,id , path , member):
        self.__photo_id = id
        self.__photo_path = path
        self.__creation_date = datetime.now()
        self.__creating_member = member

    def delete(self):
        None

class Bounty:
    def __init__(self,reputation,expiry):
        self.__reputaion = reputation
        self.__expiry = expiry

    def modify_reputation(self,reputation):
        None



class Search(ABC):
    def search(self,query):
        None







