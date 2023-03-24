package Teste;

//import java.io.FileInputStream;
//import java.io.DataInputStream;
//import java.io.DataOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Sevidor {
    public static void main(String[] args) throws IOException {
		ServerSocket socket = new ServerSocket(4511);
		System.out.println("Conexão feita");
		Socket so = socket.accept();
		ObjectInputStream input  = new ObjectInputStream(so.getInputStream());
		while(input.readUTF()!=null) {
		  String linha = input.readUTF();	
		  ObjectOutputStream exit = new ObjectOutputStream(so.getOutputStream());
		  exit.writeUTF(linha);
		}
		
		

	    input.close();
	    socket.close();
//	    exit.close();
//    	while(true) {    		
//    		ServerSocket socket = new ServerSocket(4422);
//    		System.out.println("Conexão feita");
//    		Socket so = socket.accept();
//    		System.out.println("Cliente " + so.getInetAddress().getHostAddress() + " conectado.");
//    		
//    		DataInputStream input = new DataInputStream(so.getInputStream());
//    		int men = input.readInt();
//    		System.out.println(men);
//    		DataOutputStream exit = new DataOutputStream(so.getOutputStream());
//    		exit.write(men);
//    		
//    		input.close();
//    		exit.close();
//    		socket.close();
//    	}
	}
    
}
