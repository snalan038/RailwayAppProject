import qrcode

def create_multi_data_qr_code(data_list, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    # Add each data point to the QR code
    for data in data_list:
        qr.add_data(data)
    
    qr.make(fit=True)
    
    # Create an image from the QR code
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a file
    qr_img.save(output_path)

# Example usage
data_list = ["food order", "feedback", "complaints"]
output_path = "multi_data_qr_code.png"
create_multi_data_qr_code(data_list, output_path)
