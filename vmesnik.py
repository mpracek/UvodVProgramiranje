import program
import tkinter as tk

def odpri():
    

    window = tk.Toplevel(okno)

okno = tk.Tk()
gumb = tk.Button(okno, text='''S klikom na ta gumb razumem in se strinjam,
da pisec tega programa ni kriv za kakršno koli fizično ali psihično škodo''' ,
                 command = odpri)
gumb.pack()


okno.mainloop()



