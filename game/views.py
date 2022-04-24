from django.shortcuts import render
from game.models import Puzzle
import string, random
# Create your views here.
def red(s):                    #check if a string had a redundant
    test=False
    for i in s:
        if s.count(i)>1:
            test=True
        
    return(test)
def createRandom():                #generate a non redundant random string
  
  while True:
     ran=''
  
     ran = ''.join(random.choices(string.ascii_lowercase, k = 3))
     if not red(ran):
          break
  return(ran)
game=Puzzle(
      key=createRandom(),
      )

def index(request):
 if request.method == "POST":
  if red(request.POST["text"]):
       game.guess="norep"
  else:     
       game.guess=request.POST["text"]
       game.essay=game.essay+1
 game.play()
 if game.play():
     game.key=createRandom()
     game.essay=0
     
 return render(request, "index.html",{"ran":game})