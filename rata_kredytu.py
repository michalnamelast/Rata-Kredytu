import copy


wybor = 10

    
    
print("(1) Jeśli chcesz obliczyć okres kredytu")
print("(2) Jeśli chcesz obliczyć ratę kredytu")
print("(3) Jeśli chcesz wyjść")
while wybor != 3:    

    wybor = int(input("\n: "))
  
        

    
    if wybor == 1:
        kwota1 = int(input("Podaj calkowita kwote kredytu: "))
        rata = int(input("Podaj miesieczna rate: "))
        procent = int(input("podaj roczne oprocentowanie: "))
        i = 0
        

        while kwota1 >= 0:
            i += 1
            kwota1 = kwota1 + kwota1*(procent/100) - rata * 12
        print("Bedziesz niewolnikiem banku przez lat: ", i)



    if wybor == 2:
        lata = int(input("Wpisz okres kredytu: "))
        num = int(input("Wpisz hajs jaki pozyczasz: "))
        oproc = int(input("Wpisz oprocentowanie roczne: "))
        oprocentowanie = oproc / 100
        num2 = copy.copy(num)
        rata = 0


        while num >= 0:
            rata += 1
            num = num2   # Pamiętaj o zresetowaniu kwoty! Inaczej wchodząc na kolejne powtórzenie zacznie od kwoty która została z pętli for
            for rok in range(lata):
                num = num + (num * oprocentowanie) - rata

        rata_miesieczna = rata / 12
        print("bedzies bulic miesiecznie: ", rata_miesieczna)















