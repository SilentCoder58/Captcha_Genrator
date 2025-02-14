from io import BytesIO
from tkinter import *
from random import randint
from tkinter import messagebox
import string
from captcha.image import ImageCaptcha

# Set the font paths for Linux systems
FONT_PATHS = [
    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
]

# Initialize ImageCaptcha with custom fonts
image = ImageCaptcha(fonts=FONT_PATHS)

# Generate a random 6-digit captcha code
def generate_captcha():
    return str(randint(100000, 999999))

# Generate and save the captcha image
def create_captcha_image(captcha_code):
    image_data = image.generate(captcha_code)
    assert isinstance(image_data, BytesIO)
    image.write(captcha_code, 'captcha.png')

# Verify the user's input against the captcha code
def verify():
    user_input = t1.get("1.0", END).strip()
    if user_input == random_code:
        messagebox.showinfo("Success", "Captcha Verified!")
    else:
        messagebox.showwarning("Error", "Incorrect Captcha!")
        refresh()

# Refresh the captcha code and image
def refresh():
    global random_code
    random_code = generate_captcha()
    create_captcha_image(random_code)
    
    # Update image in Tkinter
    new_photo = PhotoImage(file="captcha.png")
    l1.config(image=new_photo)
    l1.image = new_photo  # Keep reference to avoid garbage collection

# Initialize GUI
root = Tk()
root.title("Captcha Verification")

# Set initial captcha code and image
random_code = generate_captcha()
create_captcha_image(random_code)

photo = PhotoImage(file="captcha.png")
l1 = Label(root, image=photo, height=100, width=200)
t1 = Text(root, height=2, width=15)
b1 = Button(root, text="Submit", command=verify)
b2 = Button(root, text="Refresh", command=refresh)

# Layout setup
l1.pack(pady=10)
t1.pack(pady=5)
b1.pack(pady=5)
b2.pack(pady=5)

root.mainloop()
