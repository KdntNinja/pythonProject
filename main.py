import customtkinter
root = customtkinter.CTk()
root.geometry("450x300")


def array_use():
    array1 = [[first_name.get()],
              [last_name.get()]
              ]
    print(array1)
    root.destroy()


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
label = customtkinter.CTkLabel(master=frame, text="Login System", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)
first_name = customtkinter.CTkEntry(master=frame, placeholder_text="First Name")
first_name.pack(pady=12, padx=10)
last_name = customtkinter.CTkEntry(master=frame, placeholder_text="Last Name")
last_name.pack(pady=12, padx=10)
button = customtkinter.CTkButton(master=frame, text="Submit", command=array_use)
button.pack(pady=12, padx=10)
root.mainloop()
