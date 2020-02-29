"""
f=open("nacer.txt","r")
seq=""
ligne=f.readline()
while ligne!="":
    seq=seq+ligne[0:len(ligne)-1]
    ligne=f.readline()


sequence=seq
sequence=sequence.upper()
A=sequence.count("A")
T=sequence.count("T")
G=sequence.count("G")
C=sequence.count("C")

total=A+C+T+G


seq=len(sequence)
rest=seq-total
porA=(A*100)/float(seq)
porC=(C*100)/float(seq)
porT=(T*100)/float(seq)
porG=(G*100)/float(seq)
porR=(rest*100)/float(seq)
print "le por de A " ,porA ,"%\n"
print "le por de C " ,porC ,"%\n"
print "le por de G " ,porG,"%\n"
print "le por de T " ,porT,"%\n"
print "le por de reste " ,porR,"%\n"

nom=raw_input("entre fich \n")
f=open(nom,"w")
f.write(str(porA)+"\n")
f.write(str(porC)+"\n")
f.write(str(porG)+"\n")
f.write(str(porT)+"\n")
f.write(str(porR)+"\n")
"""



choix=raw_input("1 pour tran et 2 pour inverse  \n")

nom=raw_input("entre fich \n")



f=open("nacer.txt","r")
seq=""
ligne=f.readline()
while ligne!="":
    seq=seq+ligne[0:len(ligne)-1]
    ligne=f.readline()


if(choix=="1"):
    sequence=seq
    sequence=sequence.upper()
    i=0
    seq2=""
    while i<len(sequence):
        if sequence[i]=="T":
            seq2=seq2 + "U"
        else:
            seq2=seq2 + sequence[i]
        i=i+1
    print "jfnrfjkn"
    f=open(nom,"w")
    f.write(seq2)

elif(choix=="2"):
    sequence=seq
    sequence=sequence.upper()
    i=len(sequence)-1
    seq2=""
    while i>=0:
        if sequence[i]=="A":
            seq2=seq2 + "T"
        elif sequence[i]=="T":
            seq2=seq2 + "A"
        elif sequence[i]=="C":
            seq2=seq2 + "G" 
        else:
            seq2=seq2 + "C" 
        i=i-1
    f=open(nom,"w")
    f.write(seq2)
    
    