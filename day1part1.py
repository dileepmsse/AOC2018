freqs = []
try:
    with open('AOCInput.txt') as input:
        for each_line  in input:
            try:
                freq = each_line.replace("\n", '').strip()
                freqs.append(int(freq))

            except ValueError:
                pass
except:
    pass

print(sum(freqs))