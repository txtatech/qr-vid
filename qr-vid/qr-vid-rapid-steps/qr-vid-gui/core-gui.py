import wx
import threading
import core_step_1
import core_step_2
import core_step_3
import core_step_5
import core_step_6

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="QR-VID GUI")

        # Panel
        self.panel = wx.Panel(self)

        # Buttons
        self.button_step_1 = wx.Button(self.panel, label="Generate Code")
        self.button_step_1.Bind(wx.EVT_BUTTON, self.run_step_1)

        self.button_step_2 = wx.Button(self.panel, label="Create JSON")
        self.button_step_2.Bind(wx.EVT_BUTTON, self.run_step_2)

        self.button_step_3 = wx.Button(self.panel, label="Create QR Codes")
        self.button_step_3.Bind(wx.EVT_BUTTON, self.run_step_3)

        self.button_step_5 = wx.Button(self.panel, label="Parse Video Extract SRT")
        self.button_step_5.Bind(wx.EVT_BUTTON, self.run_step_5)

        self.button_step_6 = wx.Button(self.panel, label="Parse Video Write TXT")
        self.button_step_6.Bind(wx.EVT_BUTTON, self.run_step_6)

        self.button_batch = wx.Button(self.panel, label="Run 1-3 In Batch")
        self.button_batch.Bind(wx.EVT_BUTTON, self.run_batch)

        # Sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.button_step_1, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.button_step_2, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.button_step_3, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.button_step_5, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.button_step_6, 0, wx.ALL | wx.EXPAND, 5)
        self.sizer.Add(self.button_batch, 0, wx.ALL | wx.EXPAND, 5)

        self.panel.SetSizer(self.sizer)

    def run_step_1(self, event):
        threading.Thread(target=core_step_1.main).start()

    def run_step_2(self, event):
        threading.Thread(target=core_step_2.main).start()

    def run_step_3(self, event):
        threading.Thread(target=core_step_3.main).start()

    def run_step_5(self, event):
        threading.Thread(target=core_step_5.main).start()

    def run_step_6(self, event):
        threading.Thread(target=core_step_6.main).start()

    def run_batch(self, event):
        threading.Thread(target=self.batch_run).start()

    def batch_run(self):
        core_step_1.main()
        core_step_2.main()
        core_step_3.main()


app = wx.App()
frame = MainFrame()
frame.Show()
app.MainLoop()
