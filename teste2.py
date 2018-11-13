import os, sys 
comando1 = [ "/usr/bin/bc","-l"] 
comando2 = [ "/usr/local/bin/firefox"]
comando3 = [ "/usr/local/bin/mousepad"]
entrada = 0
while entrada != 4:
	entrada = int(input("Digite 1 para a calculadora, 2 para firefox e 3 para mousepad(4 para sair): "))
	if entrada == 1:
		rpaifilho, wpaifilho = os.pipe();
		rfilhopai, wfilhopai = os.pipe();
		processid = os.fork() 
		if processid:
			os.close(rpaifilho); # Fecha o descritor desnecessário 
			escrita = os.fdopen(wpaifilho, 'w') # reabre como uma stream de escrita 
			os.close(wfilhopai); # Fecha o descritor desnecessário 
			leitura = os.fdopen(rfilhopai, 'r') # reabre como uma stream de leitura 
			print("Digite uma expressão (quit para sair): ") 
			linha = sys.stdin.readline()
			while linha != "":
				if linha == "\n": # Se apertou enter leia novamente 
					linha = sys.stdin.readline()
					continue 		
				escrita.write(linha) 
				escrita.flush() 
				linha = leitura.readline()
				if linha != "": 
					print("Resposta: %s" % linha) 
				else: 
					break 
				print("Digite uma expressão (quit para sair): ") 
				linha = sys.stdin.readline() 
		else: # Processo filho 
			os.dup2(rpaifilho, sys.stdin.fileno()) # Associa a leitura pai-filho com a entrada padrão 
			os.close(wpaifilho) # Fecha o descritor desnecessário 
			os.dup2(wfilhopai, sys.stdout.fileno()) # Associa a escrita filho-pai com a saida padrao 
			os.close(rfilhopai) # Fecha o descritor desnecessário 
			# Código para substituir a imagem do processo 
			os.execve(comando1[0], comando1, os.environ) # Substitui a imagem do programa pela calculadora bc
	elif entrada == 2:			
		rpaifilho, wpaifilho = os.pipe();
		rfilhopai, wfilhopai = os.pipe();
		processid = os.fork() 
		if processid == 0:
			os.execve(comando2[0], comando2, os.environ) # Substitui a imagem do programa pelo firefox
	elif entrada == 3:
		rpaifilho, wpaifilho = os.pipe();
		rfilhopai, wfilhopai = os.pipe();
		processid = os.fork() 
		if processid == 0:
			os.execve(comando3[0], comando3, os.environ) # Substitui a imagem do programa pelo mousepad