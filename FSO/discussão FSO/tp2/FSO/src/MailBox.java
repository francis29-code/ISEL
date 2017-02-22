import java.io.File;
import java.io.RandomAccessFile;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;

public class MailBox {
	final static String path = "C:\\Users\\Denga\\Desktop\\workspace\\FSO\\comunica\\";
	private File file;
	private FileChannel filechannel;
	private MappedByteBuffer map;
	final static int MAX_BUFFER = 30;

	public MailBox(String nome) {
	
		try {
			this.file = new File(path+nome);
			this.file.createNewFile();
			filechannel = new RandomAccessFile(this.file, "rw").getChannel();

		} catch (Exception e) {
			e.printStackTrace();
		}

		try {
			map = filechannel.map(FileChannel.MapMode.READ_WRITE, 0, MAX_BUFFER);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	public String read() {

		String str = new String();
		char c;
		map.position(0);
		while ((c = map.getChar()) != '\0') {
			str += c;
		}

		return str;
	}
	
	public void eraseContent() {
		write("xxxxxxx");
	}

	public void write(String msg) {
		char c;

		map.position(0);
		for (int i = 0; i < msg.length(); i++) {
			c = msg.charAt(i);
			map.putChar(c);
		}
		map.putChar('\0');
	}

	public void closeChannel() {
		try {
			filechannel.close();
		} catch (Exception e) {

			e.printStackTrace();
		}
	}
	

}
