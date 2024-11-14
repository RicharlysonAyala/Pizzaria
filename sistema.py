# Chamando as funções
import functions
import design

# Variaveis controladoras das opções
tableOption = 0
functionOption = 0

while (tableOption != 5):
    # Menu de opções
    design.menu(['\033[1;36mPizzarias', '\033[1;32mFuncionarios', 
                 '\033[1;33mPizzas', '\033[1;35mClientes', '\033[1;31mSair do Sistema'])
    tableOption = int(input("Selecione uma das opções: "))

    # impede que o usuario digite uma opção invalida
    while (tableOption > 5 or tableOption <= 0):
        tableOption = int(input("Selecione apenas opções contidas na tabela: "))
    
    while (tableOption != 5):

        # opção Pizzarias
        if (tableOption == 1):
            # Menu de opções
            design.menu(['\033[1;36mExibir', '\033[1;32mAdicionar', 
                    '\033[1;33mAtualizar', '\033[1;31mDeletar', '\033[1;35mVoltar'])
            functionOption = int(input("Selecione qual função deseja utilizar: "))

            # impede que o usuario digite uma opção invalida
            while(functionOption > 5 or functionOption <= 0):
                functionOption = int(input("Selecione apenas opções contidas na tabela: "))

            # Exibir
            if (functionOption == 1):
                functions.showPizzarias("yes")

            # Adicionar
            elif (functionOption == 2):
                print(design.line())

                cnpj = input("\033[1;30mDigite o \033[1;32mCNPJ \033[1;30mda pizzaria para \033[1;32madicionar-la: ")

                allPizzarias = functions.showPizzarias("no")
                for cnpjs in allPizzarias:
                    if (cnpj == cnpjs[0]):
                        cnpj = input("\033[1;31mCNPJ JA CADASTRADO! \033[1;30mDigite outro \033[1;32mCNPJ \033[1;30mnão cadastrado para \033[1;32madicionar-lo: ")

                nome = input("\033[1;30mDigite o \033[1;32mNome \033[1;30mda pizzaria para \033[1;32madicionar-la: ")
                rua = input("\033[1;30mDigite a \033[1;32mRua \033[1;30mda pizzaria para \033[1;32madicionar-la: ")
                bairro = input("\033[1;30mDigite o \033[1;32mBairro \033[1;30mda pizzaria para \033[1;32madicionar-la: ")
                try:
                    numero = int(input("\033[1;30mDigite o \033[1;32mNúmero de Residência \033[1;30mda pizzaria para \033[1;32madicionar-la: "))
                except:
                    numero = int(input("\033[1;30mDigite o \033[1;31mNúmero \033[1;32mde Residência \033[1;30mda pizzaria para \033[1;32madicionar-la: "))
                functions.addPizzarias(cnpj, nome, rua, bairro, numero)

            # Atualizar
            elif (functionOption == 3):
                cnpj = input("\033[1;30mDigite o \033[1;33mCNPJ \033[1;30mda pizzaria que deseja \033[1;33matualizar: ")
                trueCNPJ = False

                while (not trueCNPJ):
                    allPizzarias = functions.showPizzarias("no")
                    for cnpjs in allPizzarias:
                        if (cnpj == cnpjs[0]):
                            trueCNPJ = True
                    if(trueCNPJ == False):
                        cnpj = input("\033[1;31mCNPJ NÃO ENCONTRADO! \033[1;30mDigite outro \033[1;33mCNPJ \033[1;30mcadastrado para \033[1;33matualizar-lo: ")

                nome = input("\033[1;33mNovo nome: ")
                rua = input("\033[1;33mNova rua: ")
                bairro = input("\033[1;33mNovo bairro: ")
                numero = int(input("\033[1;33mNovo numero de residência: "))

                functions.updatePizzarias(cnpj, nome, rua, bairro, numero)

            # Deletar
            elif (functionOption == 4):
                cnpj = input("\033[1;30mDigite o \033[1;31mCNPJ \033[1;30mda pizzaria que deseja \033[1;31mdeletar: ")
                trueCNPJ = False

                while (not trueCNPJ):
                    allPizzarias = functions.showPizzarias("no")
                    for cnpjs in allPizzarias:
                        if (cnpj == cnpjs[0]):
                            trueCNPJ = True
                    if(trueCNPJ == False):
                        cnpj = input("\033[1;31mCNPJ NÃO ENCONTRADO! \033[1;30mDigite um \033[1;31mCNPJ \033[1;30mcadastrado para \033[1;31excluir-lo: ")

                functions.deletePizzarias(cnpj)

            # Voltar
            else:
                tableOption = 0

        # opção Funcionarios
        elif (tableOption == 2):
            design.menu(['\033[1;36mExibir', '\033[1;32mAdicionar', 
                    '\033[1;33mAtualizar', '\033[1;31mDeletar', '\033[1;35mVoltar'])
            functionOption = int(input("Selecione qual função deseja utilizar: "))

            while(functionOption > 5 or functionOption <= 0):
                functionOption = int(input("Selecione apenas opções contidas na tabela: "))

            # Exibir
            if (functionOption == 1):
                functions.showFuncionarios("yes")
            
            # Adicionar
            elif (functionOption == 2):
                print(design.line())

                try:
                    idade = int(input("\033[1;30mDigite a \033[1;32mIdade \033[1;30mdo funcionário para \033[1;32madicionar-lo: "))
                except:
                    idade = int(input("\033[1;30mDigite a \033[1;31mIdade em números \033[1;30mdo funcionário para \033[1;32madicionar-lo: "))
                nome = input("\033[1;30mDigite o \033[1;32mNome \033[1;30mdo funcionário para \033[1;32madicionar-lo: ")
                numero = input("\033[1;30mDigite o \033[1;32mNúmero \033[1;30mdo funcionário para \033[1;32madicionar-lo: ")
                especializacao = input("\033[1;30mDigite a \033[1;32mEspecialização \033[1;30mdo funcionário para \033[1;32madicionar-lo: ")
                functions.addFuncionarios(idade, nome, numero, especializacao)
            
            # Atualizar
            elif (functionOption == 3):
                numeroDeContrato = int(input("\033[1;30mDigite o \033[1;33mNúmero de contrato \033[1;30mdo funcionário que deseja \033[1;33matualizar: "))
                trueNumeroDeContrato = False

                while (not trueNumeroDeContrato):
                    allFuncionarios = functions.showFuncionarios("no")
                    for funcionarios in allFuncionarios:
                        if (numeroDeContrato == funcionarios[0]):
                            print(funcionarios[0])
                            trueNumeroDeContrato = True
                    if (trueNumeroDeContrato == False):
                        numeroDeContrato = int(input("\033[1;31mNÚMERO DE CONTRATO NÃO ENCONTRADO! \033[1;30mDigite outro \033[1;33mNúmero de contrato \033[1;30mcadastrado para \033[1;33matualizar-lo: "))

                idade = input("\033[1;33mNova idade: ")
                nome = input("\033[1;33mNovo nome: ")
                numero = input("\033[1;33mNovo numero: ")
                especializacao = input("\033[1;33mNova especializacão: ")

                functions.updateFuncionarios(numeroDeContrato, idade, nome, numero, especializacao)
            
            # Deletar
            elif (functionOption == 4):
                numeroDeContrato = int(input("\033[1;30mDigite o \033[1;31mNúmero de contrato \033[1;30mdo funcionário que deseja \033[1;31mdeletar: "))
                trueNumeroDeContrato = False

                while (not trueNumeroDeContrato):
                    allFuncionarios = functions.showFuncionarios("no")
                    for funcionarios in allFuncionarios:
                        if (numeroDeContrato == funcionarios[0]):
                            trueNumeroDeContrato = True
                    if (trueNumeroDeContrato == False):
                        numeroDeContrato = int(input("\033[1;31mNÚMERO DE CONTRATO NÃO ENCONTRADO! \033[1;30mDigite outro \033[1;31mNúmero de contrato \033[1;30mcadastrado para \033[1;31mexcluir-lo: "))
                
                functions.deleteFuncionarios(numeroDeContrato)
            
            # Voltar
            else:
                tableOption = 0

        # opção Pizzas
        elif (tableOption == 3):
            design.menu(['\033[1;36mExibir', '\033[1;32mAdicionar', 
                    '\033[1;33mAtualizar', '\033[1;31mDeletar', '\033[1;35mVoltar'])
            functionOption = int(input("Selecione qual função deseja utilizar: "))

            while(functionOption > 5 or functionOption <= 0):
                functionOption = int(input("Selecione apenas opções contidas na tabela: "))

            # Exibir
            if (functionOption == 1):
                functions.showPizzas("yes")
            
            # Adicionar
            elif (functionOption == 2):
                print(design.line())

                sabor = input("\033[1;30mDigite o \033[1;32mSabor \033[1;30mda pizza para \033[1;32madicionar-la: ")

                allPizzas = functions.showPizzas("no")
                for pizzas in allPizzas:
                    if (sabor == pizzas[0]):
                        sabor = input("\033[1;31mSABOR JA CADASTRADO! \033[1;30mDigite outro \033[1;32mSabor \033[1;30mnão cadastrado para \033[1;32madicionar-lo: ")

                tempoDePreparo = input("\033[1;30mDigite o \033[1;32mTempo de Preparo \033[1;30mda pizza para \033[1;32madicionar-la: ")
                try:
                    preco = float(input("\033[1;30mDigite o \033[1;32mPreço \033[1;30mda pizza para \033[1;32madicionar-la: "))
                except:
                    preco = float(input("\033[1;30mDigite o \033[1;31mPreço em números \033[1;30mda pizza para \033[1;32madicionar-la: "))
                tamanhoDaPizza = input("\033[1;30mDigite o \033[1;32mTamanho \033[1;30mda pizza para \033[1;32madicionar-la: ")
                tipoDaPizza = input("\033[1;30mDigite o \033[1;32mTipo \033[1;30mda pizza para \033[1;32madicionar-la: ")
                functions.addPizzas(sabor, tempoDePreparo, preco, tamanhoDaPizza, tipoDaPizza)
            
            # Atualizar
            elif (functionOption == 3):
                sabor = input("\033[1;30mDigite o \033[1;33mSABOR \033[1;30mda pizza que deseja \033[1;33matualizar: ")
                truePizzas = False

                while (not truePizzas):
                    allPizzas = functions.showPizzas("no")
                    for sabores in allPizzas:
                        if (sabor == sabores[0]):
                            truePizzas = True
                    if(truePizzas == False):
                        sabor = input("\033[1;31mSABOR NÃO ENCONTRADO! \033[1;30mDigite outro \033[1;33mSabor \033[1;30mcadastrado para \033[1;33matualizar-lo: ")

                tempoDePreparo = input("\033[1;33mNovo tempo de preparo: ")
                preco = float(input("\033[1;33mNovo preço: "))
                tamanhoDaPizza = input("\033[1;33mNovo tamanho da pizza: ")
                tipoDaPizza = input("\033[1;33mNovo tipo da pizza: ")

                functions.updatePizzas(sabor, tempoDePreparo, preco, tamanhoDaPizza, tipoDaPizza)
            
            # Deletar
            elif (functionOption == 4):
                sabor = input("\033[1;30mDigite o \033[1;31mSabor \033[1;30mda pizza que deseja \033[1;31mdeletar: ")
                truePizzas = False

                while (not truePizzas):
                    allPizzas = functions.showPizzas("no")
                    for sabores in allPizzas:
                        if (sabor == sabores[0]):
                            truePizzas = True
                    if (truePizzas == False):
                        sabor = input("\033[1;31mSABOR NÃO ENCONTRADO! \033[1;30mDigite outro \033[1;31mSabor \033[1;30mcadastrado para \033[1;31mexcluir-lo: ")
                    
                functions.deletePizzas(sabor)
            
            # Voltar
            else:
                tableOption = 0

        # opção Clientes
        elif (tableOption == 4):
            design.menu(['\033[1;36mExibir', '\033[1;32mAdicionar', 
                    '\033[1;33mAtualizar', '\033[1;31mDeletar', '\033[1;35mVoltar'])
            functionOption = int(input("Selecione qual função deseja utilizar: "))

            while(functionOption > 5 or functionOption <= 0):
                functionOption = int(input("Selecione apenas opções contidas na tabela: "))

            # Exibir
            if (functionOption == 1):
                functions.showClientes("yes")
            
            # Adicionar
            elif (functionOption == 2):
                print(design.line())

                pedido = input("\033[1;30mDigite o \033[1;32mPedido \033[1;30mdo cliente para \033[1;32madicionar-la: ")
                formaDePagamento = input("\033[1;30mDigite a \033[1;32mForma de Pagamento \033[1;30mdo cliente para \033[1;32madicionar-la: ")
                try:
                    valorDaConta = float(input("\033[1;30mDigite o \033[1;32mValor da Conta \033[1;30mdo cliente para \033[1;32madicionar-la: "))
                except:
                    valorDaConta = float(input("\033[1;30mDigite o \033[1;31mValor da Conta em números \033[1;30mdo cliente para \033[1;32madicionar-la: "))
                functions.addClientes(pedido, formaDePagamento, valorDaConta)
            
            # Atualizar
            elif (functionOption == 3):
                id = int(input("\033[1;30mDigite o \033[1;33mID \033[1;30mdo cliente que deseja \033[1;33matualizar: "))
                trueClientes = False

                while (not trueClientes):
                    allClientes = functions.showClientes("no")
                    for cliente in allClientes:
                        if (id == cliente[0]):
                            trueClientes = True
                    if(trueClientes == False):
                        id = int(input("\033[1;31mID NÃO ENCONTRADO! \033[1;30mDigite outro \033[1;33mID \033[1;30mcadastrado para \033[1;33matualizar-lo: "))

                pedido = input("\033[1;33mNovo pedido: ")
                formaDePagamento = input("\033[1;33mNova forma de pagamento: ")
                valorDaConta = float(input("\033[1;33mNovo valor da conta: "))

                functions.updateClientes(id, pedido, formaDePagamento, valorDaConta)
            
            # Deletar
            elif (functionOption == 4):
                id = int(input("\033[1;30mDigite o \033[1;31mID \033[1;30mdo cliente que deseja \033[1;31mdeletar: "))
                trueClientes = False

                while (not trueClientes):
                    allClientes = functions.showClientes("no")
                    for cliente in allClientes:
                        if (id == cliente[0]):
                            trueClientes = True
                    if(trueClientes == False):
                        id = int(input("\033[1;31mID NÃO ENCONTRADO! \033[1;30mDigite outro \033[1;31mID \033[1;30mcadastrado para \033[1;31mexcluir-lo: "))

                functions.deleteClientes(id)
            
            # Voltar
            else:
                tableOption = 0

        # Sair do sistema
        else:
            design.header('\033[1;31mVoltando pro menu!!\033[m')
            break

# Fechando o banco de dados e finalizando o sistema
functions.closeData()
print("\033[1;31mSistema encerrado!!")