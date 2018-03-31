public class P6_sum_square_difference {
	public static void main(String[] args) {
		double somaQuadrados = 0;
		double quadradoSoma = 0;
		
		for (int i = 1; i <= 100; i++){
			somaQuadrados += Math.pow(i, 2);
			quadradoSoma += i;
		}
		quadradoSoma = Math.pow(quadradoSoma, 2);
		
		System.out.printf("Resp: %f\n", (quadradoSoma - somaQuadrados));
	}
}

