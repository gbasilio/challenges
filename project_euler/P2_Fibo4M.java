package br.gbasilio.euler;

public class P2_Fibo4M {
	
	public static void main(String[] args) {
		int soma = 0;
		int v_anterior = 0;
		int v_atual = 1;
		while (v_atual <= 4000000){
			int prox_v_atual = v_atual + v_anterior;
			v_anterior = v_atual;
			v_atual = prox_v_atual;
			if (v_atual % 2 == 0){
				soma += v_atual;
			}
		}
		System.out.println(soma);
	}

}
