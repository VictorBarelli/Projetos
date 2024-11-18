import tkinter as tk
from tkinter import messagebox

class EnergyCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Consumo Energético")

        self.aparelhos = []
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Nome do Aparelho").grid(row=0, column=0)
        tk.Label(self.root, text="Potência (W)").grid(row=0, column=1)
        tk.Label(self.root, text="Horas de Uso por Dia").grid(row=0, column=2)

        self.nome_aparelho = tk.Entry(self.root)
        self.nome_aparelho.grid(row=1, column=0)

        self.potencia_aparelho = tk.Entry(self.root)
        self.potencia_aparelho.grid(row=1, column=1)

        self.horas_aparelho = tk.Entry(self.root)
        self.horas_aparelho.grid(row=1, column=2)

        tk.Button(self.root, text="Adicionar Aparelho", command=self.adicionar_aparelho).grid(row=1, column=3)
        tk.Button(self.root, text="Calcular Consumo", command=self.calcular_consumo).grid(row=2, column=0, columnspan=4)

    def adicionar_aparelho(self):
        nome = self.nome_aparelho.get()
        potencia = self.potencia_aparelho.get()
        horas = self.horas_aparelho.get()

        if nome and potencia and horas:
            self.aparelhos.append({'nome': nome, 'potencia': float(potencia), 'horas': float(horas)})
            self.nome_aparelho.delete(0, tk.END)
            self.potencia_aparelho.delete(0, tk.END)
            self.horas_aparelho.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")

    def calcular_consumo(self):
        consumo_total = sum([aparelho['potencia'] * aparelho['horas'] for aparelho in self.aparelhos])
        mensagem = f"Consumo total: {consumo_total:.2f} Wh/dia\n"
        
        if consumo_total <= 300:
            mensagem += "Recomendação: Instalar painéis solares."
        elif consumo_total <= 1000:
            mensagem += "Recomendação: Combinação de painéis solares e turbina eólica pequena."
        else:
            mensagem += "Recomendação: Sistema híbrido com painéis solares, turbina eólica e baterias de armazenamento."

        messagebox.showinfo("Resultado", mensagem)

if __name__ == "__main__":
    root = tk.Tk()
    app = EnergyCalculatorApp(root)
    root.mainloop()
