import cv2
from pyzbar.pyzbar import decode

# Open the video capture
video_capture = cv2.VideoCapture('qrtest.mp4')

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Convert the frame to grayscale (optional, depending on the video)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Decode QR codes from the frame
    decoded_objects = decode(gray_frame)

    # Process the decoded data (e.g., print the data)
    for obj in decoded_objects:
        print('Decoded data:', obj.data.decode('utf-8'))

    # Display the frame
    cv2.imshow('Video', frame)

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
video_capture.release()
cv2.destroyAllWindows()
