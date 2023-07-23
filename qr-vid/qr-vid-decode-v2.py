import cv2
from pyzbar.pyzbar import decode

# Open the video capture
video_capture = cv2.VideoCapture('qr-test.mkv')

# Open the text file for appending
with open('qr-test-decoded.txt', 'a') as file:
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

        # Process the decoded data and write to the text file
        for obj in decoded_objects:
            decoded_data = obj.data.decode('utf-8')
            print('Decoded data:', decoded_data)
            file.write(decoded_data + '\n')

        # Display the frame
        cv2.imshow('Video', frame)

        # Exit the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture and close the window
video_capture.release()
cv2.destroyAllWindows()
