package Teste;


//import java.io.DataInputStream;
//import java.io.DataOutputStream;
//import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.Scanner;

 

public class proSock {
	public static void main(String[] args) throws IOException {
		Scanner tec = new Scanner(new FileReader("C:\\Users\\Davi Lúcio\\Documents\\Samuca IFRN\\minop.txt"));
		
Socket novo = new Socket("192.168.0.111",4511);
		ObjectOutputStream dado = new ObjectOutputStream(novo.getOutputStream());
//        dado.writeObject("C:\\Users\\Davi Lúcio\\Documents\\Samuca IFRN\\minop.txt");
        //o object seria o syscall
		ObjectInputStream volta = new ObjectInputStream(novo.getInputStream());
		while(tec.hasNext()) {
			dado.writeUTF(tec.nextLine());
			System.out.println(volta.readUTF());
		}

		
            novo.close();
            dado.close();
    		tec.close();
	   	}
	

	
}
