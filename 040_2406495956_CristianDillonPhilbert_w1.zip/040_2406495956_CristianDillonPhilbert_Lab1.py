print(">>==========================<<")
print("||                     	    ||")
print("|| Welcome to Interrogation ||")
print("||                     	    ||")
print(">>==========================<<")

while True:
    user_input = input("Mulai Interogasi (Y/N)? ")
    if user_input == "Y":
        print("Mari kita mulai interogasi\n")
    elif user_input == "N":
        print("Tidak jadi interogasi\n")
        break
    else:
        print("\nInput tidak valid!")
        continue

    while True :
        nama = input("Siapa namamu? ")
        npm = input("Berapa nomor NPM mu? ")
        npmisvalid = True
        digit_count = 0
        
        for char in npm:
            if '0' <= char <= '9':
                digit_count +=1
            else:
                npmisvalid = False
                break
        
        if npmisvalid == False: 
            print("NPM harus berupa angka!")
            print("------------------------------\n")
            continue
        elif digit_count != 10:
            print("NPM harus sepanjang 10 digits!")
            print("------------------------------\n")
            continue

        q1 = input("Apakah kamu punya motif (Y/N)? ")
        if q1 == "Y":
            motif = input("Apa motif kamu tadi? ")
            q2 = input("Apakah kamu punya alibi (Y/N)? ")
            if q2 == "Y":
                alibi = input("Apa alibi kamu? ")
                print("\n")
                print(nama + " dengan NPM " + npm + " memiliki motif " + motif + " dan memiliki alibi " + alibi)
                print(nama + " lumayan mencurigakan nih...")
                print("------------------------------\n")
            elif q2 == "N":
                print(nama + " dengan NPM " + npm + " memiliki motif " + motif + " tapi tidak memiliki alibi")
                print("Wah, " + nama + " mencurigakan nihh >:(")
                print("------------------------------\n")
            else:
                print("Seseorang harus punya alibi atau tidak punya alibi sama sekali!")
                print("------------------------------\n")
                continue
        elif q1 == "N":
            q2 = input("Apakah kamu punya alibi (Y/N)? ")
            if q2 == "Y":
                alibi = input("Apa alibi kamu? ")
                print("\n")
                print(nama + " dengan NPM " + npm + " tidak memiliki motif dan memiliki alibi " + alibi)
                print(nama + " tidak terlalu mencurigakan sih")
                print("------------------------------\n")
            elif q2 == "N":
                print(nama + " dengan NPM " + npm + " tidak memiliki motif maupun alibi")
                print(nama + " lumayan mencurigakan nih...")
                print("------------------------------\n")
            else:
                print("Seseorang harus punya alibi atau tidak punya alibi sama sekali!")
                print("------------------------------\n")
                continue
        else:
            print("Seseorang harus punya motif atau tidak punya motif sama sekali!")
            print("------------------------------\n")
            continue
        
        lanjut = False
        while lanjut == False:
            user_input2 = input("Lanjut interogasi (Y/N)? ")
            if user_input2 == "Y":
                print("------------------------------\n")
                start = True
                break
            elif user_input2 == "N":
                print("Interogasi telah selesai\n")
                start = False
                break
            else:
                print("\nInput tidak valid")

        if not start:
            break
    break

print(">>==========================<<")
print("||                     	    ||")
print("|| Ending the Interrogation ||")
print("||                     	    ||")
print(">>==========================<<")