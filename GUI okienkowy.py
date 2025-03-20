import tkinter as tk
from tkinter import ttk, scrolledtext, Menu, messagebox, Spinbox

win = tk.Tk()
win.title("Witaj w GUI")

# Rozciąganie okna jest opcjonalne
# win.resizable(1,1)

# Tworzenie zakładek w programie
zakladki = ttk.Notebook(win)

# Tworzenie pierwszej zakładki
zakladka1 = ttk.Frame(zakladki)
zakladki.add(zakladka1, text='Tab1')

# Tworzenie drugiej zakładki
zakladka2 = ttk.Frame(zakladki)
zakladki.add(zakladka2, text='Tab2')
zakladki.pack(expand=1, padx=10, pady=10)  # Wyświetlanie zakładek z marginesami

# Ramka w zakładce 1
frame = ttk.LabelFrame(zakladka1)
frame.grid(column=0, row=0)

# Główna ramka z etykietą w zakładce 1
mainFrame = ttk.LabelFrame(zakladka1, text="++++++++++++++++Ramka etykiety głównej 1++++++++++++++++")
mainFrame.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

# Główna ramka z etykietą w zakładce 2
mainFrame2 = ttk.LabelFrame(zakladka2, text="++++++++++++++++Ramka etykiety głównej 2++++++++++++++++")
mainFrame2.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

# Dodanie etykiety dla pola tekstowego
etykieta1 = ttk.Label(mainFrame, text="Podaj swoje imie")
etykieta1.grid(column=0, row=0)
etykieta1.configure(foreground='blue')  # Zmiana koloru czcionki na niebieski

# Pole tekstowe do wprowadzania imienia
imie = tk.StringVar()
imie_wprowadzona = ttk.Entry(mainFrame, width=20, textvariable=imie)
imie_wprowadzona.grid(column=0, row=1, sticky= 'WE')
imie_wprowadzona.focus()

# Dodanie etykiety dla pola wyboru
wybor = ttk.Label(mainFrame, text="Wybierz numer:")
wybor.grid(column=1, row=0)
wybor.configure(foreground='green')  # Zmiana koloru czcionki na zielony

# Pole wyboru numeru
numer = tk.StringVar()
wybierz_numer = ttk.Combobox(mainFrame, width=20, textvariable=numer, state='readonly')
wybierz_numer['values'] = ("1","2","3","4","5","6","7","8","9")  # Możliwe wartości
wybierz_numer.grid(column=1, row=1, sticky= 'WE')
wybierz_numer.current(0)  # Ustawienie domyślnej wartości na 1

# Funkcja obsługująca kliknięcie przycisku
def kliknij():
    przycisk.configure(text="** Zostałem kliknięty **")
    etykieta1.configure(foreground='red')
    etykieta1.configure(text="Witaj " + imie.get() + ", twoja liczba to " + wybierz_numer.get())

# Dodanie przycisku, który wywołuje funkcję kliknij()
przycisk = ttk.Button(mainFrame, text="Kliknij mnie",  command=kliknij)
przycisk.grid(column=2, row=1, sticky= 'WE')

# Dodanie zablokowanego checkboxa
checkDis = tk.IntVar()
check1 = tk.Checkbutton(mainFrame, text="Zablokowany", variable=checkDis, state='disabled')
check1.select()
check1.grid(column=0, row=2, sticky=tk.W)

# Dodanie odznaczonego checkboxa
checkUn = tk.IntVar()
check2 = tk.Checkbutton(mainFrame, text="Odznaczony", variable=checkUn)
check2.deselect()
check2.grid(column=1, row=2, sticky=tk.W)

# Dodanie zaznaczonego checkboxa
checkEn = tk.IntVar()
check3 = tk.Checkbutton(mainFrame, text="Odblokowany", variable=checkEn)
check3.select()
check3.grid(column=2, row=2, sticky=tk.W)

# Dodanie Spinboxa do wprowadzania liczby
spin = Spinbox(mainFrame2, from_=0, to=100, bd=4)
spin.grid(column=0, row=1, columnspan=3)

# Funkcja zmieniająca kolor okna na podstawie wybranego radia
kolory = ["Blue", "Red", "Green"]
def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background=kolory[0])
    elif radSel == 1:
        win.configure(background=kolory[1])
    elif radSel == 2:
        win.configure(background=kolory[2])

# Zmienna do przechowywania wyboru koloru
radVar = tk.IntVar()
radVar.set(99)  # Wartość domyślna (nieużywana)
for kolor in range(3):
    rad = 'rad' + str(kolor)
    rad = tk.Radiobutton(mainFrame2, text=kolory[kolor], variable=radVar, value=kolor, command=radCall)
    rad.grid(column=kolor, row=0, sticky=tk.W)

# Dodanie przewijanego tekstu
przewinS = 30  # Szerokość
przwinW = 3  # Wysokość
przewin = scrolledtext.ScrolledText(mainFrame, width=przewinS, height=przwinW, wrap=tk.WORD)
przewin.grid(column=0, row= 3, columnspan=3, sticky= 'WE')

# Dodanie etykiety z ramką
ramka = ttk.LabelFrame(mainFrame, text='------------Ramka------------')
ramka.grid(column=0, row=5, columnspan=3)

# Dodanie etykiet w ramce
ttk.Label(ramka, text="Etykieta1").grid(column=0, row=0)
ttk.Label(ramka, text="Etykieta2").grid(column=0, row=1)
ttk.Label(ramka, text="Etykieta3").grid(column=0, row=2)

# Funkcja zamykająca program
def quit():
    win.quit()
    win.destroy()
    exit()

# Menu główne
menu1 = Menu(win)
win.config(menu=menu1)

# Funkcja pokazująca ostrzeżenie
def ostrzerzenie():
    messagebox.showwarning('Ostrzeżenie', 'Nie można tego zrobić')

# Funkcja pokazująca błąd
def blad():
    messagebox.showerror('Uwaga', 'Właśnie wychodzisz z programu')

# Elementy menu
fileMenu = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Plik", menu=fileMenu)
fileMenu.add_command(label="Nowy", command=ostrzerzenie)
fileMenu.add_separator()
fileMenu.add_command(label="Test", command=blad)
fileMenu.add_command(label="Wyjście", command=quit)

# Funkcja pokazująca wiadomość
def wiadomosc():
    messagebox.showinfo('Wiadomość', 'To jest twój program')

# Menu 'About' z pomocą
helpMenu = Menu(menu1, tearoff=0)
menu1.add_cascade(label="O programie", menu=helpMenu)
helpMenu.add_command(label="Pomoc", command=wiadomosc)

# Uruchomienie głównej pętli aplikacji
win.mainloop()