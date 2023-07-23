# qr-vid
A method to extract code from qr codes in a video, print it to the terminal and output it as a text file.


## QR-Vid

This Python script demonstrates how to decode QR codes from a video file and save the decoded data to a text file. It also prints the output to the terminal. It utilizes the `cv2` (OpenCV) library for video processing and the `pyzbar.pyzbar` library for decoding QR codes.

### Requirements

Before running the script, make sure you have the following libraries installed:

- OpenCV (`cv2`)
- pyzbar

You can install the required libraries using `pip`:

```bash
pip install opencv-python
pip install pyzbar
```

### Usage

1. Ensure you have a video file (`qr-test.mkv` in this example) containing QR codes.
2. Place the Python script in the same directory as the video file.

### Running the Script

The script reads the video file frame by frame, converts each frame to grayscale (optional, depending on the video), and decodes any QR codes present in the frame. The decoded data is then saved to a text file (`qr-test-decoded.txt`) for further processing or analysis.

To run the script, open a terminal or command prompt and navigate to the directory containing the Python script and the video file. Then, execute the following command:

```bash
python qr-vid-decode-v1.py
```
or

```bash
python qr-vid-decode-v2.py
```

python qr-vid-decode-v1.py Prints to terminal only.
python qr-vid-decode-v2.py Prints to terminal and outputs to a text file.

### Output

As the script runs, it will display the frames of the video in a window named "Video" and print the decoded data for each QR code found in the frames. The decoded data will also be written to the `qr-test-decoded.txt` text file in the same directory as the script. The script also prints the decoded data to the terminal.

### Exiting the Script

To exit the script, press the 'q' key while the "Video" window is active. The script will stop processing the video and close the window.

### Note

- If you encounter any issues or errors, please make sure you have the required libraries installed and that the video file exists in the specified location.

### Adjusting Playback Speed:

If you want to slow down the video playback, you can increase the delay. For example, setting the delay to 100 milliseconds will slow down the video by a factor of 100: `if cv2.waitKey(100) & 0xFF == ord('q'):`. This will display each frame for approximately 100 milliseconds before moving on to the next frame.

Similarly, if you want to speed up the video playback, you can decrease the delay. For example, setting the delay to 10 microseconds will speed up the video by a factor of 0.01: `if cv2.waitKey(10) & 0xFF == ord('q'):`. Note that setting a very small delay may cause the video to appear choppy.

You can experiment with different delay values to find the playback speed that suits your needs. Keep in mind that if the delay is too small, it may become difficult to interact with the video using the 'q' key to exit the loop, as the program will not have enough time to process the key press.

![Example Image](https://github.com/txtatech/qr-vid/blob/main/qr-vid/qr-vid-decode-example.png)
