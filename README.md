Descrição
===

O projeto se trata de um programa capaz de realizar o GetRequest do protocolo SNMP, o programa conta com uma interface gráfica que possui três abas, a primeira, o usuário pode informar o IP que deseja obter informações e o código retorna uma lista com todas as OIDs (Object Identifier) disponíveis para o dispositivo indicado, além disso é possui copiar um desses OIDs para ser usado na segunda aba, na qual o usuário é capaz de informar o IP, a Porta e o OID que deseja receber uma resposta, então o código irá montar o quadro SNMP message para realizar o GetRequest e mostrar a resposta obtida para o usuário. Por fim, a última aba “SNMP TRAP” contém um botão que inicia a espera de mensagens snmp trap na rede, através da porta 162.