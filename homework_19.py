import random
import os
path = os.path.join(os.getcwd(), "random_file.txt")
randomlist = random.sample(range(1, 100), 21)
odds = [] 
# odd_str = ""  
for value in randomlist:
    if value % 2 != 0:
        odds.append(value)    
    # traverse in the string  
odd_str=' '.join([str(item) for item in odds])
sum_ = sum(odds)
res = F"Numers={odd_str} \nSum={sum_} "
with open(path, "w") as l:
	l.write(res)
with open(path, "r") as l:
	print(l.read(100))
    


