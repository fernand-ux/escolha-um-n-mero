
from tkinter import *
from random  import randint

n=0



janela=Tk()
janela.title("teste a sorte")
janela.geometry('300x200+200+200')
janela.visor=Label()
janela.rod=Label()

 

def result():
 
 janela.visor['text']=randint(0,2)
 janela.visor.pack(side="top")
 

def cont():
  global n
  
  if n > 1000:
    return
  
  result()
  print(janela.visor['text'])
  janela.rod['text']="sua rodada é:", n
  janela.rod.pack(side="left")
  
  n += 1

def Aperte():

 janela.Bt=Button()
 janela.Bt['text']="clique e descubra seu numero"
 janela.Bt.pack(side="top")
 janela.Bt['command']=cont

Aperte()
janela=mainloop()











  

  
   

  





