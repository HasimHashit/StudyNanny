# for now Crow but i prefer keow
import random
import threading
import schedule
import time
from twilio.rest import Client


def studyTime():
    theList = [
        'You gotta study "Mathematics" now bro,i know you hate it but u just gotta',
        'You got Machine Learning NOW!!!',
        'I want you to study Physics NOW!!!! Go DO it Brah!!!',
        'Biology,is what you gotta study now BRO!!!,Its all about understanding the signs,Knowlodge BABY!!!',
        'God calls Bro,You gotta study the Quran,and Hadiths remeber "Knowlodge with Action" ',
        'I know you feel like chilling or not but you got a book/audiobook to read or listen to so go do that!!!',
'You got panda classes bro, read or watch a video',
'You got Data Science class bro, u got a video for this alrady'
'You to brainstorm a python project'
'Make a video for the project you made'
'REMEMBER "PRACTICE, PRACTICE, PRACTICE" '
'Watch your stomach bro everything in moderation'
'Build a project!!!!!'

    ]
    choices = random.choice(theList)
    print(choices)


    account_sid = 'ACb8b5d1ad4fc61387577c55290863470a'
    auth_token = '3b79785c4a053a3fce756931bf176f80'
    client = Client(account_sid, auth_token)

    message = client.messages \
          .create(
        body= choices,
        from_= '+12514395136',
        to= '+2349060540946'
    )



def theTime():
    timer = threading.Timer(1.0, studyTime)
    timer.start()
    print("Timer initialized,loading........")


schedule.every().day.at("12:00").do(theTime)
schedule.every(180).minutes.do(theTime)

while True:
    schedule.run_pending()
    time.sleep(1)


