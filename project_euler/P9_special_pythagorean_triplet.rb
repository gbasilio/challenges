
for a in 0..333 do
  for b in 0..500 do
    c = Math.sqrt(a**2 + b**2)
    if c - Integer(c) == 0
      if (a + b + c == 1000)
        p "#{a} * #{b} * #{c} = #{a*b*c}"
      end
    end
  end
end

