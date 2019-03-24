g=1

while g>0:
    try:
        a = int(input('chislo a: '))
    except (ValueError, NameError):
        print('errorA')
        continue
        
    while g>0:
        try:
            b = int(input('chislo b: '))
        except (ValueError, NameError):
            print('errorB')
            continue
                
        while g>0:
            try:
                c = int(input('chislo c: '))
            except (ValueError, NameError):
                print('errorC')
                continue
                        
            while g>0:
                try:
                    d = int(input('chislo d: '))
                    
                    print(a)
                    print(b)
                    print(c)
                    print(d)

                    g -= 1

                except (ValueError, NameError):
                    print('errorD')
                    continue

