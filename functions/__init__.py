import sqlite3

connect = sqlite3.connect("./data/clientes.db")
cursor = connect.cursor()

def addPizzarias(cnpj, nome, rua, bairro, numero):
   cursor.execute('''
   INSERT INTO Pizzarias (cnpj, nome, rua, bairro, numero)
   VALUES (?, ?, ?, ?, ?)
   ''', (cnpj, nome, rua, bairro, numero))
   connect.commit()
   print("Pizzaria adicionada com sucesso!")

def addFuncionarios(idade, nome, numero, especializacao):
   counter = 1
   autoIncrementFuncionarios = showFuncionarios("no")
   for elements in autoIncrementFuncionarios:
      counter+=1

   for cnpjs in autoIncrementFuncionarios:
      if (cnpjs[0] == counter):
         counter += 1

   cursor.execute('''
   INSERT INTO Funcionarios (numeroDeContrato, idade, nome, numero, especializacao)
   VALUES (?, ?, ?, ?, ?)
   ''', (counter, idade, nome, numero, especializacao))
   connect.commit()
   print("Funcionário adicionado com sucesso!")

def addPizzas(sabor, tempoDePreparo, preco, tamanhoDaPizza, tipoDaPizza):
   cursor.execute('''
   INSERT INTO Pizzas (sabor, tempoDePreparo, preco, tamanhoDaPizza, tipoDaPizza)
   VALUES (?, ?, ?, ?, ?)
   ''', (sabor, tempoDePreparo, preco, tamanhoDaPizza, tipoDaPizza))
   connect.commit()
   print("Pizza adicionada com sucesso!")

def addClientes(pedido, formaDePagamento, valorDaConta):
   counter = 1
   autoIncrementClients = showClientes("no")
   for elements in autoIncrementClients:
      counter+=1

   for sabores in autoIncrementClients:
      if (sabores[0] == counter):
         counter += 1

   cursor.execute('''
   INSERT INTO Clientes (id, pedido, formaDePagamento, valorDaConta)
   VALUES (?, ?, ?, ?)
   ''', (counter, pedido, formaDePagamento, valorDaConta))
   connect.commit()
   print("Cliente registrado com sucesso!")

def showPizzarias(show):
   cursor.execute('SELECT * FROM Pizzarias')
   pizzarias = cursor.fetchall()
   if (show == "yes"):
      for pizzaria in pizzarias:
         print("\033[1;30mCNPJ: \033[1;36m{} \033[1;30mNome: \033[1;36m{} \033[1;30mRua: \033[1;36m{} \033[1;30mBairro: \033[1;36m{} \033[1;30mNúmero de Residência: \033[1;36m{}".format(
             pizzaria[0], pizzaria[1], pizzaria[2], pizzaria[3], pizzaria[4]))
   else:
      return pizzarias

def showFuncionarios(show):
   cursor.execute('SELECT * FROM Funcionarios')
   funcionarios = cursor.fetchall()
   if (show == "yes"):
      for funcionario in funcionarios:
         print("\033[1;30mNúmero de Contrato: \033[1;36m{} \033[1;30mIdade: \033[1;36m{} \033[1;30mNome: \033[1;36m{} \033[1;30mNúmero: \033[1;36m{} \033[1;30mEspecialização: \033[1;36m{}".format(
             funcionario[0], funcionario[1], funcionario[2], funcionario[3], funcionario[4]))
   else:
      return funcionarios

def showPizzas(show):
   cursor.execute('SELECT * FROM Pizzas')
   pizzas = cursor.fetchall()
   if (show == "yes"):
      for pizza in pizzas:
         print("\033[1;30mSabor: \033[1;36m{} \033[1;30mTempo de Preparo: \033[1;36m{} \033[1;30mPreço: \033[1;36m{} \033[1;30mTamanho da Pizza: \033[1;36m{} \033[1;30mTipo da Pizza: \033[1;36m{}".format(
             pizza[0], pizza[1], pizza[2], pizza[3], pizza[4]))
   else:
      return pizzas

def showClientes(show):
   cursor.execute('SELECT * FROM Clientes')
   clientes = cursor.fetchall()
   if (show == "yes"):
      for cliente in clientes:
         print("\033[1;30mID: \033[1;36m{} \033[1;30mPedido: \033[1;36m{} \033[1;30mForma de Pagamento: \033[1;36m{} \033[1;30mValor da Conta: \033[1;36m{} \033[1;30m".format(
             cliente[0], cliente[1], cliente[2], cliente[3]))
   else:
      return clientes

def updatePizzarias(cnpj, nome, rua, bairro, numero):
   cursor.execute('''
   UPDATE Pizzarias
   SET nome = ?, rua = ?, bairro = ?, numero = ?
   WHERE cnpj = ?
   ''', (nome, rua, bairro, numero, cnpj))
   connect.commit()
   print("Pizzaria atualizada com sucesso!")

def updateFuncionarios(numeroDeContrato, idade, nome, numero, especializacao):
   cursor.execute('''
   UPDATE Funcionarios
   SET idade = ?, nome = ?, numero = ?, especializacao = ?
   WHERE numeroDeContrato = ?
   ''', (idade, nome, numero, especializacao, numeroDeContrato))
   connect.commit()
   print("Funcionario atualizado com sucesso!")

def updatePizzas(sabor, tempoDePreparo, preco, tamanhoDaPizza, tipoDaPizza):
   cursor.execute('''
   UPDATE Pizzas
   SET tempoDePreparo = ?, preco = ?, tamanhoDaPizza = ?, tipoDaPizza = ?
   WHERE sabor = ?
   ''', (tempoDePreparo, preco, tamanhoDaPizza, tipoDaPizza, sabor))
   connect.commit()
   print("Pizza atualizada com sucesso!")

def updateClientes(id, pedido, formaDePagamento, valorDaConta):
   cursor.execute('''
   UPDATE Clientes
   SET pedido = ?, formaDePagamento = ?, valorDaConta = ?
   WHERE id = ?
   ''', (pedido, formaDePagamento, valorDaConta, id))
   connect.commit()
   print("Cliente atualizado com sucesso!")

def deletePizzarias(cnpj):
   cursor.execute('''
   DELETE FROM Pizzarias
   WHERE cnpj = ?
   ''', (cnpj,))
   connect.commit()
   print("Pizzaria deletada com sucesso!")
   
def deleteFuncionarios(numeroDeContrato):
   cursor.execute('''
   DELETE FROM Funcionarios
   WHERE numeroDeContrato = ?
   ''', (numeroDeContrato,))
   connect.commit()
   print("Funcionario deletado com sucesso!")
   
def deletePizzas(sabor):
   cursor.execute('''
   DELETE FROM Pizzas
   WHERE sabor = ?
   ''', (sabor,))
   connect.commit()
   print("Pizza deletada com sucesso!")
   
def deleteClientes(id):
   cursor.execute('''
   DELETE FROM Clientes
   WHERE id = ?
   ''', (id,))
   connect.commit()
   print("Cliente deletado com sucesso!")

def closeData():
   connect.close()