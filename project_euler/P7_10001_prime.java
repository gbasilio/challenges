public class P7_10001_prime{

	public static void main(String[] args) {
		int i = 2;
		int pcount = 0;
		while (true){
			boolean prime = true;
			for (int j = 2; j < i; j++) {
				if (i % j == 0) {
					prime = false;
					break;
				}
				if (j > (i/2)) break;
			}
			if (prime) {
				pcount++;
				System.out.println(pcount + ": " + i);
			}
			i++;
			if (pcount >= 10001) break;
		}
	}
}
