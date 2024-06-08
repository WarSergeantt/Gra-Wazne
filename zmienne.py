from colors import Colors



def pobierz_dane():
    print(f'{Colors.BLUE}Witaj! Jeszcze ciebie tutaj nie bylo, wiec przedstaw sie:{Colors.END}')
    imie = input(f"{Colors.MAGENTA}Imię:{Colors.END}{Colors.GREEN}... {Colors.END}")
    nazwisko = input(f"{Colors.MAGENTA}Nazwisko:{Colors.END}{Colors.GREEN} ...{Colors.END}")
    wiek = int(input(f"{Colors.MAGENTA}Wiek:{Colors.END}{Colors.GREEN}... {Colors.END}"))
    return imie, nazwisko, wiek