
target_num = 600851475143;
primes = []

for i in 1..(target_num) do
	prime = true
	for j in 2..(i/2) do
		if i % j == 0
			prime = false
		end
	end
	primes << prime

	

end

