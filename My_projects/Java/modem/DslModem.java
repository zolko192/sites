public class DslModem extends Modem {
	String method = "Dsl connection!";
	
	public void connect() {
		System.out.println("Connection to the Internet.....");
		System.out.println("Using a " + method);
	}
}
