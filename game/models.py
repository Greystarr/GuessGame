from django.db import models

# Create your models here.

class Puzzle(models.Model):
    guess = models.CharField(max_length=5) #the guess
    key = models.CharField(max_length=5) #the true answer
    cncp = models.IntegerField(default=0) #correct number correct place
    cnwp = models.IntegerField(default=0) #correct number wrong place
    essay = models.IntegerField(default=0) #number of guesses
    
    def play (self):
        result = False   #result of the game
        self.cnwp=0
        self.cncp=0
        for i in range(0, len(str(self.guess))):
          if self.guess[i] == self.key[i]:
              self.cncp=self.cncp+1
        for i in range(0, len(str(self.guess))):
          if self.guess[i] != self.key[i] and self.guess[i] in self.key :
              self.cnwp=self.cnwp+1
        if self.guess == self.key:
            result= True
        return(result)
