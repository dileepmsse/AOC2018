freqs = []
try:
    with open('AOCInput-0201.txt') as input:
        for each_line  in input:
            try:
                freq = each_line.replace("\n", '').strip()
                freqs.append(freq)

            except ValueError:
                pass
except:
    pass
	
twice = 0
thrice = 0	

for freq in freqs:
	
	lst = dict.fromkeys(freq, 0) #creates a list with unique keys
	
	for letter in freq:
		lst[letter] += 1
	
	if 2 in lst.values():
		twice += 1
	
	if 3 in lst.values():
		thrice +=1

print("nextstar",twice * thrice)
#print(lst)