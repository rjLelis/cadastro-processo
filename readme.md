# Implementar uma aplicação usando Django. 

1. Criar uma App Django contendo um modelo chamado `Processo`, com os seguintes atributos: 

* pasta (String) 
* comarca (String) 
* uf (String) 

2. Criar uma segunda App Django chamada `cadastro_processo` contendo um modelo chamado `Planilha`, com os seguintes atributos: 

* nome (String) 
* cliente (String) 
* arquivo (FileField) 

3. Com a App cadastro_processo criada, criar uma ação Django, que ao uma inserir uma planilha .csv que será disponibilizada (contendo processos com informações de pasta, comarca, uf) no modelo Planilha, cadastrar cada linha do .csv no modelo Processo. 
