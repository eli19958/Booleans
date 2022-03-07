#Elizabeth Montero
#3/7/22


#Problem 1

def Equals(a,b):#define function
    if a==b:
        print("{} and {} are equal".format(a,b)) #check numbers if they are equal
    else:
        print("{} and {} are not equal".format(a,b))#check if numbers are not equal

Equals(15,15) #numbers selected 

Equals(15,10)

#Problem 2
def SumGreater(x,y):#define function
    if x+y==10:
        print("Sum is equal to 10")
    elif x+y>10:
        print("Sum is greater than 10")
    else:
        print("Sum is less than 10")

SumGreater(5,4) #less than 10

SumGreater(12,3)#more than 10

SumGreater(6,4) #it equals 10

#Problem 3
def check_five(lst):  #Define function 
  if 5 in lst: # Iterate through list
    print('Number 5 is present in the list') 

check_five([2,6,8,4,5]) # Call function

#Problem 4
def leap_year(year): #Define function 
  if (year % 4) == 0: #Check for divisibilty by 4
    if (year % 100) == 0: #Check for divisibilty by 100
      if (year % 400) == 0: #Check for divisibilty by 400
        print(f"{year} is a leap year") 
      else:
        print(f"{year} is not a leap year") 
    else:
        print(f"{year} is a leap year") 
  else:
    print(f"{year} is not a leap year") 
leap_year(1990)

#Problem 5
class character:
    def __init__(self, nickname, weapons, weaknesses): #define function
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname


    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses
    
    def checks(self,p):
        print("Checks function")
        task = input("What task the character are going to perform(Write,climb,cook)") #select write,climb, cook
        
        #For cooking a dish
        if task == "cook":
            if p.weaknesses == "small":
                print("The character can not cook")
                
            elif ('pan' in p.weapons) and ('groceries' in p.weapons):
                print("The character can cook")     
                
            else:
             print("The character will not Cook")
                
                
        # for climbing a mountain        
        elif task == "climb":
            if p.weaknesses != "slow":
                print("The character can not climb the mountain")
                
            elif ('rope' in p.weapons) and ('coat' in p.weapons) and ("first aid kit") in p.weapons:
                print("The character can climb")
                
            else:
                print("The character will not climb a mountain")
                
        # For writing a book
        elif task == "write":
            if p.weaknesses != "confusion":
                print("The character can not write a book")
                
            elif ('pen' in p.weapons) and ('paper' in p.weapons) and ("idea") in p.weapons:
                print("The character can a write a book")
                
            else:
                print("The character will not write a book")
        
        
        

player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries'] #item list
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)
    
player1.checks(player1)

