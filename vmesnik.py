import program as pr
import tkinter as tk
import os

okno = tk.Tk()
okno.title('Mali stavni pomočnik')

vpis = tk.Entry(okno)
vpis.grid(row =  1,column = 0 )

gumb1 = tk.Button(okno, text = 'Poraz', command = pr.poraz('nova1.txt'))
gumb1.grid(row = 0, column = 1)
gumb2 = tk.Button(okno, text = 'Zmaga', command = pr.zmaga('nova1.txt'))
gumb2.grid(row = 1, column = 1)
gumb3 = tk.Button(okno, text = 'Remi', command = pr.remi('nova1.txt'))
gumb3.grid(row = 2, column = 1)
gumb4 = tk.Button(okno, text = 'Igra doma', command = pr.domač('nova2.txt'))
gumb4.grid(row = 0, column = 2)
gumb5 = tk.Button(okno, text = 'Igra v Gosteh', command = pr.gost('nova2.txt'))
gumb5.grid(row = 1, column = 2)
gumb6 = tk.Button(okno, text = 'Dodaj',
                  command = pr.seznam_stav('stava.txt',
                                           'str',
                                           pr.vrnjeni_rezultati('nova1.txt'),
                                           pr.kraj('nova2.txt')))
gumb6.grid(row = 1, column = 3)
gumb7 = tk.Button(okno, text = 'Izpiši', command = pr.celota('stava.txt'))
gumb7.grid(row = 1, column = 4)
gumb8 = tk.Button(okno, text = 'Izbriši', command = pr.izbris('nova1.txt',
                                                              'nova2.txt',
                                                              'stava.txt'))
gumb8.grid(row = 1, column = 5)

vpis = tk.Entry(okno)
vpis.grid(row =  1,column = 0 )

okno.mainloop()
