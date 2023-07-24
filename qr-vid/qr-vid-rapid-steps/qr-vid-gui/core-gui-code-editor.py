import cv2
import logging
from pyzbar.pyzbar import decode
import subprocess
import os
import threading
import wx
import wx.stc as stc
import keyword
import queue

def main():
    # Set up logging
    logging.basicConfig(filename='qr_vid.log', level=logging.INFO)

    # Flag to control the decoding process
    stop_decoding = False

    def decode_qr_codes(video_file_path):
        # Open the video capture
        video_capture = cv2.VideoCapture(video_file_path)

        while True:
            # Check the stop_decoding flag
            if stop_decoding:
                break

            # Read a frame from the video
            ret, frame = video_capture.read()

            # Check if the frame was read successfully
            if not ret:
                break

            # Convert the frame to grayscale (optional, depending on the video)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Decode QR codes from the frame
            decoded_objects = decode(gray_frame)

            # Process the decoded data
            for obj in decoded_objects:
                decoded_data = obj.data.decode('utf-8')
                wx.CallAfter(text_ctrl.AppendText, decoded_data + '\n')

        # Release the video capture
        video_capture.release()

    class Python3CodeEditor(stc.StyledTextCtrl):
        def __init__(self, parent):
            super().__init__(parent)
            self.StyleSetSpec(stc.STC_STYLE_DEFAULT, "size:10,face:Courier New")
            self.StyleClearAll()

            # Python3 styles
            self.StyleSetSpec(stc.STC_P_DEFAULT, "fore:#000000")  # White
            self.StyleSetSpec(stc.STC_P_COMMENTLINE, "fore:#008000,back:#F0FFF0")  # Green
            self.StyleSetSpec(stc.STC_P_NUMBER, "fore:#008080")  # Teal
            self.StyleSetSpec(stc.STC_P_STRING, "fore:#800080")  # Purple
            self.StyleSetSpec(stc.STC_P_CHARACTER, "fore:#800080")  # Purple
            self.StyleSetSpec(stc.STC_P_WORD, "fore:#000080")  # Navy
            self.StyleSetSpec(stc.STC_P_TRIPLE, "fore:#800080")  # Purple
            self.StyleSetSpec(stc.STC_P_TRIPLEDOUBLE, "fore:#800080")  # Purple
            self.StyleSetSpec(stc.STC_P_CLASSNAME, "fore:#0000FF,bold")  # Blue
            self.StyleSetSpec(stc.STC_P_DEFNAME, "fore:#008080,bold")  # Teal
            self.StyleSetSpec(stc.STC_P_OPERATOR, "bold")
            self.StyleSetSpec(stc.STC_P_IDENTIFIER, "")
            self.StyleSetSpec(stc.STC_P_COMMENTBLOCK, "fore:#7F7F7F")  # Grey
            self.StyleSetSpec(stc.STC_P_STRINGEOL, "fore:#000000,back:#E0C0E0,eolfilled")  # Purple-ish

            self.SetLexer(stc.STC_LEX_PYTHON)
            self.SetKeyWords(0, " ".join(keyword.kwlist))

    # Create a new wx App
    app = wx.App()

    # Create a new wx Frame
    frame = wx.Frame(None, title="QR Code Decoder")
    panel = wx.Panel(frame)

    # Create a Python3 code editor
    text_ctrl = Python3CodeEditor(panel)

    def open_file_dialog(event):
        with wx.FileDialog(panel, "Open Video File", wildcard="Video files (*.mkv;*.avi;*.mp4)|*.mkv;*.avi;*.mp4",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            video_file_path = fileDialog.GetPath()
            try:
                # Run the decoding in a new thread to avoid freezing the GUI
                threading.Thread(target=decode_qr_codes, args=(video_file_path,)).start()

            except IOError:
                wx.LogError("Cannot open file '%s'." % video_file_path)

    def run_code(event):
        code = text_ctrl.GetValue()
        try:
            output = subprocess.check_output(['python3', '-c', code])
            print('Output:', output.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print('Error:', e.output.decode('utf-8'))

    run_button = wx.Button(panel, label="Run Code")
    run_button.Bind(wx.EVT_BUTTON, run_code)

    def stop_decoding_gui(event):
        # Set the stop_decoding flag to True to interrupt the decoding process
        global stop_decoding
        stop_decoding = True

    # Create a Stop button
    stop_button = wx.Button(panel, label="Stop")
    stop_button.Bind(wx.EVT_BUTTON, stop_decoding_gui)

    # Create a button for opening the file dialog
    open_file_button = wx.Button(panel, label="Open File")
    open_file_button.Bind(wx.EVT_BUTTON, open_file_dialog)

    # Use a box sizer to lay out the widgets
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(open_file_button, 0, wx.ALL | wx.EXPAND, 5)
    sizer.Add(run_button, 0, wx.ALL | wx.EXPAND, 5)
    sizer.Add(stop_button, 0, wx.ALL | wx.EXPAND, 5)
    sizer.Add(text_ctrl, 1, wx.ALL | wx.EXPAND, 5)
    panel.SetSizer(sizer)

    def on_close(event):
        global stop_decoding

        stop_decoding = True
        frame.Destroy()

    frame.Bind(wx.EVT_CLOSE, on_close)

    frame.Show()

    # Start the wx event loop
    app.MainLoop()

if __name__ == '__main__':
        main()