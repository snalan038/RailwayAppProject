import qrcode

def generate_qr_code(data_list):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    for data in data_list:
        qr.add_data(data)
    
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save("multi_data_qr_code.png")

# Example usage
data_list = ["Train Number: 1645\nName: Selva\nCompartment Number: 7\nSeat Number: 14"]
generate_qr_code(data_list)
