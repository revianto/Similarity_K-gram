print('Minimal 6 huruf')
print('Input Text Training: ') 
t1 = input()
print('Input Text Uji: ') 
t2 = input()

# print(t1,t2)
t1 = t1.replace(" ","")
t2 = t2.replace(" ","")

def kgram(word):
	kgram = []
	gram = []
	for i in word:
		gram.append(i)
	nt2 = 4
	for i in range(len(gram)):
		nt1 = nt2 - 4
		word2 = []
		for j in range(nt1,nt2):
			word2.append(gram[nt1])
			nt1 += 1
		word3 = "".join(word2)
		kgram.append(word3)
		# print(i)
		nt2 += 1
		if nt2 > len(gram):
			break
	return kgram

k1 = kgram(t1)
k2 = kgram(t2)

c = 0
k = 2
ab = len(k1)+len(k2)
for i in k2:
	if i in k1:
		c +=1

print(k)
s = k*c/ab

print(s*100,'%')

if s >= 0.6:
	print('Plagiat')
else:
	print('Bukan Plagiat')