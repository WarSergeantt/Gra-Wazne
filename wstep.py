import time
from colors import Colors
from osoba import Osoba
import zmienne
from rozwiniecie import rozwiniecie1

def wstep1():
    print('za chwilę zaladuje sie gra: aby zagrac dalej wybierz na klawiaturze "T", natomiast by ją zakonczyc wybierz "N"')
    for i in range(1, 101):
        if i == 100:
            print(f'{Colors.MAGENTA}{i}{Colors.END}')
        elif i >= 80:
            print(f'{Colors.GREEN}{i}{Colors.END}')
        elif i >= 50:
            print(f'{Colors.YELLOW}{i}{Colors.END}')
        else:
            print(f'{Colors.RED}{i}{Colors.END}')
        time.sleep(0.05)
    zacznij_gre = input(f'{Colors.CYAN}GRA ZOSTALA POPRAWNIE WCZYTANA \n{Colors.RED}!UWAGA!{Colors.MAGENTA} Zwazaj na wielkosc liter {Colors.RED}!UWAGA! \n{Colors.BLUE}Chcesz przystapic do gry {Colors.YELLOW}(wpisz {Colors.GREEN}Tak{Colors.YELLOW}){Colors.BLUE} czy oposcic gre {Colors.YELLOW}(wpisz {Colors.RED}Nie{Colors.YELLOW})?{Colors.END}\n')

    if zacznij_gre == 'Tak':
            imie, nazwisko, wiek = zmienne.pobierz_dane()
            osoba = Osoba(imie, nazwisko, wiek)
            print(osoba.przedstaw_sie())
            rozwiniecie1(imie)
        
    elif zacznij_gre == 'Nie':
        print(f'{Colors.RED}Gra zostaje przerwana.{Colors.END}')
        return None