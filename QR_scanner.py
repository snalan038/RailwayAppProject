import cv2
from pyzbar import pyzbar

def scan_qr_code():
    # Initialize the video capture object
    cap = cv2.VideoCapture(0)

    while True:
        # Read the frame from the video capture
        _, frame = cap.read()

        # Find and decode QR codes
        barcodes = pyzbar.decode(frame)

        # Loop over the detected barcodes
        for barcode in barcodes:
            # Extract the bounding box location of the barcode
            x, y, w, h = barcode.rect

            # Draw a rectangle around the barcode
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Convert the barcode data to a string
            barcode_data = barcode.data.decode("utf-8")
            
            # Print the barcode data
            print("QR Code data:", barcode_data)

            # Add your logic here for processing the barcode data (feedbacks, food orders, complaints, etc.)

        # Display the frame
        cv2.imshow("QR Code Scanner", frame)

        # Wait for 'q' key to be pressed to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the windows
    cap.release()
    cv2.destroyAllWindows()

# Call the scan_qr_code function to start scanning
scan_qr_code()



