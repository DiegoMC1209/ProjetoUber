import this, avalicao


this.localidade = 0
this.opcao = 0
this.opcaoMotorista = 0
this.opcaoAvaliacao = 0
this.comentario = 0

print("        Bem  Vindo a Uber!        \n\n")

def mostrarMenu():
    print("Onde você se encontra? " +
            "\n1. Santo André"+
            "\n2. São Bernardo" +
            "\n3. São Caetano" +
            "\n4. Mauá" +
            "\n5. Diadema" +
            "\n6. Guarulhos"
            "\n7. Embu das Artes" +
            "\n8. Campinas" +
            "\n9. Boituva" +
            "\n10. Barueri")
    this.opcao = int(input())

def operacao():
    while this.opcao < 1 or this.opcao > 10:

        mostrarMenu()
        if this.opcao == 1:

            print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

            print("Motoristas Disponiveis: \n" +
                  "\n1. Julio Souza (★★★) á 2km de você" +
                  "\n2. Antonio Farias (★★★★) á 6km de você" +
                  "\n3. Gustavo Almeida (★★) á 3km de você" +
                  "\n4. Gabriela Silva (★★★★★) á 2,5km de você" +
                  "\n5. Evandra Soares (★★★★) á 4km de você")
            this.opcaoMotorista = int(input())
            if this.opcaoMotorista == 1 or 5:
                avalicao.avaliar()

        elif this.opcao == 2:
            print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

            print("Motoristas Disponiveis: \n" +
                  "\n1. Adagoberto Farias (★★) á 1,2km de você" +
                  "\n2. Guilherme Botelho (★) á 4,6km de você" +
                  "\n3. Andreia Silva (★★★★) á 3,2km de você" +
                  "\n4. Gabriel Moraes (★★★) á 4,2km de você" +
                  "\n5. Pedro Guilherme (★★★★★) á 4,9km de você")
            this.opcaoMotorista = int(input())
            if this.opcaoMotorista == 1 or 5:

                avalicao.avaliar()

        elif this.opcao == 3:
            print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

            print("Motoristas Disponiveis: \n" +
                  "\n1. Valentina Pereira (★★★★★) á 2,1km de você" +
                  "\n2. Sophia Abravanel (★★★★) á 2,6km de você" +
                  "\n3. Aline Gobertina (★★★) á 3,2km de você" +
                  "\n4. Pedro Miguel (★★) á 2,2km de você" +
                  "\n5. Joaquim Calembrari(★) á 1,4km de você")
            this.opcaoMotorista = int(input())
            if this.opcaoMotorista == 1 or 5:

                avalicao.avaliar()

        elif this.opcao == 4:
            print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

            print("Motoristas Disponiveis: \n" +
                  "\n1. Gabriela Alves (★) á 2,9km de você" +
                  "\n2. Gustavo Medina (★★) á 1,6km de você" +
                  "\n3. Felipe Coutinho (★★★) á 3,1km de você" +
                  "\n4. André Adogoberto (★★★★) á 2,3km de você" +
                  "\n5. Jucelina Alves (★★★★★) á 4,1km de você")
            this.opcaoMotorista = int(input())
            if this.opcaoMotorista == 1 or 5:

                avalicao.avaliar()

        elif this.opcao == 5:
            print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

            print("Motoristas Disponiveis: \n" +
                  "\n1. Diego Batagim (★★★★) 1,9á km de você" +
                  "\n2. Rafael Pereira (★★★) 3á km de você" +
                  "\n3. Rafael Melo (★★★★★) á 2,3km de você" +
                  "\n4. Vinicius Morais (★★) á 7,8km de você" +
                  "\n5. Allan Sobral (★) á 1km de você")
            this.opcaoMotorista = int(input())
            if this.opcaoMotorista == 1 or 5:

                avalicao.avaliar()

        elif this.opcao == 6:
            print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

            print("Motoristas Disponiveis: \n" +
                  "\n1. Gustavo Rafael(★★★★). 10km de distancia" +
                  "\n2. Antonio Silva(★★★) á 2km de voçê" +
                  "\n3. Vinicius Eduardo(★★★★) á 6km de voçê" +
                  "\n4. Mateus pereira(★★★★) á 12km de voçê" +
                  "\n5. Cristiano Soares(★★★★★) á 4km de voçê")
            this.opcaoMotorista = int(input())
            if this.opcaoMotorista == 1 or 5:
                avalicao.avaliar()

        elif this.opcao == 7:
            print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

            print("Motoristas Disponiveis: \n" +
                  "\n1. Guilherme Souza(★★) 11km de distancia" +
                  "\n2. Aline Farias(★★★★★) á 4km de voçê" +
                  "\n3. Pedro Almeida(★★★★) á 5km de voçê" +
                  "\n4. Gabriel Silva(★★★★) á 1km de voçê" +
                  "\n5. Diego edmundo(★★★★★) á 5km de voçê")
            this.opcaoMotorista = int(input())
            if this.opcaoMotorista == 1 or 5:
                avalicao.avaliar()

        elif this.opcao == 8:
            print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

            print("Motoristas Disponiveis: \n" +
                  "\n1. Alan Souza(★) 8km de distancia" +
                  "\n2. Pedro Farias(★★★★) á 2km de voçê" +
                  "\n3. Jean Lucas(★★★) á 2km de voçê" +
                  "\n4. Messi Silva(★★) á 3km de voçê" +
                  "\n5. Neymar Soares(★★★★★) á 4km de voçê")
            this.opcaoMotorista = int(input())
            if this.opcaoMotorista == 1 or 5:
                avalicao.avaliar()

        elif this.opcao == 9:
            this.opcaoMotorista = -1
            while(this.opcaoMotorista < 1 or this.opcaoMotorista > 5):
                print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

                print("Motoristas Disponiveis: \n" +
                      "\n1. Lionel Antonio(★) 3km de distancia" +
                      "\n2. Pablo (★★★★) á 2km de voçê" +
                      "\n3. Gustavo Almeida(★★★★) á 4km de voçê" +
                      "\n4. Gabriela Silva(★★★★★) á 4km de voçê" +
                      "\n5. Evandra Soares(★★★★) á 9km de voçê")
                this.opcaoMotorista = int(input())
                if this.opcaoMotorista > 1 and this.opcaoMotorista < 5:
                    avalicao.avaliar()
                else:
                    print("Erro!, digite novamente!")
                    this.opcaoMotorista = int(input())


        elif this.opcao == 10:
            print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

            print("Motoristas Disponiveis: \n" +
                  "\n1. Julio Souza(★) 1km de distancia" +
                  "\n2. Antonio Farias(★★★★) á 3km de voçê" +
                  "\n3. Gustavo Almeida(★★★★★) á 2km de voçê" +
                  "\n4. Gabriela Silva(★★★) á 4km de voçê" +
                  "\n5. Evandra Soares(★★) á 6km de voçê")
            while this.opcaoMotorista > 1 and this.opcaoMotorista < 5:
                avalicao.avaliar()







