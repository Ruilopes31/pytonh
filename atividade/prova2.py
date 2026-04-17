import customtkinter as ctk
from tkinter import messagebox


def calcular():
    try:
        n1 = float(nota1.get())
        n2 = float(nota2.get())
        n3 = float(nota3.get())

        media = (n1 + n2 + n3)/3

        if media >= 5:
            situacao = "Aprovado(a)"
            cor_texto = "#2ecc71"  # Verde
        else:
            situacao = "Em Recuperação"
            cor_texto = "#e74c3c"  # Vermelho

        resultado.configure(text=f'Média: {media:.1f} - {situacao}', text_color=cor_texto)
    except ValueError:
        messagebox.showerror('ERRO', 'Por favor, preencha todos os campos corretamente com números!')


ctk.set_appearance_mode('light')
janela = ctk.CTk()
janela.geometry('600x400')
janela.resizable(False,False)

ctk.CTkLabel(janela,
             text='APP ESCOLAR',
             font=('Arial',40,'bold'),
             text_color='darkblue',
             ).pack(pady=20)

nota1 = ctk.CTkEntry(janela,
                         placeholder_text='Digite a nota da 1ª unidade',
                         width=300,
                         height=35,
                         border_color='darkblue',
                         border_width=2)
nota1.pack(pady=10)

nota2 = ctk.CTkEntry(janela,
                       placeholder_text='Digite a nota da 2ª unidade',
                       width=300,
                       height=35,
                       border_color='darkblue',
                       text_color='#4d4d4d',
                       border_width=2)
nota2.pack(pady=10)


nota3 = ctk.CTkEntry(janela,
                           placeholder_text='Digite a nota da 3ª unidade',
                           width=300,
                           height=35,
                           border_color='darkblue',
                           text_color='#4d4d4d',
                           border_width=2)
nota3.pack(pady=10)


botao = ctk.CTkButton(janela,
                      text='resultado',
                      fg_color='white',
                      text_color='#4d4d4d',
                      border_color='darkblue',
                      border_width=2,
                      width=150,
                      height=35,
                      hover_color='#e0e0e0',
                      cursor='hand2',
                      command=calcular)
botao.pack(pady=15)

resultado = ctk.CTkLabel(janela,
                         text='',
                         font=('Arial',24,'bold'))
resultado.pack(pady=10)

janela.mainloop()