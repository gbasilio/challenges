public class P4_largest_palindrome_product {
	public static void main(String[] args) {
		int largestP=0;		
		for (int i = 999; i >= 0; i--){
			for (int j = 999; j >= 0; j--){
				int prod = i * j;
				String s = prod+"";
				char[] c = new char[s.length()];
				for (int k = 0; k < s.length(); k++){
					c[s.length()-k-1] = s.charAt(k);
				}
				String invertedS = new String(c);
				if (s.equals(invertedS) && i >= 100 && j >= 100){
					if (prod > largestP){
						largestP = prod;
					}
				}
			}
		}
		
		System.out.println(largestP);
	}
}
