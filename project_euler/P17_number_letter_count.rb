# I chose to convert the numbers to its names and then count their letters and sum up

@numbers_to_words = {
 1000000 => "million",
 1000 => "thousand",
 100 => "hundred",
 90 => "ninety",
 80 => "eighty",
 70 => "seventy",
 60 => "sixty",
 50 => "fifty",
 40 => "forty",
 30 => "thirty",
 20 => "twenty",
 19=>"nineteen",
 18=>"eighteen",
 17=>"seventeen", 
 16=>"sixteen",
 15=>"fifteen",
 14=>"fourteen",
 13=>"thirteen",    
 12=>"twelve",
 11 => "eleven",
 10 => "ten",
 9 => "nine",
 8 => "eight",
 7 => "seven",
 6 => "six",
 5 => "five",
 4 => "four",
 3 => "three",
 2 => "two",
 1 => "one"
}


def number_name(n)
  if n < 1000
    reversed_digits = n.to_s.scan(/./).reverse
    ones = reversed_digits[0].to_i
    tens = reversed_digits[1].to_i if reversed_digits.size >= 2
    hundreds = reversed_digits[2].to_i if reversed_digits.size >= 3
    number_name = ''
    # hundreds
    number_name << "#{@numbers_to_words[hundreds]} #{@numbers_to_words[100]}" if hundreds
    number_name << " and " if hundreds && (tens != 0 || ones != 0)
    # tens and ones
    tens_ones = "#{tens}#{ones}".to_i
    if tens_ones > 0 && tens_ones < 20
      # 0-19
      number_name << "#{@numbers_to_words[tens_ones]}" 
    else
      # 20-99
      number_name << "#{@numbers_to_words[tens*10]}" if tens
      number_name << "-" if tens != 0 && ones != 0
      number_name << "#{@numbers_to_words[ones]}"
    end

    return number_name
  else
   # 1000
   return "#{@numbers_to_words[1]} #{@numbers_to_words[n]}"
  end
end

# convert all numbers from 1 to 1000 to their respective names and count the number of letters
letter_count = 0
for i in 1..1000 do 
  letter_count += number_name(i).gsub(' ', '').gsub('-','').size
end

puts letter_count



