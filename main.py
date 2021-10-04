waga_paczki = 0
waga_elementu = None
aktualna_waga_paczki = 0
numer_paczki = 0
numer_najlzejszej_paczki = 0
max_waga_paczki = 20
min_waga_elementu = 1
max_waga_elementu = 10
liczba_paczek_wyslanych = 0
liczba_kilogramow_wyslanych = 0
waga_najlzejszej_paczki = 20
liczba_elementow_do_wysylki = int(input('Podaj liczbę elementów do wysyłki:'))

for idx in range(liczba_elementow_do_wysylki):
    waga_elementu = int(input('Podaj wagę elementu: '))
    if waga_elementu == 0:
        break
    elif waga_elementu<1 or waga_elementu>10:
        print("Błędna waga")
        break
    else:
        liczba_kilogramow_wyslanych += waga_elementu
        if aktualna_waga_paczki+waga_elementu <= max_waga_paczki:
            aktualna_waga_paczki += waga_elementu
        else:
            numer_paczki += 1

            if aktualna_waga_paczki < waga_najlzejszej_paczki:
                waga_najlzejszej_paczki = aktualna_waga_paczki
                numer_najlzejszej_paczki = numer_paczki
            aktualna_waga_paczki = waga_elementu

numer_paczki += 1
liczba_paczek_wyslanych = numer_paczki
if liczba_kilogramow_wyslanych == 0:
    liczba_paczek_wyslanych = 0

if aktualna_waga_paczki < waga_najlzejszej_paczki:
    waga_najlzejszej_paczki = aktualna_waga_paczki
    numer_najlzejszej_paczki = numer_paczki

suma_pustych_kilogramow = liczba_paczek_wyslanych*20-liczba_kilogramow_wyslanych
puste_kilogramy_w_najlzejszej = 20 - waga_najlzejszej_paczki

print('Liczba paczek wyslanych to {}, liczba kilogramow wyslanych to {}, suma pustych kilogramow to {},\
numer najlzejszej paczki to {}, sa tam {} puste kilogramy.'
      .format(liczba_paczek_wyslanych, liczba_kilogramow_wyslanych,
     suma_pustych_kilogramow, numer_najlzejszej_paczki,
     puste_kilogramy_w_najlzejszej))
