from tkinter import *
from tkinter import ttk



cor1="#473335"
cor2="#FCAA67"
cor3="#d7f9f1"  #ecra
cor4="#548687" # numeros
cor5="#b0413e" #operacoes

janela=Tk()
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(background=cor1)

frame_tela=Frame(janela, width=235,height=50,bg=cor3)
frame_tela.grid(row=0,column=0)

frame_corpo=Frame(janela, width=235,height=268)
frame_corpo.grid(row=1,column=0)

todos_valores=''

def entrar_valores(event):

    global todos_valores

    todos_valores=todos_valores+ str(event)


    #passar valor para label
    valor_text.set(todos_valores)

#funcao calcular
def calcular():
    global todos_valores
    resultado= eval(todos_valores)
    valor_text.set(str(resultado))

#funcao limpar tela
def limpar_tela():
    global todos_valores
    todos_valores=''
    valor_text.set('')



#criar label

valor_text= StringVar()

app_label= Label(frame_tela, textvariable= valor_text, width=16,height=2,padx=7, relief='flat', anchor='e', justify='right', font=("Ivy 18 "), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)

#criar botoes
b1=Button(frame_corpo, command=limpar_tela, text='C', width=11, height=2, bg=cor4, font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
b1.place(x=0,y=0)

b2=Button(frame_corpo,command=lambda:entrar_valores('%'), text='%', width=5, height=2,bg=cor4, font=("Ivy 13 bold"), relief="raised", overrelief="ridge" )
b2.place(x=118,y=0)

b3=Button(frame_corpo,command=lambda:entrar_valores('/'), text='/', width=5, height=2,bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
b3.place(x=177,y=0)


b5=Button(frame_corpo,command=lambda:entrar_valores('7'), text='7', width=5, height=2,bg=cor4, font=("Ivy 13 bold"), relief="raised", overrelief="ridge" )
b5.place(x=0,y=52)
b6=Button(frame_corpo,command=lambda:entrar_valores('8'), text='8', width=5, height=2,bg=cor4, font=("Ivy 13 bold"), relief="raised", overrelief="ridge" )
b6.place(x=59,y=52)
b7=Button(frame_corpo,command=lambda:entrar_valores('9'), text='9', width=5, height=2,bg=cor4, font=("Ivy 13 bold"), relief="raised", overrelief="ridge" )
b7.place(x=119,y=52)
b8=Button(frame_corpo,command=lambda:entrar_valores('*'), text='*', width=5, height=2,bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
b8.place(x=177,y=52)

b9=Button(frame_corpo,command=lambda:entrar_valores('4'), text='4', width=5, height=2,bg=cor4, font=("Ivy 13 bold"), relief="raised", overrelief="ridge" )
b9.place(x=0,y=104)
b10=Button(frame_corpo,command=lambda:entrar_valores('5'), text='5', width=5, height=2,bg=cor4, font=("Ivy 13 bold"), relief="raised", overrelief="ridge" )
b10.place(x=59,y=104)
b11=Button(frame_corpo,command=lambda:entrar_valores('6'), text='6', width=5, height=2,bg=cor4, font=("Ivy 13 bold"), relief="raised", overrelief="ridge" )
b11.place(x=119,y=104)
b12=Button(frame_corpo,command=lambda:entrar_valores('-'), text='-', width=5, height=2,bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
b12.place(x=177,y=104)

b13=Button(frame_corpo,command=lambda:entrar_valores('1'), text='1', width=5, height=2,bg=cor4, font=("Ivy 13 bold"), relief="raised", overrelief="ridge" )
b13.place(x=0,y=156)
b14=Button(frame_corpo,command=lambda:entrar_valores('2'), text='2', width=5, height=2,bg=cor4, font=("Ivy 13 bold"), relief="raised", overrelief="ridge" )
b14.place(x=59,y=156)
b15=Button(frame_corpo,command=lambda:entrar_valores('3'), text='3', width=5, height=2,bg=cor4, font=("Ivy 13 bold"), relief="raised", overrelief="ridge" )
b15.place(x=119,y=156)
b16=Button(frame_corpo,command=lambda:entrar_valores('+'), text='+', width=5, height=2,bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
b16.place(x=177,y=156)

b17=Button(frame_corpo,command=lambda:entrar_valores('0'), text='0', width=11, height=2, bg=cor4, font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
b17.place(x=0,y=208)

b18=Button(frame_corpo,command=lambda:entrar_valores('.'), text='.', width=5, height=2,bg=cor4, font=("Ivy 13 bold"), relief="raised", overrelief="ridge" )
b18.place(x=118,y=208)

b19=Button(frame_corpo,command= calcular, text='=', width=5, height=2,bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief="raised", overrelief="ridge")
b19.place(x=177,y=208)








janela.mainloop()
