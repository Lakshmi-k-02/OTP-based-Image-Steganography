from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from io import BytesIO
import os
import random

class Stegno:

    art = ''
    art2 = ''
    output_image_size = 0
    generated_otp = None  # Variable to store the OTP for validation during decoding

    def main(self, root):
        root.title('Image Steganography')
        root.geometry('500x600')
        root.resizable(width=False, height=False)
        f = Frame(root, bg='#C71585', padx=30, pady=180)

        title = Label(f, text='Image Steganography', fg='black', bg='#FFB6C1')
        title.config(font=('Times new roman', 36, 'italic'))
        title.grid(pady=10)

        b_encode = Button(f, text="Encode", command=lambda: self.frame1_encode(f), padx=14, fg='black', bg='#FFB6C1', font=('Times news roman', 14, 'italic'))
        b_encode.grid(row=2, pady=12)

        b_decode = Button(f, text="Decode", padx=14, command=lambda: self.frame1_decode(f), fg='black', bg='#FFB6C1', font=('Times news roman', 14, 'italic'))
        b_decode.grid(row=3, pady=12)


        f.grid(row=0, column=0, sticky="nsew")
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

    def home(self, frame):
        frame.destroy()
        self.main(root)

    def frame1_decode(self, f):
        f.destroy()
        d_f2 = Frame(root, bg='#BC8F8F', padx=10, pady=180)

        

        l1 = Label(d_f2, text='Select Image with Hidden text:', font=('Times new roman', 22, 'italic'), fg='Black', bg='#BC8F8F')
        l1.grid()

        bws_button = Button(d_f2, text='Select', command=lambda: self.frame2_decode(d_f2), fg='black', bg='#DEB887', font=('courier', 18, 'bold'))
        bws_button.grid()

        back_button = Button(d_f2, text='Cancel', command=lambda: Stegno.home(self, d_f2), fg='black', bg='#DEB887', font=('courier', 18, 'bold'))
        back_button.grid(pady=15)

        d_f2.grid()

    def frame2_decode(self, d_f2):
        d_f3 = Frame(root, bg='#ffeb3b', padx=10, pady=10)
        myfile = tkinter.filedialog.askopenfilename(filetypes=[('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')])
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)

            l4 = Label(d_f3, text='Selected Image :', font=('Times new roman', 18, 'bold'), fg='black', bg='#ffeb3b')
            l4.grid()
            panel = Label(d_f3, image=img, bg='#ffeb3b')
            panel.image = img
            panel.grid()

            # Prompt for OTP here
            otp_input = simpledialog.askstring("OTP", "Enter the OTP to decode the message:")
            if otp_input != Stegno.generated_otp:
                messagebox.showerror("Error", "Invalid OTP! Cannot decode message.")
                return

            hidden_data = self.decode(myimg)
            l2 = Label(d_f3, text='Hidden data is :', font=('Times new roman', 18, 'bold'), fg='black', bg='#ffeb3b')
            l2.grid(pady=10)
            text_area = Text(d_f3, width=30, height=10, bg='#ffffff', font=('Times new roman', 12))
            text_area.insert(INSERT, hidden_data)
            text_area.configure(state='disabled')
            text_area.grid()

            back_button = Button(d_f3, text='Cancel', command=lambda: self.page3(d_f3), fg='white', bg='#800080', font=('Times new roman', 11, 'bold'))
            back_button.grid(pady=15)

            show_info = Button(d_f3, text='More Info', command=self.info, fg='white', bg='#800080', font=('Times new roman', 11, 'bold'))
            show_info.grid()

            d_f3.grid(row=1)
            d_f2.destroy()

    def decode(self, image):
        data = ''
        imgdata = iter(image.getdata())

        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
                      imgdata.__next__()[:3] +
                      imgdata.__next__()[:3]]
            binstr = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return data



    def frame1_encode(self, f):
        f.destroy()
        f2 = Frame(root, bg='#E9967A', padx=60, pady=180)

        

        l1 = Label(f2, text='Select the Image in which\n you want to hide text :', font=('Times new roman', 22, 'italic'), fg='black', bg='#E9967A')
        l1.grid()

        bws_button = Button(f2, text='Select', command=lambda: self.frame2_encode(f2), fg='black', bg='#CD5C5C', font=('Times new roman', 18, 'bold'))
        bws_button.grid()

        back_button = Button(f2, text='Cancel', command=lambda: Stegno.home(self, f2), fg='black', bg='#CD5C5C', font=('Times new roman', 18, 'bold'))
        back_button.grid(pady=15)

        f2.grid()

    def frame2_encode(self, f2):
        ep = Frame(root, bg='#9ACD32', padx=10, pady=10)
        myfile = tkinter.filedialog.askopenfilename(filetypes=[('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')])
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((250, 150))
            img = ImageTk.PhotoImage(myimage)
            l3 = Label(ep, text='Selected Image', font=('Times new roman', 18, 'bold'), fg='black', bg='#9ACD32')
            l3.grid()
            panel = Label(ep, image=img, bg='#9ACD32')
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()

            l2 = Label(ep, text='Enter the message', font=('Times new roman', 18, 'bold'), fg='black', bg='#9ACD32')
            l2.grid(pady=15)

            text_area = Text(ep, width=40, height=8, bg='#ffffff', font=('Times new roman', 12))
            text_area.grid()

            # Generate OTP
            Stegno.generated_otp = self.generate_otp()

            otp_label = Label(ep, text=f"OTP: {Stegno.generated_otp}", font=('Times new roman', 12, 'bold'), fg='#000000', bg='#9ACD32')
            otp_label.grid(pady=10)

            back_button = Button(ep, text='Encode', command=lambda: [self.enc_fun(text_area, myimg), Stegno.home(self, ep)], fg='white', bg='#006400', font=('Times new roman', 11, 'bold'))
            back_button.grid(pady=15)

            encode_button = Button(ep, text='Cancel', command=lambda: Stegno.home(self, ep), fg='white', bg='#006400', font=('Times new roman', 11, 'bold'))
            encode_button.grid()

            ep.grid(row=1)
            f2.destroy()

    def generate_otp(self):
        """Generates a 4-digit random OTP."""
        otp = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        return otp

    def info(self):
        try:
            str = 'original image:-\nsize of original image:{}mb\nwidth: {}\nheight: {}\n\n' \
                  'decoded image:-\nsize of decoded image: {}mb\nwidth: {}' \
                '\nheight: {}'.format(self.output_image_size.st_size/1000000,
                                    self.o_image_w,self.o_image_h,
                                    self.d_image_size/1000000,
                                    self.d_image_w,self.d_image_h)
            messagebox.showinfo('info',str)
        except:
            messagebox.showinfo('Info','Unable to get the information')

    def genData(self,data):
        newd = []
        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def modPix(self,pix, data):
        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)
        for i in range(lendata):
            pix = [value for value in imdata.__next__()[:3] +
                   imdata.__next__()[:3] +
                   imdata.__next__()[:3]]
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):
                    if (pix[j] % 2 != 0):
                        pix[j] -= 1
                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def encode_enc(self,newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)
        for pixel in self.modPix(newimg.getdata(), data):
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def enc_fun(self,text_area,myimg):
        data = text_area.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert","Kindly enter text in TextBox")
        else:
            newimg = myimg.copy()
            self.encode_enc(newimg, data)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myimg.filename))[0]
            newimg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newimg.size
            messagebox.showinfo("Success","Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")

    def page3(self,frame):
        frame.destroy()
        self.main(root)

root = Tk()
o = Stegno()
o.main(root)
root.mainloop()
