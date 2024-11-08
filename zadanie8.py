pada = False
licznik_nie = 0
while not pada:
    print("Nie pada! yaaay")
    odpowiedz = input("Czy pada? (tak/nie) ")
    if odpowiedz == 'tak':
        print('powiedziałeś nie: ', licznik_nie , 'razy')
        pada = True
    elif odpowiedz == 'nie':
        licznik_nie += 1
    else:
        print("to wyjdż na dwór i się dowiedz")
