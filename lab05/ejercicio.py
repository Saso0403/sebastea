brain = "X-DSPAM-Confidence:0.8475"

s1 = brain.find(":")
print("Inicia en el Indice: "+ str(s1))

s2 = brain.find("5")
print("Termina en: "+ str(s2))

last = len(brain)
substring = brain[s1+1:last]
numeric = float(substring)

print(numeric)
print(type(numeric))