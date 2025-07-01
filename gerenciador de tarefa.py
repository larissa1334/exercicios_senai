import os

tarefas={'tarefa:','lavar roupa:','lavar louça:','limpar o quarto:'
      'data:','01/07:','02/07:','03/07:'
 }
def mostrar_tarefas():
    barra=f'|{"-" * 30}|'
    print (barra)
    print('|tarefas:') 
    for i in range (len(tarefas['tarefas'])):
       print(f"| {i + 1}.{tarefas['tarefa'][i]} - data:{tarefas ['data'][i]}")
    print(barra)

def adicionar_tarefas():
    tarefa= input('digite o nome da tarefa:')
    data=input (' | digite a data :')
    tarefas['tarefas'].append(tarefas)
    tarefas['datas'].append(data)
    print('|tarefa adicionada com sucesso')

def remover_tarefa():
    mostrar_tarefas()
   