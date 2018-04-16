
# get the number (fortunately I don't have to worry about the size of the number in ruby - that could make the problem much more challenging)
twoPower1000Str = (2**1000).to_s

# get the digits in an array
digits = twoPower1000Str.scan(/./)

# get the sum
sum = 0
digits.each do |d|
  sum += d.to_i
end

puts "The sum of the digits of 2^1000 = #{sum}"


