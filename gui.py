from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import sys

from trans import translate
from voice import voice
from counter import wr, r
import setting


class App(tk.Tk):

    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.title('translate')
        self.geometry('600x300')
        self.attributes('-alpha', 1)#прозрачность
        self.attributes('-topmost', True)#поверх окон
        self.overrideredirect(False)# нельзя закрыть
        self.resizable(True, True)# нельзя изменить размер окна
        self.count = int(r())
        ttk.Style().theme_use("vista")
        self.configure(bg='black')
        self.exit_button()
        self.get_text()
        self.setting()
        self.bind('<Return>', self.callbackFunc)
        self.bind('</>', self.callbackFunc)



    def get_text(self):

        self.name_var=tk.StringVar()
        self.space2_var=tk.StringVar()
        self.scale = tk.DoubleVar()
        self.name_label = tk.Label(self, text = 'Вход', font=('calibre',20, 'bold'), bg='black', fg='blue')
        name_entry = tk.Entry(self,textvariable = self.name_var,bg='#660b04', font=('calibre',20,'normal'))

        self.space2_label = tk.Label(self, text = 'Выход', font = ('calibre',20,'bold'), bg='black', fg='red')
        space2_entry=tk.Entry(self, textvariable = self.space2_var,bg='#660b04', font = ('calibre',20,'normal'))

        self.count_label = tk.Label(self, text=self.count,  font=('calibre',20, 'bold'), bg='black', fg='purple')
        self.sub_btn=tk.Button(self,text = 'Submit', command = self.submit, bg='black', fg='white')
        self.voice_btn=tk.Button(self,text='🔊', command=self.voice_line, bg='black', fg='white')
        self.save_btn=tk.Button(self, text='📥', command=self.save, bg='black', fg='white')
        self.clear_btn = tk.Button(self, text = '♻️', command=self.clear, bg='black', fg='white')
        self.scale_line = tk.Scale(self,setting.scale_sets, variable=self.scale)

        self.name_label.pack()
        name_entry.pack()
        self.space2_label.pack()
        space2_entry.pack()
        self.sub_btn.pack()
        self.voice_btn.place(x= 240, y= 172)
        self.save_btn.place(x= 4, y=13)
        self.count_label.place(x= 35, y= 10)
        self.clear_btn.place(x= 330, y=172)
        self.scale_line.place(x= 370, y= 175)


    # def book(self):
    #     self.notebook = ttk.Notebook(self, )



    def submit(self):
        word1=self.name_var.get()
        word2=self.space2_var.get()
        if word1 != '':
            self.space2_var.set(translate(word1))
        elif word2 != '':
            self.name_var.set(translate(word2))



    def voice_line(self):
        line=self.name_var.get()
        voice(line)



    def save(self):
        word1=self.name_var.get()
        word2=self.space2_var.get()
        if word1 and word2 != '':
            try:
                with open('eng_words.txt', mode='a',encoding='utf-8') as file:
                    file.write(self.space2_var.get() + ' ' *100 + self.name_var.get() + '\n')
                    self.count += 1
                    wr(str(self.count))
                    self.count_label['text'] = self.count

            except (FileNotFoundError, IOError) as ex:
                messagebox.showerror('Error', ex)






    def clear(self):
        self.name_var.set("")
        self.space2_var.set("")
        self.attributes('-alpha', float(self.scale.get())/100)
        self.scale_line.set(30)
        self.update()






    def callbackFunc(self, event):
        strn = str(event)


        strn = strn.split()[3].lstrip('keysym=')

        if strn == 'Return':
            self.submit()
        elif strn == "lash":
            self.clear()

        if self.combo_win.current() == 0:
            self.configure(bg='black')
            self.name_label['bg'] = 'black'
            self.space2_label['bg'] = 'black'
            self.hi_there['bg'] = 'red'

        elif self.combo_win.current() == 1:
            messagebox.showwarning('warring', 'too bright')
            self.configure(bg='white')
            self.name_label['bg'] = 'white'
            self.space2_label['bg'] = 'white'
            self.hi_there['bg'] = 'white'

        elif self.combo_win.current() == 2:
            self.attributes('-alpha', 0.1)#прозрачность
            self.scale_line.set(10)
        elif self.combo_win.current() == 3:
            self.attributes('-alpha', 0.3)#прозрачность
            self.scale_line.set(30)
        elif self.combo_win.current() == 4:
            self.attributes('-alpha', 0.5)#прозрачность
            self.scale_line.set(50)
        elif self.combo_win.current() == 5:
            self.attributes('-alpha', 1)#прозрачность
            self.scale_line.set(100)





    def setting(self):


        self.combo_win = ttk.Combobox(self,
                                    values=["night", "day", "0.1", "0.3", "0.5", "1"],
                                    width=15, state='readonly', background='black')

        self.combo_win.current(0)
        self.combo_win.pack(side=tk.LEFT)
        self.combo_win.bind("<<ComboboxSelected>>", self.callbackFunc)

    def exit_button(self):
        self.hi_there = tk.Button(self, text='⚠️', command=self.app_exit, bg='red', activebackground='purple')
        self.hi_there.pack(side="bottom")




    def app_exit(self):
        ask = messagebox.askyesno('Вопрос', 'Do you want to exit?')

        if ask == True:


            self.destroy()
            sys.exit()
        else:
            messagebox.showinfo('info', 'Ok')















