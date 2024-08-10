# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:00:42 2024

@author: André Luis
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import DateEntry

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lorrane Nail Designer")
        self.root.geometry("800x600")
        self.clientes = []
        self.agendamentos = []
        self.criar_widgets()

    def criar_widgets(self):
        self.tabControl = ttk.Notebook(self.root)

        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text='Cadastro de Cliente')
        self.tabControl.add(self.tab2, text='Agendamento')

        self.tabControl.pack(expand=1, fill="both")

        self.criar_aba_cliente()
        self.criar_aba_agendamento()
        self.carregar_clientes()

    def criar_aba_cliente(self):
        lbl_nome = ttk.Label(self.tab1, text="Nome:")
        lbl_nome.grid(column=0, row=0, padx=10, pady=10)

        self.nome_cliente = ttk.Entry(self.tab1, width=30)
        self.nome_cliente.grid(column=1, row=0, padx=10, pady=10)

        lbl_telefone = ttk.Label(self.tab1, text="Telefone:")
        lbl_telefone.grid(column=0, row=1, padx=10, pady=10)

        self.telefone_cliente = ttk.Entry(self.tab1, width=30)
        self.telefone_cliente.grid(column=1, row=1, padx=10, pady=10)

        btn_salvar_cliente = ttk.Button(self.tab1, text="Salvar Cliente", command=self.salvar_cliente)
        btn_salvar_cliente.grid(column=1, row=2, padx=10, pady=10)

        btn_editar_cliente = ttk.Button(self.tab1, text="Alterar Cliente", command=self.editar_cliente)
        btn_editar_cliente.grid(column=1, row=3, padx=10, pady=10)

        lbl_lista_clientes = ttk.Label(self.tab1, text="Clientes Cadastrados:")
        lbl_lista_clientes.grid(column=0, row=4, padx=10, pady=10)

        self.lista_clientes = tk.Listbox(self.tab1, width=50)
        self.lista_clientes.grid(column=1, row=4, padx=10, pady=10)
        self.lista_clientes.bind("<<ListboxSelect>>", self.selecionar_cliente)

    def criar_aba_agendamento(self):
        lbl_cliente = ttk.Label(self.tab2, text="Cliente:")
        lbl_cliente.grid(column=0, row=0, padx=10, pady=10)

        self.combobox_cliente_agendamento = ttk.Combobox(self.tab2, width=28)
        self.combobox_cliente_agendamento.grid(column=1, row=0, padx=10, pady=10)

        lbl_data = ttk.Label(self.tab2, text="Data:")
        lbl_data.grid(column=0, row=1, padx=10, pady=10)

        self.data_agendamento = DateEntry(self.tab2, width=28, background='darkblue', foreground='white', borderwidth=2)
        self.data_agendamento.grid(column=1, row=1, padx=10, pady=10)

        lbl_hora = ttk.Label(self.tab2, text="Hora:")
        lbl_hora.grid(column=0, row=2, padx=10, pady=10)

        frame_hora = ttk.Frame(self.tab2)
        frame_hora.grid(column=1, row=2, padx=120, pady=10, sticky='w')

        self.combobox_hora = ttk.Combobox(frame_hora, values=[f"{i:02}" for i in range(24)], width=5)
        self.combobox_hora.grid(column=0, row=0, padx=0, pady=0)
        self.combobox_hora.set('00')  

        self.combobox_minuto = ttk.Combobox(frame_hora, values=[f"{i:02}" for i in range(60)], width=5)
        self.combobox_minuto.grid(column=1, row=0, padx=0, pady=0)
        self.combobox_minuto.set('00') 

        lbl_servico = ttk.Label(self.tab2, text="Escolha de Serviço:")
        lbl_servico.grid(column=0, row=3, padx=10, pady=10)

        self.nome_servico = ttk.Entry(self.tab2, width=30)
        self.nome_servico.grid(column=1, row=3, padx=10, pady=10)

        lbl_valor_servico = ttk.Label(self.tab2, text="Valor:")
        lbl_valor_servico.grid(column=0, row=4, padx=10, pady=10)

        self.valor_servico = ttk.Entry(self.tab2, width=30)
        self.valor_servico.grid(column=1, row=4, padx=10, pady=10)

        btn_salvar_agendamento = ttk.Button(self.tab2, text="Salvar Agendamento", command=self.salvar_agendamento)
        btn_salvar_agendamento.grid(column=1, row=5, padx=10, pady=10)

        btn_editar_agendamento = ttk.Button(self.tab2, text="Alterar Agendamento", command=self.editar_agendamento)
        btn_editar_agendamento.grid(column=1, row=6, padx=10, pady=10)

        lbl_pesquisar = ttk.Label(self.tab2, text="Pesquisar Agendamentos do Dia:")
        lbl_pesquisar.grid(column=0, row=7, padx=10, pady=10)

        self.pesquisa_data = DateEntry(self.tab2, width=30, background='darkblue', foreground='white', borderwidth=2)
        self.pesquisa_data.grid(column=1, row=7, padx=10, pady=10)
        self.pesquisa_data.set_date(datetime.today())  # Preenche com a data de hoje

        btn_pesquisar_agendamento = ttk.Button(self.tab2, text="Pesquisar", command=self.pesquisar_agendamento)
        btn_pesquisar_agendamento.grid(column=1, row=8, padx=10, pady=10)

        self.resultados_pesquisa = tk.Text(self.tab2, height=10, width=50)
        self.resultados_pesquisa.grid(column=1, row=9, padx=10, pady=10)

    def salvar_cliente(self):
        nome = self.nome_cliente.get()
        telefone = self.telefone_cliente.get()
        if nome and telefone:
            self.clientes.append({'nome': nome, 'telefone': telefone})
            self.salvar_clientes()
            self.carregar_clientes()
            messagebox.showinfo("Cadastro de Cliente", f"Cliente {nome} salvo com sucesso!")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    def editar_cliente(self):
        indice_cliente_selecionado = self.lista_clientes.curselection()
        if indice_cliente_selecionado:
            indice_cliente_selecionado = indice_cliente_selecionado[0]
            cliente = self.clientes[indice_cliente_selecionado]
            self.nome_cliente.delete(0, tk.END)
            self.nome_cliente.insert(0, cliente['nome'])
            self.telefone_cliente.delete(0, tk.END)
            self.telefone_cliente.insert(0, cliente['telefone'])
            self.clientes.pop(indice_cliente_selecionado)
            self.salvar_clientes()
            self.carregar_clientes()

    def salvar_agendamento(self):
        cliente = self.combobox_cliente_agendamento.get()
        data = self.data_agendamento.get_date().strftime('%d-%m-%Y')  # Obtém a data no formato desejado
        hora = f"{self.combobox_hora.get()}:{self.combobox_minuto.get()}"  # Obtém a hora e minuto selecionados
        nome_servico = self.nome_servico.get()
        valor_servico = self.valor_servico.get()
        if cliente and data and hora and nome_servico and valor_servico:
            self.agendamentos.append({'cliente': cliente, 'data': data, 'hora': hora, 'nome_servico': nome_servico, 'valor_servico': valor_servico})
            self.salvar_agendamentos()
            self.carregar_agendamentos()
            messagebox.showinfo("Agendamento", f"Agendamento para {cliente} em {data} às {hora} salvo com sucesso!")
        else:
            messagebox.showwarning("Erro", "Favor preencha todos os campos.")

    def editar_agendamento(self):
        indice_agendamento_selecionado = self.resultados_pesquisa.get('1.0', tk.END).splitlines().index(self.resultados_pesquisa.get('1.0', tk.END).strip()) - 1
        if indice_agendamento_selecionado >= 0:
            agendamento = self.agendamentos[indice_agendamento_selecionado]
            self.combobox_cliente_agendamento.set(agendamento['cliente'])
            self.data_agendamento.set_date(datetime.strptime(agendamento['date'], '%d-%m-%Y'))  # Define a data
            self.combobox_hora.set(agendamento['time'].split(':')[0])  # Define a hora
            self.combobox_minuto.set(agendamento['time'].split(':')[1])  # Define os minutos
            self.nome_servico.delete(0, tk.END)
            self.nome_servico.insert(0, agendamento['nome_servico'])
            self.valor_servico.delete(0, tk.END)
            self.valor_servico.insert(0, agendamento['valor_servico'])
            self.agendamentos.pop(indice_agendamento_selecionado)
            self.salvar_agendamentos()
            self.carregar_agendamentos()

    def pesquisar_agendamento(self):
        data_pesquisa = self.pesquisa_data.get_date().strftime('%d-%m-%Y')
        resultados = f"Resultados de agendamentos para {data_pesquisa}:\n"
        for index, agendamento in enumerate(self.agendamentos):
            if agendamento['data'] == data_pesquisa:
                resultados += f"- Cliente: {agendamento['cliente']}, Data: {agendamento['data']}, Hora: {agendamento['hora']}, Serviço: {agendamento['nome_servico']}, Valor: {agendamento['valor_servico']}\n"
        self.resultados_pesquisa.delete('1.0', tk.END)
        self.resultados_pesquisa.insert(tk.END, resultados)

    def selecionar_cliente(self, event):
        indice_cliente_selecionado = self.lista_clientes.curselection()
        if indice_cliente_selecionado:
            indice_cliente_selecionado = indice_cliente_selecionado[0]
            cliente = self.clientes[indice_cliente_selecionado]
            self.nome_cliente.delete(0, tk.END)
            self.nome_cliente.insert(0, cliente['nome'])
            self.telefone_cliente.delete(0, tk.END)
            self.telefone_cliente.insert(0, cliente['telefone'])

    def carregar_clientes(self):
        self.lista_clientes.delete(0, tk.END)
        for cliente in self.clientes:
            self.lista_clientes.insert(tk.END, f"{cliente['nome']} - {cliente['telefone']}")
        self.combobox_cliente_agendamento['values'] = [cliente['nome'] for cliente in self.clientes]

    def carregar_agendamentos(self):
        pass

    def salvar_clientes(self):
        pass

    def salvar_agendamentos(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
