# Lift diam di lantai y
y = 1 # Nilai default y
idle = True
PanggilTurun = [False for i in range(6)]
PanggilNaik = [False for i in range(6)]
Batas = int(input("Masukkan batas orang dalam lift: "))
cap = int(input("Masukkan kapasitas berat yang dapat ditampung lift (dalam kg): "))
weight = [0 for i in range(Batas)]
emg = False
mungkinemg = False
#------------------------------------------------------------
# [ R E S E T   N I L A I   M E N J A D I   D E F A U L T ]
def reset():
    global y
    global PanggilNaik
    global PanggilTurun
    global mungkinemg
    mungkinemg = False
    y = 1
    for i in range(5):
        PanggilNaik[i] = False
        PanggilTurun[i] = False
#------------------------------------------------------------
# [ M E S I N    P E N G G E R A K   &   E N C O D E R  &   G O V E R N O R ]
def Naik(a, b):
    global idle
    global y
    global emg
    global mungkinemg
    listrik = input("Apakah listrik aman (0=tidak, 1=ya)? ")
    if(b == 5): Dengar()
    elif(listrik == "0"): ard(b)
    elif(b < 5):
        if(mungkinemg): emergency()
        if(idle):
            idle = False
            tmp = b
            cepat = False
            while(a != b+1):
                cepat = True
                b += 1
            if(cepat): GerakCepat(tmp, b, 1)
            b += 1
            y = b
            GerakLambat(b-1, b, 1)
            idle = True
def Turun(a, b):
    global idle
    global y
    global emg
    global mungkinemg
    listrik = input("Apakah listrik aman (0=tidak, 1=ya)? ")
    if(b == 5): Dengar()
    elif(listrik == "0"): ard(b)
    elif(b > 1):
        if(mungkinemg): emergency()
        if(idle):
            idle = False
            tmp = b
            cepat = False
            while(a != b-1):
                cepat = True
                b -= 1
            if(cepat): GerakCepat(tmp, b, 0)
            b -= 1
            y = b
            GerakLambat(b+1, b, 0)
            idle = True
def GerakLambat(a, b, c):
    if(c == 1):
        print(f"__|{b}|__")
        print("|  |  |")
        print("|  |  |")
        print("|__|__|")
        print("   ^")
        print("   .")
        print("   .")
        print("   .")
        print("   .")
        print("   .")
        print(f"__|{a}|__")
        print("|  |  |")
        print("|  |  |")
        print("|__|__|")
        print("Lift bergerak lambat.")
    else:
        print(f"__|{a}|__")
        print("|  |  |")
        print("|  |  |")
        print("|__|__|")
        print("   .")
        print("   .")
        print("   .")
        print("   .")
        print("   .")
        print("   v")
        print(f"__|{b}|__")
        print("|  |  |")
        print("|  |  |")
        print("|__|__|")
        print("Lift bergerak lambat.")
def GerakCepat(a, b, c):
    if(c == 1):
        print(f"__|{b}|__")
        print("|  |  |")
        print("|  |  |")
        print("|__|__|")
        print("   ^")
        print("   .")
        print("   .")
        print(f"__|{a}|__")
        print("|  |  |")
        print("|  |  |")
        print("|__|__|")
        print("Lift bergerak cepat.")
    else:
        print(f"__|{a}|__")
        print("|  |  |")
        print("|  |  |")
        print("|__|__|")
        print("   .")
        print("   .")
        print("   v")
        print(f"__|{b}|__")
        print("|  |  |")
        print("|  |  |")
        print("|__|__|")
        print("Lift bergerak cepat.")
    print()
#------------------------------------------------------------
# [ A U T O M A T I C   R E S C U E   D R I V E ]
def ard(x):
    global idle
    global y
    print("Menunggu 15 detik...")
    print("Lift bergerak ke lantai terdekat.")
    print("Lift mati.")
    idle = False
#------------------------------------------------------------
# [ C A R   D O O R   &   C A R   O P E R A T I N G   P A N E L ]
def Tunggu(a):
    print(f"Lift sedang menunggu selama {a} detik...")
def BukaPintu():
    print("________________")
    print("||            ||")
    print("||____________||")
    print("||\__________/||")
    print("|| |        | ||")
    print("|| |        | ||")
    print("|| |        | ||")
    print("|| |        | ||")
    print("|| |        | ||")
    print("|| |________| ||")
    print("||/__________\||")
    print("Pintu lift dibuka.")
    Tunggu(30)
    penghalangpintu = input("Apakah ada yang menghalangi pintu (0=tidak, 1=ya)? ")
    if(penghalangpintu == "1"):
        Tunggu(3)
def TutupPintu():
    print("________________")
    print("||            ||")
    print("||____________||")
    print("||     ||     ||")
    print("||     ||     ||")
    print("||     ||     ||")
    print("||     ||     ||")
    print("||     ||     ||")
    print("||     ||     ||")
    print("||     ||     ||")
    print("||||||||||||||||")
    print("Pintu lift ditutup.")
#------------------------------------------------------------
# [ C O U N T E R W E I G H T ]
def CekKapasitas(a):
    sum = 0
    for i in range(Batas):
        sum += weight[i]
    while(sum > a):
        # [ A L A R M   B U Z Z E R ]
        print("*beep* *beep*")
        print("Berat melebihi kapasitas lift! Harap beberapa orang meninggalkan lift.")
        print(weight)
        idx = int(input(f"Pilih orang yang mau dikeluarkan (basis 1): "))
        sum -= weight[idx-1]
        weight[idx-1] = 0
    print(weight)
#------------------------------------------------------------
# [ E M E R G E N C Y ]
def emergency():
    global idle
    global emg
    emgbutton = input("Apakah lift bisa berjalan dengan baik (0=tidak, 1=ya)? ")
    if(emgbutton == "0"): 
        print("Tombol emergency ditekan.")
        # [ I N T E R P H O N E ]
        print("Mendengar arahan dan mendapat bantuan dari teknisi.")
        print("Keluar dari lift.")
        idle = False
        emg = True
#------------------------------------------------------------
# [ C O N T R O L   S Y S T E M ]
def Dengar():
    global idle
    global y
    global emg 
    global mungkinemg
    while(idle):
        reset()
        x = int(input("Kamu lagi di lantai berapa nih (Pilih di antara 1-5)? "))
        if(x == 1) : PanggilNaik[x] = True
        elif(x == 5): PanggilTurun[x] = True
        else : 
            inp = input("Mau naik atau turun (0=turun, 1=naik)? ")
            if(inp == "1"): PanggilNaik[x] = True
            else: PanggilTurun[x] = True
        if(PanggilTurun[x] or PanggilNaik[x]):
            if(x > y): 
                Naik(x, y)
            elif(x < y): Turun(x, y)
            if(idle):
                BukaPintu()
                for i in range(Batas):
                    weight[i] = int(input(f"Masukkan berat orang ke-{i+1} (Masukkan 0 jika orang ke-{i+1} tidak ada): ")) 
                CekKapasitas(cap)
                TutupPintu()
                z = int(input("Masukkan lantai tujuan: "))
                mungkinemg = True    
                if(z > y): Naik(z, y)
                elif(z < y): Turun(z, y)
                if(idle):
                    BukaPintu()
                    TutupPintu()
                    print("Anda telah sampai di lantai tujuan.")
                    tmp = input("Apakah Anda masih ingin menaiki lift (0=tidak, 1=ya)? ")
                    if(tmp == "0"): idle = False
        if(x < 5): x += 1
        elif(x == 5): x = 1
Dengar()