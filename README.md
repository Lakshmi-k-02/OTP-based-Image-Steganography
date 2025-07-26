Image based Steganography with OTP Verification

A desktop GUI application built with Python Tkinter that allows users to securely encode and decode messages within images using LSB (Least Significant Bit) steganography, protected by an OTP verification system.

Encode secret messages inside .png, .jpg, or .jpeg images.
OTP (One-Time Password) verification to decode messages.
LSB-based steganography for image-based data hiding.
Image preview and message input via a GUI.
Input validations and user-friendly error handling.

Install the required libraries usinge pip install pillow

Technologies Used:
Python 3.x
Tkinter (GUI)
PIL (Pillow) – for image processing
Random, OS – for OTP generation and file handling

How It Works:
    1.Encoding:
    Select an image.
    Enter the message you want to hide.
    The system generates a 4-digit OTP.
    The image with the hidden message is saved as a new file.

    2.Decoding:
    Select an image that has a hidden message.
    Enter the OTP that was generated during encoding.
    If the OTP is correct, the hidden message is revealed


OTP is generated automatically during the encoding process. Make sure to save it securely!
Only users with the correct OTP can decode the hidden message.
This tool uses Least Significant Bit (LSB) technique for hiding messages in pixel values.
