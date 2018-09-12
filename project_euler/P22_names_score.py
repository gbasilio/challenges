
names_list = open('p022_names.txt', 'r').read().split(',')
names_list = list(map(lambda name: name.replace('"',''), names_list))

sum_name_scores = 0
name_position = 0
for name in sorted(names_list):
    name_position += 1
    name_sum = 0
    for c in name:
        name_sum += ord(c)-64
    name_score = name_position * name_sum 
    sum_name_scores += name_score

print sum_name_scores
