import tkinter as tk
from tkinter import ttk, messagebox
import qrcode


def generate_wifi_qr():
    ssid = ssid_entry.get()
    security = security_var.get()
    password = password_entry.get()

    if not ssid:
        messagebox.showerror("Error", "SSID cannot be empty")
        return

    if security != "nopass" and not password:
        messagebox.showerror("Error", "Password is required for WEP and WPA")
        return

    # Generate WiFi configuration string
    wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};;"

    # Create QR code instance
    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    # Add WiFi configuration data
    qr.add_data(wifi_config)
    qr.make(fit=True)

    # Create an image from the QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(f"{ssid}_wifi_qr.png")
    messagebox.showinfo("Success", f"QR code saved as {ssid}_wifi_qr.png")


# Create the main window
root = tk.Tk()
root.title("WiFi QR Code Generator")

# Create and pack a frame
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# SSID input
ttk.Label(frame, text="SSID:").grid(column=0, row=0, sticky=tk.W, pady=5)
ssid_entry = ttk.Entry(frame, width=30)
ssid_entry.grid(column=1, row=0, sticky=(tk.W, tk.E), pady=5)

# Security type dropdown
ttk.Label(frame, text="Security:").grid(column=0, row=1, sticky=tk.W, pady=5)
security_var = tk.StringVar()
security_dropdown = ttk.Combobox(frame, textvariable=security_var, values=["WPA", "WEP", "nopass"], state="readonly")
security_dropdown.grid(column=1, row=1, sticky=(tk.W, tk.E), pady=5)
security_dropdown.set("WPA")

# Password input
ttk.Label(frame, text="Password:").grid(column=0, row=2, sticky=tk.W, pady=5)
password_entry = ttk.Entry(frame, width=30, show="*")
password_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), pady=5)

# Generate button
generate_button = ttk.Button(frame, text="Generate QR Code", command=generate_wifi_qr)
generate_button.grid(column=0, row=3, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()