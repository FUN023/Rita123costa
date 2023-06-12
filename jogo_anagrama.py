import json
import random
import textwrap
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
 
def close_window():
    root.destroy()
 
root = tk.Tk()
root.geometry("800x400")
root.title("Jogo do anagrama")
root.configure(background="light blue")
 

welcome_label = tk.Label(root, text="\n Bem-vindo jogo do anagrama! \n \n Regras do jogo : ",bg="light blue",font=("Gotham",15, "bold" ))

welcome_label.pack(anchor="center", expand=True)

welcome_label2 = tk.Label(root, text="1. Adivinhar palavra que se encontra baralhada em inglês \n 2. Se acertar, pontuação aumenta 1 \n 3. Existem 3 tentativas \n 4. Se não acertar, perde uma tentativa \n 5. Para acabar clique FIM \n 6. Para continuar clique NOVO JOGO \n",bg="light blue",font=("Gotham", 15))

welcome_label2.pack(anchor="center", expand=True)
 
 
close_button = tk.Button(root, text=" INICIAR JOGO ", command=close_window,bg="pink",font=("Gotham", 14))
 
close_button.pack(anchor="center", expand=True)
 
root.mainloop()
 
 
root = tk.Tk()
root.geometry("1200x500")
root.title("Jogo do anagrama")
root.configure(background="light blue")
 
 
input_box = tk.Entry(root)
    
file= open("dictionary.json")
data = json.load(file)
 
pals=list(data.keys())
contador=3
pontuacao=0
palavra=""
palavra_modificada=""
            
def sair_jogo():
    messagebox.showinfo("Sair",f"Pontuação obtida: {pontuacao}")
    exit()
            
       
def regras_jogo():
    messagebox.showinfo("Regras","\n Bem-vindo ao programa! \n \n Regras do jogo : \n 1- Adivinhar palavra que se encontra baralhada em inglês \n 2- Se acertar, pontuação aumenta 1 \n 3- Tem 3 tentativas \n 4- Se não acertar, perde uma tentativa \n 5- Para sair do jogo clique FIM \n 6- Para continuar clique NOVO JOGO \n \n")
    
def clear_window(window):
       # Destroy all widgets within the window
    for widget in window.winfo_children():
        widget.destroy()
        
def novo_jogo():
    global contador
    global palavra
    global palavra_modificada
    global input_box
    global pontuacao
    
    clear_window(root)
    root.geometry("1200x500")
    root.title("Jogo do anagrama")
    root.state("zoomed")

    frame2 = tk.Frame(root, borderwidth=2, bg="light blue",width=200, height=150)
    frame2.grid(row=0, column=0, sticky="nsew")

    
    input_box = tk.Entry(frame2)
    input_label=tk.Entry(root)
    
    titulo_pontuacao=f"Pontuação: {pontuacao}"
    
    input_pontuacao=tk.Entry(frame2)
    input_pontuacao=tk.Label(frame2, text=titulo_pontuacao,anchor=tk.W,bg="light blue", font=("Gotham", 12), fg="dark red")
    input_pontuacao.grid(row=1, column=0)
    
    
    input_box.grid(row=9, column=0)
    button = tk.Button(frame2, text="Novo Jogo", command=novo_jogo,bg="pink", highlightthickness=0, cursor="hand2")
    button.grid(row=14, column=0, columnspan=2)
    
    buttonsair = tk.Button(frame2, text="Sair", command=sair_jogo,bg="pink",highlightthickness=0, cursor="hand2")
    buttonsair.grid(row=14, column=4, columnspan=2)
    
    buttonregras = tk.Button(frame2, text="Regras do Jogo", command=regras_jogo,bg="pink",highlightthickness=0, cursor="hand2")
    buttonregras.grid(row=14, column=2, columnspan=2)
    
        
    input_box.focus()
    input_box.bind("<Return>", get_input)
 
    palavra=random.choice(pals)
    palavra_modificada = list(palavra)
    random.shuffle(palavra_modificada) 
    palavra_baralhada = "".join(palavra_modificada)
 
    
    titulo=f"ADIVINHE A PALAVRA: \n \n {palavra_baralhada}\n \n"
     
    titulo2="Significado: "
    
    varias_linhas=textwrap.wrap(data[palavra], width=100)
    for linha in varias_linhas:
        titulo2+=linha+"\n"
        
    titulo+=titulo2
    input_label = tk.Label(frame2, text=titulo,anchor=tk.W,bg="light blue",font=("Gotham", 13,))
    input_label.grid(row=0, column=0)
 
    input_label.grid(row=0, column=0, sticky="nsew")
    frame2.grid_rowconfigure(0, weight=1)
    frame2.grid_columnconfigure(0, weight=1)
 
 
    contador=3
 
def clear_entry():
    input_box.delete(0, tk.END)
    
def get_input(event=None):
    global contador
    global palavra
    global pontuacao
     
    contador-=1
    resposta = input_box.get()
    
    
    clear_entry()
    
    if resposta == palavra and len(resposta)>0:
        messagebox.showinfo("Resultado","ACERTOU!")
        pontuacao+=1
        novo_jogo()
    else:
        messagebox.showinfo("Resultado",f"NÃO ACERTOU! Tentativas restantes: {contador}")
    if contador<=0:
        resultado = messagebox.askyesno(f"Novo jogo"," Fazer novo jogo?")
        if resultado:
            contador=3
            novo_jogo()
        else:
            messagebox.showinfo("Sair",f"Pontuação obtida: {pontuacao}")
            exit()
           
 
novo_jogo()
