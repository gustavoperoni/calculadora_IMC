import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        nome = entrada_nome.get()
        peso = float(entrada_peso.get())
        altura_cm = float(entrada_altura.get())
        altura_m = altura_cm / 100  # converter para metros

        imc = peso / (altura_m ** 2)
        resultado = f"{nome}, seu IMC é: {imc:.2f}\n"

        # Determina a classificação e cor
        if imc < 18.5:
            classificacao = "Abaixo do peso"
            cor = "blue"
        elif imc < 25:
            classificacao = "Peso normal"
            cor = "green"
        elif imc < 30:
            classificacao = "Sobrepeso"
            cor = "orange"
        elif imc < 35:
            classificacao = "Obesidade grau 1"
            cor = "orange"
        elif imc < 40:
            classificacao = "Obesidade grau 2"
            cor = "red"
        else:
            classificacao = "Obesidade grau 3 (mórbida)"
            cor = "red"

        resultado += f"Classificação: {classificacao}"
        label_resultado.config(text=resultado, fg=cor)

        # Alerta se IMC for acima de 30
        if imc >= 30:
            messagebox.showwarning("Atenção!", f"{nome}, seu IMC indica obesidade.\nConsidere procurar um profissional de saúde.")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("320x370")
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="Calculadora de IMC", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Entrada de nome
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

# Entrada de peso
label_peso = tk.Label(janela, text="Peso (kg):")
label_peso.pack()
entrada_peso = tk.Entry(janela)
entrada_peso.pack()

# Entrada de altura
label_altura = tk.Label(janela, text="Altura (cm):")
label_altura.pack()
entrada_altura = tk.Entry(janela)
entrada_altura.pack()

# Botão de calcular
botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

# Iniciar a aplicação
janela.mainloop()
