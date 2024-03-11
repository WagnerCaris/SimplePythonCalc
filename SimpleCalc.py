# importando tkinter
from tkinter import *
from tkinter import ttk

cor1= "#3d3d3d" #dark gray
cor2= "#ffffff" #white
cor3= "#283266" #blue
cor4= "#a1a1a6" #white gray
cor5= "#f77a05" #orange

janela =Tk()
janela.title("Caluladora")
janela.geometry("324x360")
janela.config(bg=cor1)     




# criando frames
frame_tela = Frame(janela, width=1999, height=60, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=1999, height=300)
frame_corpo.grid(row=1, column=0)

# variavel todos os valores

todos_valores = ''

# criando label
valor_texto = StringVar()

#criando uma fucao
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    #passando valor para tela
    valor_texto.set(todos_valores)

# fucnacao para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))


    # fucancao limpar tela
def limpar_tela():
    global todos_valores
    todos_valores =""
    valor_texto.set("")



app_label = Label(frame_tela, textvariable=valor_texto, width=28, height=3, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font= ('Ivy 15 '), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

#criando botoes
b_1 = Button(frame_corpo, text="C", width=15, height=3, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command=limpar_tela)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text="%", width=9, height=3, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('%'))
b_2.place(x=149, y=0)

b_3 = Button(frame_corpo, text="/", width=9, height=3, bg=cor5, fg=cor2, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('/'))
b_3.place(x=230, y=0)

b_4 = Button(frame_corpo, text="7", width=9, height=3, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('7'))
b_4.place(x=0, y=58)

b_5 = Button(frame_corpo, text="8", width=9, height=3, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('8'))
b_5.place(x=75, y=58)

b_6 = Button(frame_corpo, text="9", width=9, height=3, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('9'))
b_6.place(x=149, y=58)

b_6 = Button(frame_corpo, text="X", width=9, height=3, bg=cor5, fg=cor2, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('*'))
b_6.place(x=230, y=58)

b_7 = Button(frame_corpo, text="4", width=9, height=3, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('4'))
b_7.place(x=0, y=116)

b_8 = Button(frame_corpo, text="5", width=9, height=3, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('5'))
b_8.place(x=75, y=116)

b_9 = Button(frame_corpo, text="6", width=9, height=3, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('6'))
b_9.place(x=149, y=116)

b_10 = Button(frame_corpo, text="-", width=9, height=3, bg=cor5,fg=cor2, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('-'))
b_10.place(x=230, y=116)

b_11 = Button(frame_corpo, text="1", width=9, height=3, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('1'))
b_11.place(x=0, y=174)

b_12 = Button(frame_corpo, text="2", width=9, height=3, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('2'))
b_12.place(x=75, y=174)

b_13 = Button(frame_corpo, text="3", width=9, height=3, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('3'))
b_13.place(x=149, y=174)

b_14 = Button(frame_corpo, text="+", width=9, height=3, bg=cor5, fg=cor2, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('+'))
b_14.place(x=230, y=174)

b_1 = Button(frame_corpo, text="0", width=15, height=3, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('0'))
b_1.place(x=0, y=232)

b_2 = Button(frame_corpo, text=".", width=9, height=3, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrar_valores('.'))
b_2.place(x=149, y=232)

b_3 = Button(frame_corpo, text="=", width=9, height=3, bg=cor5, fg=cor2, font=('sans 13 bold'), relief=RAISED, overrelief=RIDGE, command= calcular)
b_3.place(x=230, y=232)




janela.mainloop()