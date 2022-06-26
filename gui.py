"""
    Moduł gui
    Gui zostało stworzone za pomocą tkinter
"""
import tkinter
from tkinter import Label, Listbox, Button, Spinbox, Entry, Text
import tkinter.messagebox
from api import moja_nazwa, daj_followy, tweety_os_czasu, tweety_kogos, wyslij_tweeta, \
    dane_uzytkownika, wysz_tweetow, wysz_retweet, wysz_lajk, wysz_follow


def win1():
    """
        Funkcja tworząca okno główne tkinter
    """
    root = tkinter.Tk()
    root.title("Okno główne prymitywnego bota do Twittera")
    root.configure(background='#F0F8FF')
    root.geometry("800x500+300+50")
    root.resizable(False, False)
    Label(root, text='Witaj w oknie prymitywnego bota do Twittera.', bg='#F0F8FF',
          font=('arial', 22, 'bold')).place(x=100, y=50)
    Label(root, text='Wybierz co chcesz zrobić', bg='#F0F8FF',
          font=('arial', 14, 'italic')).place(x=280, y=100)
    lsbox = Listbox(root, bg='#97FFFF', font=('Calibri', 12, 'normal'), width=70, height=10)
    lsbox.insert('0', 'Pokaż moją nazwę użytkownika')
    lsbox.insert('1', 'Wyświetl ostatnie tweety z mojej osi czasu')
    lsbox.insert('2', 'Wyświetl ostatnie tweety danego użytkownika')
    lsbox.insert('3', 'Daj followa wszystkim moim followersom')
    lsbox.insert('4', 'Napisz tweeta')
    lsbox.insert('5', 'Wyświetl dane użytkownika')
    lsbox.insert('6', 'Działania na tweetach')
    lsbox.place(x=100, y=202)
    Button(root, text='Wybierz', bg='#FFF8DC', font=('arial', 12, 'normal'),
           command=lambda: wybor(lsbox.curselection())).place(x=142, y=432)
    Button(root, text='Wyjdz', bg='#ffd8ca', font=('arial', 12, 'normal'),
           command=root.destroy).place(x=220, y=432)
    root.mainloop()


def win2():
    """
        Funkcja tworząca okno, w którym do wyboru jest
        liczba ostatnich tweetów z osi czasu
    """
    okno2 = tkinter.Tk()
    okno2.title("Wyswietl ostatnie tweety z osi czasu")
    okno2.configure(background='#F0F8FF')
    okno2.geometry("500x300+460+200")
    okno2.resizable(False, False)
    Label(okno2, text='Wybierz liczbę tweetow', bg='#F0F8FF', font=('arial', 22, 'bold')).place(
        x=100, y=50)
    Label(okno2, text='Liczba \n tweetów', bg='#F0F8FF',
          font=('arial', 7, 'bold')).place(x=75, y=95)
    l_tweetow = Spinbox(okno2, from_=1, to=20, font=('arial', 12, 'normal'), bg='#F0F8FF', width=10)
    l_tweetow.place(x=126, y=100)
    Button(okno2, text='Wybierz', bg='#FFF8DC', font=('arial', 12, 'normal'), command=
    lambda: [tweety_os_czasu(l_tweetow.get()), okno2.destroy()]).place(x=126, y=132)
    Button(okno2, text='Cofnij', bg='#ffd8ca', font=('arial', 12, 'normal'),
           command=okno2.destroy).place(x=205, y=132)


def win3():
    """
        Funkcja tworząca okno okno, w którym do wyboru jest
        liczba ostatnich tweetów i nazwa uzytkownika
        w celu wyswietlenia jego ostatnich tweetow
    """
    okno3 = tkinter.Tk()
    okno3.title("Wyswietl ostatnie tweety z osi czasu danego uzytkownika")
    okno3.configure(background='#F0F8FF')
    okno3.geometry("500x300+460+200")
    okno3.resizable(False, False)
    Label(okno3, text='Wybierz liczbę tweetow \n oraz nazwę użytkownika', bg='#F0F8FF',
          font=('arial', 22, 'bold')).place(x=50, y=20)
    Label(okno3, text='Liczba \n tweetów', bg='#F0F8FF',
          font=('arial', 7, 'bold')).place(x=75, y=95)
    Label(okno3, text='Nazwa \n użytkownika', bg='#F0F8FF',
          font=('arial', 7, 'bold')).place(x=55, y=125)
    l_tweetow = Spinbox(okno3, from_=1, to=20, font=('arial', 12, 'normal'), bg='#F0F8FF', width=10)
    l_tweetow.place(x=126, y=100)
    nazwa_uz = Entry(okno3, width=20)
    nazwa_uz.place(x=125, y=132)
    Button(okno3, text='Wybierz', bg='#FFF8DC', font=('arial', 12, 'normal'), command=
    lambda: [tweety_kogos(nazwa_uz.get(), l_tweetow.get()), okno3.destroy()]).place(x=126, y=152)
    Button(okno3, text='Cofnij', bg='#ffd8ca', font=('arial', 12, 'normal'),
           command=okno3.destroy).place(x=205, y=152)


def win4():
    """
        Funkcja tworząca okno, w którym wpisuje się treść
        tweeta do wysłania
    """
    okno4 = tkinter.Tk()
    okno4.title("Wyślij tweeta")
    okno4.configure(background='#F0F8FF')
    okno4.geometry("500x300+460+200")
    okno4.resizable(False, False)
    Label(okno4, text='Wpisz treść tweeta', bg='#F0F8FF',
          font=('arial', 22, 'bold')).place(x=120, y=20)
    tresc = Text(okno4, height=9, width=50)
    tresc.place(x=40, y=68)
    Button(okno4, text='Wybierz', bg='#FFF8DC', font=('arial', 12, 'normal'), command=
    lambda: [wyslij_tweeta(tresc.get("1.0", "end-1c")), okno4.destroy()]).place(x=126, y=232)
    Button(okno4, text='Cofnij', bg='#ffd8ca', font=('arial', 12, 'normal'),
           command=okno4.destroy).place(x=205, y=232)


