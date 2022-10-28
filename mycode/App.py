import wx
import NN

class prg_win(wx.Frame):
    
    def __init__(self, parent, title):
        
        super().__init__(parent, -1, title='prognoz', size=(300, 300))




        menubar = wx.MenuBar()
        
        vkladka = wx.Menu()
        
        item = wx.MenuItem(vkladka, wx.ID_EXIT, "exit", "exit from")
        
        vkladka.Append(item)
        
        menubar.Append(vkladka, "exit")

        self.SetMenuBar(menubar)

        a = "Результат"
        result = ""
        text = ""


        
        
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)



        self.q=wx.StaticText(panel, label="Спад"), 1, wx.EXPAND
        self.w=wx.StaticText(panel, label = a), 2, wx.EXPAND
        self.e=wx.TextCtrl(panel)
        self.r=wx.StaticText(panel, label = "")
        self.t=wx.StaticText(panel, label="Рост"), 5, wx.EXPAND
        self.y=wx.StaticText(panel), 6, wx.EXPAND
        self.u=wx.TextCtrl(panel)
        self.i=wx.StaticText(panel, label = "")
        self.o=wx.StaticText(panel, label="Санкции"), 9, wx.EXPAND
        self.p=wx.StaticText(panel), 10, wx.EXPAND
        self.a=wx.TextCtrl(panel)
        self.s=wx.StaticText(panel, label = "")
        self.d=wx.StaticText(panel, label="Катаклизмы"), 13, wx.EXPAND
        self.f=wx.StaticText(panel), 14, wx.EXPAND
        self.g=wx.TextCtrl(panel)
        self.h=wx.Button(panel, label = "Посчитать"), 16, wx.EXPAND

        self.Bind(wx.EVT_BUTTON, self.Clicked)


                      
        gbox = wx.GridSizer(8, 2, 8, 8)
        gbox.AddMany([self.q,self.w])
        gbox.Add(self.e, flag=wx.EXPAND)
        gbox.AddMany([self.r,self.t,self.y,self.u,self.i,self.o,self.p,self.a,self.s,self.d,self.f,self.g,self.h])
        
        vbox.Add(gbox, proportion = 1,  flag=wx.EXPAND | wx.ALL, border = 20)
        panel.SetSizer(vbox)
        
        self.Centre()




    def Clicked(self, event):
        e_e = self.e.GetValue()
        u_u = self.u.GetValue()
        a_a = self.a.GetValue()
        g_g = self.g.GetValue()
        f = open(r"file.txt", "w")
        f.write(e_e+"\n")
        f.write(u_u+"\n")
        f.write(a_a+"\n")
        f.write(g_g)
        f.close()
        self.r.SetLabel(str(NN.prognoz()))
        


    

         

        

def main():
        
        app = wx.App()
        
        frame = prg_win(None, title="")
        
        frame.Show()
        
        app.MainLoop()
        




if __name__ == '__main__':

    main()
        




