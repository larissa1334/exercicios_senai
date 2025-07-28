import os

tarefas={'tarefa:','lavar roupa:','lavar louça:','limpar o quarto:'
      'data:','01/07:','02/07:','03/07:'
 }
def mosrtrar_tarefas():
    for i in range (len(tarefas['tarefas'])):
        print (f'{i+1}.{tarefas['tarefas'[i]]} datas: {tarefas['datas'][i]}')
        