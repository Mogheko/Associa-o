cpf = input('Digite o cpf:')
Arquivo = open('./Associados/Associados.txt','r')

if cpf in Arquivo:
        print('Essa pessoa já é associada')
        
else:
        Arquivo=open('./Associados/Associados.txt','a')
        Arquivo.write("\n" + cpf)
        print('Associada com sucesso')
        
Arquivo.close()