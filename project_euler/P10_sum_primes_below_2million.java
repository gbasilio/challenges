public class P10_sum_primes_below_2million {

	public static void main(String[] args) {
		long sum = 0;
		for (int i = 2; i <= 2000000; i++){
			int sqRt = (int)Math.sqrt(i);
			boolean prime = true;
			for (int j = 2; j <= sqRt; j++){
				if (i % j == 0){
					prime = false;
					break;
				}
			}
			if (prime){
				sum += i;
			}
		}
		System.out.println(sum);
	}
}

