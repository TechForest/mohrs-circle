#!/usr/bin/python
import Tkinter
import tkMessageBox
import math


class Calculations:
    def __init__(self):
        self.sx = 0
        self.sy = 0
        self.txy = 0
        self.r = 0
        self.save = 0
        self.smax = 0
        self.smin = 0
        self.tmax = 0
        self.tetap = 0
        self.tetas = 0

    def run(self, sx, sy, txy, teta=0):
        sin = math.sin
        cos = math.cos
        rad = math.radians
        self.sx = sx
        self.sy = sy
        self.txy = txy
        self.teta = teta
        self.r = 0
        self.save = (self.sx + self.sy)/2.
        self.savem = (self.sx - self.sy)/2.
        self.r = ((((self.sx - self.sy)/2.)**2)+self.txy**2)**0.5
        self.nsx = (self.save + self.savem*cos(rad(2.*teta)) +
                    self.txy*sin(rad(2*teta)))
        self.nsy = (self.save - self.savem*cos(2.*rad(teta)) -
                    self.txy*sin(2.*rad(teta)))
        self.ntxy = -self.savem*sin(2.*rad(teta))+self.txy*cos(2.*rad(teta))
        self.smax = self.save + (((self.savem)**2) + self.txy**2)**0.5
        self.smin = self.save - (((self.savem)**2) + self.txy**2)**0.5
        self.tmax = ((self.savem**2) + self.txy**2)**0.5
        self.tetap = ((math.degrees(math.atan((2.*self.txy) /
                                              (self.sx-self.sy))))/2.)
        self.tetas = ((math.degrees(math.atan(-(self.sx-self.sy) /
                                              (2.*self.txy))))/2.)


class Gui:
    def __init__(self, app):
        self.radius = 0
        app.title("Mohr Circle")
        app.geometry('1100x500')
        calc = Calculations()

        self.frame = Tkinter.Frame(app)
        self.frame.pack(side='right', pady=10)
        self.frame1 = Tkinter.Frame(self.frame)
        self.frame1.pack()
        self.frame2 = Tkinter.Frame(self.frame)
        self.frame2.pack()
        self.frame3 = Tkinter.Frame(self.frame)
        self.frame3.pack()
        self.frame4 = Tkinter.Frame(self.frame)
        self.frame4.pack()

        top_draw_frame = Tkinter.Frame(app)
        top_draw_frame.pack(expand=Tkinter.YES, fill=Tkinter.BOTH, side='left')

        label_text = Tkinter.StringVar()

        label_text = Tkinter.StringVar()
        label_text.set(u"\u03C3x")
        label1 = Tkinter.Label(self.frame1, textvariable=label_text, height=2)
        label1.pack(side='left', padx=7)
        cust_name = Tkinter.StringVar(None)
        self.entry1 = Tkinter.Entry(self.frame1,
                                    textvariable=cust_name, width=15)
        self.entry1.pack(side='left')

        label_text2 = Tkinter.StringVar()
        label_text2.set(u"\u03C3y")
        label2 = Tkinter.Label(self.frame2, textvariable=label_text2, height=2)
        label2.pack(side='left', padx=7)
        cust_name2 = Tkinter.StringVar(None)
        self.entry2 = Tkinter.Entry(self.frame2,
                                    textvariable=cust_name2, width=15)
        self.entry2.pack(side='left')

        label_text3 = Tkinter.StringVar()
        label_text3.set(u"\u03C4xy")
        label3 = Tkinter.Label(self.frame3, textvariable=label_text3, height=2)
        label3.pack(side='left', padx=5)
        cust_name3 = Tkinter.StringVar(None)
        self.entry3 = Tkinter.Entry(self.frame3,
                                    textvariable=cust_name3, width=15)
        self.entry3.pack(side='left')

        label_text4 = Tkinter.StringVar()
        label_text4.set(u"\u03B8")
        label4 = Tkinter.Label(self.frame4, textvariable=label_text4, height=2)
        label4.pack(side='left', padx=12)
        cust_name4 = Tkinter.StringVar(None)
        self.entry4 = Tkinter.Entry(self.frame4,
                                    textvariable=cust_name4, width=15)
        self.entry4.pack(side='left')
        button1 = Tkinter.Button(self.frame, text="OK", width=10,
                                 command=self.execute)
        button1.pack(padx=10, pady=10)

        menu_bar = Tkinter.Menu(app)
        file_menu = Tkinter.Menu(menu_bar, tearoff=0)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=app.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        about_menu = Tkinter.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label="About the app", command=self.new_window)
        menu_bar.add_cascade(label="About", menu=about_menu)
        app.config(menu=menu_bar)
        # left canvas
        self.canvas = Tkinter.Canvas(top_draw_frame, width=450,
                                     height=500, bg='white')
        self.canvas.pack(side='left')
        # self.canvas.pack(side='left', expand=Tkinter.YES, fill=Tkinter.BOTH)
        h = self.canvas.winfo_reqheight()
        w = self.canvas.winfo_reqwidth()
        print w, h
        self.canvas.create_oval(60, 60, 400, 400, width=2,
                                fill='blue', tag='circle')
        radius = (400 - 60)/2
        self.canvas.create_line(60+radius, 60+radius,
                                400, 100, width=3, fill='red')

        self.canvas2 = Tkinter.Canvas(top_draw_frame, width=450,
                                      height=500, bg='white')
        self.canvas2.create_oval(60, 60, 400, 400, width=2,
                                 fill='blue', tag='circle')
        self.canvas2.pack(side='left')
        # self.canvas3.pack(side='left', expand=Tkinter.YES, fill=Tkinter.BOTH)

        self.canvas1 = Tkinter.Canvas(self.frame, width=200,
                                      height=400, bg='#f0f0f0')
        # xo,yo,x1,y1
        self.canvas1.create_rectangle(60, 100, 140, 180,
                                      fill='#b4b4ff', width=1)
        self.canvas1.pack(expand=Tkinter.YES, fill='both')
        calc.run(100., 60., -48., 30.)
        print 'tetap = '+str(calc.tetap)
        print 'tetas = '+str(calc.tetas)
        print 'smax = '+str(calc.smax)
        print 'smin = '+str(calc.smin)
        print 'tmax = '+str(calc.tmax)
        print 'smed = '+str(calc.save)
        print 'r = '+str(calc.r)
        print 'nsx = '+str(calc.nsx)
        print 'nsy = '+str(calc.nsy)
        print 'ntxy = '+str(calc.ntxy)

    def execute(self):
        try:
            string_input = self.entry1.get()
            self.radius = int(string_input)
            self.build_canvas(self.radius)
        except ValueError:
            self.wrong_value()

    def wrong_value(self):
        tkMessageBox.showinfo("Status",
                              "Please insert only numbers!")

    def new_window(self):
        top = Tkinter.Toplevel()
        top.title("About the app")
        top.geometry('380x80')
        label_text = Tkinter.StringVar()
        label_text.set("App developed by Estevao Fonseca")
        label1 = Tkinter.Label(top, textvariable=label_text, height=2)
        label1.pack(side='top', padx=10, pady=15)
        top.mainloop()

    def build_canvas(self, radius):
        self.canvas.delete('circle')
        self.canvas.create_oval(10, 10, radius, radius, width=2,
                                fill='blue', tag='circle')
        self.canvas.create_line(100, 100, 200, 300, width=3, fill='red')

app = Tkinter.Tk()
Gui(app)
app.mainloop()
