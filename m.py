a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","@","_"]
b = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
c = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
d = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
e = ["1","2","3","4","5","6","7","8","9","0"]
f = ["_","-","@","#"]
f1 = ''
f2 = []
for x1 in f:
    for x2 in f:
        for x3 in f:
            for x4 in f:
                for x5 in f:
                    for x6 in f:
                        for x7 in f:
                            for x8 in f:
                                f1 = x1+x2+x3+x4+x5+x6+x7+x8
                                f2.append(f1)
                                #print(f1)
filler = ''
for fan in f2:
    fan = fan+'\n'
    filler = filler + fan     
open("a","w").write(str(filler))
