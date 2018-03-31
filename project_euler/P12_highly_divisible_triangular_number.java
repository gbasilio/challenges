package com.taxweb.plugin;

import java.util.HashSet;
import java.util.Set;

public class P12_highly_divisible_triangular_number {

	public static void main(String[] args) {
		int curr = 1;
		while (true){
			int triangular = 0;
			for (int i = 1; i <=curr; i++){
				triangular += i;
			}
			
			Set<Integer> divisores = new HashSet<Integer>();
			for (int i = 1; i <= Math.sqrt(triangular); i++){
				if (triangular % i == 0){
					divisores.add(i);
					divisores.add(triangular/i);
				}
			}
			int numDivisores = divisores.size();
			
			System.out.println(triangular + " - " + numDivisores);
			if (numDivisores  >= 500){
				break;
			}
			curr++;
		}
			
	}
	
}
