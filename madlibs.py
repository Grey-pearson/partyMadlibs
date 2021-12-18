# hello world

def blank():
    print('please enter a') 

blank()
name = str(input('name: '))
blank()
theme = str(input('theme: '))
blank()
place = str(input('place: '))
blank()
dotw = str(input('day of the week: '))
blank()
time = str(input('time: '))
blank()
verb = str(input('verb: '))
blank()
animal = str(input('animal: '))
blank()
bodyp = str(input('body part: '))
blank()
contactinfo = str(input('contact info: '))

madlib = f'{name} is having a great {theme} party! its going to be at {place}\
 on {dotw} please make sure to show up at {time}, or else you will be required \
 to {verb} a/an {animal} with your {bodyp} RSVP at {contactinfo}'

print(madlib)