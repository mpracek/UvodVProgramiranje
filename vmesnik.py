import program
import tkinter as tk

def odpri():
    okno.bind('<Button-1>'

okno = tk.Tk()
gumb = tk.Button(okno, text='S klikom na ta gumb razumem in se strinjam,' /n
                 'da pisec tega programa ni kriv za kakršno koli fizično ali psihično škodo',
                 command = odpri())
gumb.pack()
okno1 = tk.Tk()
okno2 = tk.Tk()

okno.mainloop()
okno1.mainloop()
okno2.mainloop()


