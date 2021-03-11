
sekwencja = [0,0,0,0,1]
i = len(sekwencja) # count of bite
wielomian = [i-3]

# choose you preffer Fibbonaci or Galua registry
Galois = True
Fib = False
ile_cykli=32 # how many cykles of registry do you want


if(Galois):
    for c in range(ile_cykli):
        stara_sekwencja = list(sekwencja)
        
        for a in range(i):
            
            if( a in wielomian ):
                
                sekwencja[a]=stara_sekwencja[(a-1)]^stara_sekwencja[len(stara_sekwencja)-1]
            else:
                
                sekwencja[a]=stara_sekwencja[(a-1)] 
        
        temp = i-1
        k=0
        for s in sekwencja:
            k = k + s*2**temp
            temp-=1
        print(sekwencja,k)
        
        
if(Fib):
    for c in range(ile_cykli):
        stara_sekwencja = list(sekwencja)
        
        for a in range(i):
            
            
            if( a == 0):
                sekwencja[0]=stara_sekwencja[(a-1)]
                #print(stara_sekwencja)
                for q in wielomian:
                    sekwencja[0]=sekwencja[0] ^ stara_sekwencja[q-1]
                    #print(sekwencja[0],stara_sekwencja[q])
                
            else:
                
                sekwencja[a]=stara_sekwencja[(a-1)] 
        temp = i-1
        k=0
        for s in sekwencja:
            k = k + s*2**temp
            temp-=1
        print(sekwencja,k)
        
        