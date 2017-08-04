import program as pr
import tkinter as tk

#def odpri():
 #   okno = tk.Tk()
  #  okno.mainloop()

#window = tk.Toplevel(okno)
#gumb = tk.Button(okno, text='''S klikom na ta gumb razumem in se strinjam,
#da pisec tega programa ni kriv za kakršno koli fizično ali psihično škodo''' ,
#                command = odpri)
#gumb.pack()


okno = tk.Tk()
okno.title('Mali stavni pomočnik')
#okno.geometry('300x300')

vpis = tk.Entry(okno)
vpis.grid(row =  1,column = 0 )

gumb1 = tk.Button(okno, text = 'Poraz', command = pr.poraz())
gumb1.grid(row = 0, column = 1)
gumb2 = tk.Button(okno, text = 'Zmaga', command = pr.zmaga())
gumb2.grid(row = 1, column = 1)
gumb3 = tk.Button(okno, text = 'Remi', command = pr.remi())
gumb3.grid(row = 2, column = 1)
gumb4 = tk.Button(okno, text = 'Igra doma')
gumb4.grid(row = 0, column = 2)
gumb5 = tk.Button(okno, text = 'Igra v Gosteh')
gumb5.grid(row = 1, column = 2)
gumb6 = tk.Button(okno, text = 'Dodaj')
                  #command = pr.seznam_stav(tk.Entry())
gumb6.grid(row = 1, column = 3)
gumb7 = tk.Button(okno, text = 'Izpiši', command = pr.celota('stava.txt'))
gumb7.grid(row = 1, column = 4)
gumb8 = tk.Button(okno, text = 'Izbriši', command = pr.izbris('stava.txt'))
gumb8.grid(row = 1, column = 5)

#oznaka1 = tk.Label(okno, text = '''Izberi zadnjih pet rezultatov
 #                                   med možnostmi poraz, zmaga ali remi.''')
#oznaka1.grid(row = 2, column = 2 )
#oznaka2 = tk.Label(okno, text = '''Med možnostima igra doma ter igra v gosteh
 #                                   izberi tisto, ki drži.''')
#oznaka2.grid(row = 2 ,column = 4 )

vpis = tk.Entry(okno)
vpis.grid(row =  1,column = 0 )

okno.mainloop()
