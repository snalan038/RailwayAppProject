from flask import Flask, render_template,request
import cv2
from pyzbar import pyzbar
from twilio.rest import Client



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('qr.html')
    
@app.route('/my-link/')
def my_link():
    # Initialize the video capture object
    cap = cv2.VideoCapture(0)

    while True:
        # Read the frame from the video capture, 
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
            #Qprint("QR Code data:", barcode_data)
            return render_template('index.html', value=barcode_data)

            # Add your logic here for processing the barcode data (feedbacks, food orders, complaints, etc.)

        # Display the frame
        cv2.imshow("QR Code Scanner", frame)

        # Wait for 'q' key to be pressed to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the windows
    cap.release()
    cv2.destroyAllWindows()

@app.route('/process_data', methods=['POST','GET'])
def process_data():
    my_value = request.form['user']
    account_sid = 'AC15a309f87fe39cb4cef52435e31fcc24'
    auth_token = 'dc9a72bdce30b91b8ad7808abc430c8e'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=my_value,
        from_='+12542564301',
        to='+919344929070'
    )
    print(message.sid)


if __name__ == '__main__':
    app.run(debug=True)
