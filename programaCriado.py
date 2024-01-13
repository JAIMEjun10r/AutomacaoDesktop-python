import tkinter as tk
from tkinter import messagebox

def limpar_campos():
    entry_empresa.delete(0, tk.END)
    entry_produto.delete(0, tk.END)
    entry_serial.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_valor.delete(0, tk.END)

def mostrar_alerta():
    messagebox.showinfo("Cadastro", "Os dados foram cadastrados!")
    limpar_campos()

# Criar janela principal
janela = tk.Tk()
janela.title("Java Lixo")
# janela.geometry('300x300')
janela_width = 300
janela_height = 300

# Definir manualmente as coordenadas de abertura da janela
x = 500
y = 200

janela.geometry(f'{janela_width}x{janela_height}+{x}+{y}')

# Criar e posicionar os widgets
tk.Label(janela, text="Empresa:").grid(row=0, column=0, padx=10, pady=5)
entry_empresa = tk.Entry(janela)
entry_empresa.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Produto:").grid(row=1, column=0, padx=10, pady=5)
entry_produto = tk.Entry(janela)
entry_produto.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Serial:").grid(row=2, column=0, padx=10, pady=5)
entry_serial = tk.Entry(janela)
entry_serial.grid(row=2, column=1, padx=10, pady=5)

tk.Label(janela, text="Quantidade:").grid(row=3, column=0, padx=10, pady=5)
entry_quantidade = tk.Entry(janela)
entry_quantidade.grid(row=3, column=1, padx=10, pady=5)

tk.Label(janela, text="Valor:").grid(row=4, column=0, padx=10, pady=5)
entry_valor = tk.Entry(janela)
entry_valor.grid(row=4, column=1, padx=10, pady=5)

# Botão Cadastrar centralizado e com tamanho reduzido
tk.Button(janela, text="Cadastrar", command=mostrar_alerta, width=10, height=2).grid(row=5, column=1, columnspan=1, pady=5)

# Configurar a última linha para expandir e preencher o espaço verticalmente
janela.grid_rowconfigure(5, weight=1)

# Configurar a última coluna para expandir e preencher o espaço horizontalmente
janela.grid_columnconfigure(1, weight=1)

# Iniciar o loop principal da interface gráfica
janela.mainloop()