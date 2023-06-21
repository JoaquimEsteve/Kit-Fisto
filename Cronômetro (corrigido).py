import time
import tkinter as tk

def atualizar_cronometro():
    global pararcro
    agora = time.time() - inicio
    
    horas = int(agora / 3600)
    minutos = int((agora % 3600) / 60)
    segundos = int(agora % 60)
    
    tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    label.configure(text=tempo_formatado)
    pararcro = label.after(1000, atualizar_cronometro) #No arquivo original, o cronômetro não parava após clicar no botão "parar", porém, após utilizar uma variável, nesse caso, "pararcro", e a substituir novamente abaixo...

def iniciar_cronometro():
    global inicio
    inicio = time.time()
    atualizar_cronometro()

def parar_cronometro():
    label.after_cancel(pararcro) #A função "parar" do cronograma passa a funcionar após colocar a nova variável, agora global, nesta linha de código.

# Criação da janela
janela = tk.Tk()
janela.title("Cronômetro")

# Criação do rótulo para exibir o tempo
label = tk.Label(janela, text="00:00:00", font=("Arial", 24), pady=10)
label.pack()

# Criação dos botões de início e parada do cronômetro
btn_iniciar = tk.Button(janela, text="Iniciar", command=iniciar_cronometro)
btn_iniciar.pack(side=tk.LEFT, padx=10)

btn_parar = tk.Button(janela, text="Parar", command=parar_cronometro)
btn_parar.pack(side=tk.RIGHT, padx=10)

# Execução da janela
janela.mainloop()
