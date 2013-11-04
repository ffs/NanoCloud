#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket
import os
import sys

PORTAL = ''                                								# Endereco IP do Servidor
HOST_1 = ''																# Endereco IP do Host 1
HOST_2 = ''																# Endereco IP do Host 2
HOST_3 = ''																# Endereco IP do Host 3
PORT = 4200                                								# Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((PORTAL, PORT))
tcp.listen(5)
CONTADOR = 0;
while True:
        con, cliente = tcp.accept()
        pid = os.fork()
        if pid == 0:
                tcp.close()
                print 'Conectado com o Cliente {}', cliente
                
                
                
                
                print 'Aguardando Arquivo Fonte do Cliente', cliente
                
                ## Recebe o arquivo Fonte ##
                while True:												
					arq = open('/tempCodigo.txt', 'w')					# Abre arquivo Temporário utilizado para montar o código fonte
					msg = con.recv(1024)
					if not msg: break
					print cliente, msg
					arq.write(msg)										# Escreve mensagem recebida no arquivo Temporário aberto
                ## Arquivo fonte recebido ##
                
                print 'Arquivo Fonte recebido com sucesso do Cliente', cliente
                
                
                
                
                print 'Escalonando um Host para executar o programa do Cliente', cliente
				
				## Escalonando um servidor
				
				CONTADOR = CONTADOR + 1
				if CONTADOR mod 3 == 1 HOST = HOST_1
				else if CONTADOR mod 3 == 2 HOST = HOST_2
				else HOST = HOST_3
				
				## Servidor escalonado
				
				print 'Host escalonado: ', HOST
				
				
				
				
				print 'Abrindo conexão com o HOST {}', HOST
				
				## Abre conexão com o Host escalonado
				host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				host.connect((HOST, PORT))
				## Conexão aberta com sucesso ##
				
				print 'Conectado com o HOST {} com sucesso', HOST
				
				
				
				
				print 'Enviado Arquivo Fonte do Cliente {} para o Host {}', cliente, HOST
				
				## Envia o arquivo Fonte ##
				arquivoFonte = arq.read()
				host.send (arquivoFonte)								# Envia arquivo fonte para servidor escalonado
				## Arquivo fonte enviado ##
				
				print 'Enviado Arquivo Fonte do Cliente {} enviado com sucesso para o Host {}', cliente, HOST
				
				
				
				
				print 'Aguardando resposta do Host {} para o Cliente {}', HOST, cliente
				
				## Aguarda resposta do Host ##
				while True:
					resposta = host.recv(1024) 							# Esperar resposta do servidor
					if not msg: break
					print host, msg
					con.send (resposta)									# Enviar resposta ao cliente
				## Arquivo fonte recebido ##
				
				print 'Resposta enviada do Host {} para o Cliente {}', HOST, cliente
				
				
				
				
				print 'Finalizando conexao com o Host', HOST
				
				host.close();
				
                print 'Finalizando conexao do cliente', cliente
                
                con.close()
                
                sys.exit(0)
        else:
                os.waitpid (pid, 0)
                con.close()
