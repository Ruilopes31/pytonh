import customtkinter as ctk

#Função de execução -------

def calcular():
    try:
        d = int(distancia.get())
        c = int(consumo.get())
        p = float(combustivel.get())
        
        gasto = (d/c)*p
        
        resultado.configure(text=f'O gasto será de R${gasto:.2f}')
    except:
        resultado.configure(text=f' ⚠️ Digite Valores Válidos !! ⚠️ ')


#---------------------------
# aqui comeca a janela --
ctk.set_appearance_mode('dark')
janela = ctk.CTk()
janela.geometry('600x450')
janela.resizable(False,False)

# Titulo ---

ctk.CTkLabel(janela,
             text='APP VIAGEM',
             font=('Arial',40,'bold'),
             text_color='lightblue',
             ).pack(pady=15)

# 1º Campo: distância

distancia = ctk.CTkEntry(janela,
                         placeholder_text='Digite a distância da viagem em KM',
                         width=300,
                         height=30,
                         border_color='lightblue',
                         border_width=3)
distancia.pack(pady=20)

# 2º Campo: Consumo

consumo = ctk.CTkEntry(janela,
                       placeholder_text='Digite o consumo do seu veículo',
                       width=300,
                       height=30,
                       border_color='lightblue',
                       border_width=3)
consumo.pack(pady=20)

# 3º Campo: Preço do Combustivel

combustivel = ctk.CTkEntry(janela,
                           placeholder_text='Digite o preço atual do combustivel',
                           width=300,
                           height=30,
                           border_color='lightblue',
                           border_width=3)
combustivel.pack(pady=20)

# Botão -------------

botao = ctk.CTkButton(janela,
                      text='Calcular Gasto',
                      fg_color='white',
                      text_color='darkblue',
                      border_color='red',
                      border_width=2,
                      width=180,
                      height=40,
                      hover_color='red',
                      cursor='hand2',
                      command=calcular)
botao.pack(pady=20)

# Local do resultado

resultado = ctk.CTkLabel(janela,
                         text='',
                         text_color='yellow',
                         font=('Arial',30))
resultado.pack(pady=20)




janela.mainloop()