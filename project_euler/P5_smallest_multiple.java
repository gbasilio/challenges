public class P5_smallest_multiple.java {
	public static void main(String[] args) {
		long inicio = System.nanoTime();
		int resp = 20;
		while (true){
			boolean found = true;
			for (int i = 1; i <= 20; i++){
				if (resp % i != 0){
					found = false;
					break;
				}
			}
			if (found) break;
			resp++;
		}
		System.out.println(resp);
		System.out.println((System.nanoTime() - inicio) / (1000000) + "ms");
	}
}
