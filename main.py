import array
import time
import customtkinter

array1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
          [1, 2, 3, 4, 5, 6, 7, 8, 9]
          ]

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("450x300")


def loading_bar(bar_status, status2, is_success):
    balk = "█"
    c = 1
    try:
        while c <= 100:
            progress_bar = balk * c
            length = 100 - len(progress_bar)
            end_balk = "" * length
            percent = len(progress_bar)

            if percent != 100:
                bar_name = f"{bar_status} Status: [...]\033[0m"
            else:

                if is_success == "Completed":
                    bar_name = f"\n{bar_status} Status:\033[5m\033[32m [{is_success}]\033[0m"
                else:
                    bar_name = f"\n{bar_status}:\033[0m\033[5m\033[31m Failed"

            print(f"\r{status2}: [{progress_bar}{end_balk}] | {percent}% | {bar_name}", end=" ")
            c += 1
            time.sleep(0.015)

    except KeyboardInterrupt:
        print(f"\n{bar_status}:\033[0m\033[5m\033[31m Failed")


def write_file():
    info_write = open("User_File", "w")
    info_write.write(f"{username.get().lower()}\n{password.get().lower()}")

    root.destroy()


def read_use_file():
    open1 = open("users.txt", "a")
    open1.close()
    username_correct = None
    password_correct = None
    filepath = "User_File"

    write_file()

    with open(filepath) as fp:
        line = fp.readline()
        user = line.strip().lower()
        line = fp.readline()
        passw = line.strip().lower()

    while True:
        account = f"{user}:{passw}"

        if account == ":":
            print(f"\nVerification Status:\033[0m\033[5m\033[31m Failed")
            break

        with open(r'users.txt', 'r') as file:
            content = file.read()

            if account in content:
                loading_bar("User Verification", "Verifying Username", "Completed")
                username_correct = True
                loading_bar("Password Verification", "Verifying Password", "Completed")
                password_correct = True
                break
            else:
                loading_bar("User Verification", "Verifying Username", "Failed")
                loading_bar("Password Verification", "Verifying Password", "Failed")

    if password_correct and username_correct:
        login_correct_file = open("User_File", "w")
        login_correct_file.write("True")
        login_correct_file.close()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
username.pack(pady=12, padx=10)

password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
password.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=read_use_file)
button.pack(pady=12, padx=10)

root.mainloop()

with open("User_File") as uf:
    read = uf.readline()

    if read.strip().lower() == "true":
        print("\n\n\033[5m\033[32m[Access Granted]\033[0m")
