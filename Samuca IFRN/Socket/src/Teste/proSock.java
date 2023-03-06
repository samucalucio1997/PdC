package Teste;


import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.net.Socket;

 

public class proSock {
	public static void main(String[] args) throws IOException {
		Socket novo = new Socket("45.228.102.255",4422);
		FileOutputStream fos = new FileOutputStream("C:\\Users\\Davi Lúcio\\Documents\\Samuca IFRN\\minop.txt");
		ObjectOutputStream dado = new ObjectOutputStream(fos);
        dado.writeObject("Olá");//o object seria o syscall
        dado.close();
        novo.close();
	   	}
	

	
}
