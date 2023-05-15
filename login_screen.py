import tkinter as tk
import customtkinter
from urllib.parse import quote
import webbrowser

async def login():
    email=email_entry.get()
    print("email: ", email)
    encoded_email = quote(email)
    print(encoded_email)
    # webbrowser.open_new("http://localhost:8000/login/microsoft")
    url = f"http://localhost:8000/login/microsoft?prompt=login&login_hint={encoded_email}"
    # data = {"email" : email} 
    # response = requests.post(url, json=data)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")



frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login to your Account")
label.pack(pady=12, padx=10)

email_var = tk.StringVar()
email_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Email", textvariable=email_var)
email_entry.pack(pady=12, padx=10)
email = email_entry.get()

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

root.mainloop()

