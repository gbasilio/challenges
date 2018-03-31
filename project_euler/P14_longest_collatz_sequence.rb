
longest_chain = 0
initial_num = 0
for n in 1..1000000 do
  curr = n
  seq = []
  while curr != 1 do
    seq << curr
    if curr%2 == 0
      curr = curr/2
    else
      curr = 3*curr+1
    end
  end

  p "Start: #{n} / chain length: #{seq.size}"
  if seq.size > longest_chain
    longest_chain = seq.size
    initial_num = n
  end
end

p "Longest chain is #{longest_chain} elements long and is formed when starting the Collatz sequence with #{initial_num}."