def win5():
    """
        Funkcja tworząca okno do wpisania nazwu użytkownika
        w celu wyświetlenia jego danych
    """
    okno5 = tkinter.Tk()
    okno5.title("Wywietl dane użytkownika")
    okno5.configure(background='#F0F8FF')
    okno5.geometry("500x300+460+200")
    okno5.resizable(False, False)
    Label(okno5, text='Podaj nazwę użytkownika', bg='#F0F8FF',
          font=('arial', 22, 'bold')).place(x=70, y=20)
    Label(okno5, text=' Nazwa \n użytkownika', bg='#F0F8FF',
          font=('arial', 7, 'bold')).place(x=55, y=125)
    nazwa_uz = Entry(okno5, width=20)
    nazwa_uz.place(x=125, y=132)
    Button(okno5, text='Cofnij', bg='#ffd8ca', font=('arial', 12, 'normal'),
           command=okno5.destroy).place(x=220, y=432)
    Button(okno5, text='Wybierz', bg='#FFF8DC', font=('arial', 12, 'normal'), command=
    lambda: [dane_uzytkownika(nazwa_uz.get()), okno5.destroy()]).place(x=126, y=152)
    Button(okno5, text='Cofnij', bg='#ffd8ca', font=('arial', 12, 'normal'),
           command=okno5.destroy).place(x=205, y=152)


def win6():
    """
        Funkcja tworząca okno, w którym użytkownik wpisuje wyszukiwaną frazę,
        liczbę tweetów i wybiera, co chce zrobić
    """
    okno6 = tkinter.Tk()
    okno6.title("Działania na tweetach")
    okno6.configure(background='#F0F8FF')
    okno6.geometry("500x300+460+200")
    okno6.resizable(False, False)
    Label(okno6, text='Wpisz liczbę tweetów, wuszukiwaną frazę \n i co chcesz zrobić', bg='#F0F8FF',
          font=('arial', 12, 'bold')).place(x=90, y=20)
    Label(okno6, text='Wyszukiwana \n fraza', bg='#F0F8FF',
          font=('arial', 7, 'bold')).place(x=55, y=125)
    Label(okno6, text='Liczba \n tweetów', bg='#F0F8FF',
          font=('arial', 7, 'bold')).place(x=75, y=95)
    fraza = Entry(okno6, width=20)
    fraza.place(x=125, y=132)
    l_tweetow = Spinbox(okno6, from_=1, to=20, font=('arial', 12, 'normal'), bg='#F0F8FF', width=10)
    l_tweetow.place(x=126, y=100)
    lsbox = Listbox(okno6, bg='#97FFFF', font=('Calibri', 12, 'normal'), width=51, height=4)
    lsbox.insert('0', 'Wyszukaj i wyświetl tweety po wpisanej frazie')
    lsbox.insert('1', 'Podaj dalej wyszukane tweety po wpisanej frazie')
    lsbox.insert('2', 'Polajkuj wyszukane tweety po wpisanej frazie')
    lsbox.insert('3', 'Daj followa autorom tweetów wyszukanych po wpisanej frazie')
    lsbox.place(x=45, y=162)
    Button(okno6, text='Wybierz', bg='#FFF8DC', font=('arial', 12, 'normal'), command=lambda:
    wybor_okno6(lsbox.curselection(), l_tweetow.get(), fraza.get())).place(x=142, y=255)
    Button(okno6, text='Cofnij', bg='#ffd8ca', font=('arial', 12, 'normal'),
           command=okno6.destroy).place(x=220, y=255)


def wybor(el_wybrany):
    """
        Funkcja, która na podstawie wyboru użytkownika
        wywołuje kolejną funkcję w celu obsługi żądania
        :param el_wybrany: wybrany element
    """
    try:
        if el_wybrany[0] == 0:
            moja_nazwa()
        elif el_wybrany[0] == 1:
            win2()
        elif el_wybrany[0] == 2:
            win3()
        elif el_wybrany[0] == 3:
            daj_followy()
        elif el_wybrany[0] == 4:
            win4()
        elif el_wybrany[0] == 5:
            win5()
        elif el_wybrany[0] == 6:
            win6()
    except IndexError:
        brak_wyboru()


def wybor_okno6(el_wybrany_okno6, liczba, fraza):
    """
        Funkcja, która na podstawie wyboru użytkownika w oknie 6
        wywołuje kolejną funkcję w celu obsługi żądania i dalej podaje
        parametry liczba i fraza
        :param el_wybrany_okno6: wybrany element
        :param liczba: liczba tweetów
        :param fraza: wyszukiwana fraza
    """
    try:
        if el_wybrany_okno6[0] == 0:
            wysz_tweetow(liczba, fraza)
        elif el_wybrany_okno6[0] == 1:
            wysz_retweet(liczba, fraza)
        elif el_wybrany_okno6[0] == 2:
            wysz_lajk(liczba, fraza)
        elif el_wybrany_okno6[0] == 3:
            wysz_follow(liczba, fraza)
    except IndexError:
        brak_wyboru()


def brak_wyboru():
    """
        Komunikat informujący o braku wyboru
        :return:
    """
    tkinter.messagebox.showinfo("Uwaga!",
                                "Musisz coś wybrać!")
