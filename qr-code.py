import tkinter as tk
import qrcode
from PIL import ImageTk

# define the generate_qr function
def generate_qr():
    # get the input URL from the user
    url = url_entry.get()

    # generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # convert the QR code image to a PhotoImage and display it in the GUI
    photo_img = ImageTk.PhotoImage(img)
    qr_code.configure(image=photo_img)
    qr_code.image = photo_img

# create the main window
root = tk.Tk()
root.title("QR Code Generator")

# create the input label and entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(side="left")
url_entry = tk.Entry(root, width=50)
url_entry.pack(side="left")

# create the generate button
generate_button = tk.Button(root, text="Generate", command=generate_qr)
generate_button.pack(side="left")

# create the QR code image label
qr_code = tk.Label(root)
qr_code.pack()

# run the GUI
root.mainloop()
