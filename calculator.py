from tkinter import *
import math
from pygame import mixer
mixer.init()
import speech_recognition

def click(value):
   ex=entryField.get()#ex variable store the value entered.

   ans=''

   try:
      if value=="C":
         ex=ex[:-1]#123 will be 12 bcz of list slicing.
         entryField.delete(0,END)
         entryField.insert(0,ex)
         return

      elif value=="CE":
         entryField.delete(0,END)
         return

      elif value=="√":
         ans=math.sqrt(eval(ex))#eval() evaluate the Python expression as a 'string' and return the value as an integer
               

      elif value=="π":
         ans=math.pi
               

      elif value=="cosθ":
         ans=math.cos(math.radians(eval(ex)))
               
      elif value=="tanθ":
         ans=math.tan(math.radians(eval(ex)))
               

      elif value=="sinθ":
         ans=math.sin(math.radians(eval(ex)))
               
      elif value=="2π":
         ans=2*math.pi

      elif value=="cosh":
         ans=math.cosh(eval(ex))

      elif value=="tanh":
         ans=math.tanh(eval(ex))

      elif value=="sinh":
         ans=math.sinh(eval(ex))

      elif value==chr(8731):
         ans=eval(ex)**(1/3)

      elif value=="x\u02b8":#7**2
         entryField.insert(END,"**")
         return

      elif value=="x\u0003":
         ans=eval(ex)**3

      elif value=="x\u00B2":
         ans=eval(ex)**2

      elif value=="ln":
         ans=math.log(eval(ex))

      elif value=="deg":
         ans=math.degrees(eval(ex))

      elif value=="rad":
         ans=math.radians(eval(ex))

      elif value=="e":
         ans=math.e

      elif value=="log₁₀":
         ans=math.log10(eval(ex))

      elif value=="x!":
         ans=math.factorial(eval(ex))

      elif value==chr(247):
         entryField.insert(END,"/")
         return
            
      elif value=="=":
         ans=eval(ex)

      else:
         entryField.insert(END,value)
         return


      entryField.delete(0,END)
      entryField.insert(0,ans)


   except SyntaxError:
      pass

def add(a,b):
   return a+b
def sub(a,b):
   return a-b
def mul(a,b):
   return a*b
def div(a,b):
   return a/b
def mod(a,b):
   return a%b
def floor(a,b):
   return a//b
def power(a,b):
   return a**b
def factorial(a):
   if a==0:
      return 1
   else:
      return a*factorial(a-1)
def square(a):
   return a**0.5
def cube(a):
   return a**3
def sin(a):
   return math.sin(a)
def cos(a):
   return math.cos(a)
def tan(a):
   return math.tan(a)
def log(a):
   return math.log(a)
def pi():
   p=math.pi
   return p
def e():
   return math.e
def hcf(a,b):
   h=math.gcd(a,b)
   return h
def lcm(a,b):
   l=math.lcm(a,b)
   return l
def percentage(a,b):
   p=(a*b)/100
   return p


operrations={
   "ADDITION": add, "SUM": add, "PLUS": add, "ADD":add, "TOTAL":add,
    "SUBTRACTION": sub, "MINUS": sub, "SUBTRACT": sub, "DIFFERENCE": sub,
    "MULTIPLICATION": mul, "MULTIPLY": mul, "PRODUCT": mul,
    "DIVISION": div, "DIVIDE": div,
    "MODULUS": mod, "MOD": mod,
    "FLOOR DIVISION": floor, "FLOOR": floor,
    "POWER": power, "FACTORIAL": factorial,
    "SQUARE ROOT": square, "SQUARE": square,
    "CUBE ROOT": cube, "CUBE": cube,
    "SINE": sin, "SIN": sin, "COS": cos, "TAN": tan,
    "LOGARITHM": log, "LOG": log,
    "PI": pi, "EULER'S NUMBER": e,
    "HCF": hcf, "LCM": lcm,
    "PERCENTAGE": percentage, "PERCENT": percentage
    }


def findNumber(t):
   l=[]
   for i in t:
      try:
         l.append(int(i))
      except ValueError:
         pass
   return l




def audio():
   mixer.music.load("music1.mp3")
   mixer.music.play()

   sr=speech_recognition.Recognizer()
   with speech_recognition.Microphone() as n:
      try:
         sr.adjust_for_ambient_noise(n,duration=0.2)
         voice=sr.listen(n)
         text=sr.recognize_google(voice)
         print(text)
         mixer.music.load("music2.mp3")
         mixer.music.play()
         list=text.split(' ')
         for word in list:

            if word.upper() in operrations.keys():
               l=findNumber(list)
               result=(operrations[word.upper()])(l[0],l[1])#calling the fucntion form dictionary

               entryField.delete(0,END)
               entryField.insert(0,result)
            

           


            else:
               pass



      except:
         pass 




   
      
 

root=Tk()
root.title("Smart Calculator")
root.config(bg="dodgerblue3")
root.geometry("680x486+100+100")

loadImage=PhotoImage(file='logo.png')
loadLable=Label(root,image=loadImage,bg="dodgerblue3")
loadLable.grid(row=0,column=0)


entryField=Entry(root,font=('arial',20,'bold'),bg="dodgerblue3",fg='white',bd=10,relief=SUNKEN,width=30)
entryField.grid(row=0,column=0,columnspan=8)

micImage=PhotoImage(file='microphone.png')
micButton=Button(root,image=micImage,bg="dodgerblue3",bd=0,activebackground="dodgerblue3",command=audio)
micButton.grid(row=0,column=7)

button_text_list=["C", "CE", "√", "+", "π","cosθ","tanθ","sinθ", 
                  "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh", 
                  "4", "5", "6","*" , chr(8731), "x\u02b8", "x\u0003", 
                  "x\u00B2", "7", "8", "9", chr(247), "ln", "deg", "rad", 
                  "e", "0", ".", "%", "=", "log₁₀", "(" ,")", "x!"]
rowv=1
columnv=0
for i in button_text_list:
    
    button=Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg="dodgerblue3",fg='white'
                    ,font=('arial',18,'bold'),activebackground="dodgerblue3",command=lambda button=i: click(button))
    button.grid(row=rowv,column=columnv,pady=1)
    columnv+=1
    if columnv>7:
        rowv+=1
        columnv=0




root.mainloop()