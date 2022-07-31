# BluNate 2022
# oof.py

# import
import tkinter
import os
import sys
import shutil
from tkinter import ttk, messagebox, filedialog
from tkinter import *
from PyLnk import Lnk

# def


def move_window(event):  # Allow window moving
    T.geometry(f'+{event.x_root}+{event.y_root}')


def resoof():
    global filename
    filename = f'{opath}\oof.ogg'
    T.destroy()


path = f'{os.getenv("APPDATA")}\Microsoft\Windows\Start Menu\Programs\Roblox'
lnk = Lnk(f'{path}\Roblox Player.lnk')
path = f'{os.path.split(lnk.path)[0]}/content/sounds/ouch.ogg'

opath = f'{os.getcwd()}/'
pict = f'{os.environ["HOMEPATH"]}\Downloads'


def select():
    global filename
    filename = filedialog.askopenfilename(
        title='Select Sound', initialdir=pict, filetypes=(('OGG sound files', '*.ogg'),))
    if filename == '':
        messagebox.showerror("Error", "Please select a file")
        sys.exit()
    T.destroy()


T = Tk()
T.overrideredirect(1)
T.eval('tk::PlaceWindow . center')
T.tk.call('wm', 'iconphoto', T._w, PhotoImage(file=f'{opath}icon.png'))

# define styles
T['bg'] = '#111'
Style = ttk.Style()
Style.theme_use('alt')
Style.configure("TLabel", font=('corbel', 12),
                background="#333", foreground='#ddd')
Style.configure("TButton", font=('corbel', 12),
                background="#333", foreground='#ddd')
Style.configure("TFrame", background="#333")
Style.configure("TNotebook", background="#111")
Style.configure("TNotebook.Tab", background='#222', foreground='#ddd')
Style.map("TNotebook.Tab", background=[
          ("selected", '#333')], foreground=[("selected", '#ddd')])
Style.map('TButton', background=[
          ('active', '#111'), ('disabled', '#111')], foreground=[('disabled', '#555')])

# define variables
tab = ttk.Notebook(T)

# top bar code
main = ttk.Frame(tab)
repl = ttk.Frame(tab)
logoimage = PhotoImage(file=f'{opath}icon.png')
Label(T, image=logoimage, background='#111',
      foreground='#ddd').grid(column=0, row=0, sticky='W')
Label(T, text='Restore oof sound', background='#111',
      foreground='#ddd', font=('corbel', 12)).grid(column=0, row=0)
Label(T, image=logoimage, background='#111',
      foreground='#ddd').grid(column=0, row=0, sticky='E')
tab.add(main, text='oof')
tab.grid(column=0, row=1)

# main window
ttk.Label(main, text='Restore the roblox death sound to the original').pack()
ttk.Label(main, text='oof sound, or a sound of your choice!').pack()
ttk.Label(main, text='').pack()
ttk.Button(main, text='Select a sound', command=select).pack(side=tkinter.LEFT)
ttk.Button(main, text='Restore oof', command=resoof).pack(side=tkinter.RIGHT)
ttk.Button(main, text='Cancel', command=sys.exit).pack()

#bind and loop
T.bind("<Return>", sys.exit)
T.bind("<Control-B1-Motion>", move_window)
T.mainloop()

shutil.copyfile(filename, path)
