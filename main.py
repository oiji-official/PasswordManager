from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

def find_password():
    website = website_entry.get()
    if len(website) == 0 :
        messagebox.showinfo(title = "Oops!", message = "Please enter the website you want to search the details for.")
    else:
        try:
            with open("data.json", mode = "r") as data_file:
                data = json.load(data_file)
                if website in data:
                    email = data[website]["email"]
                    password = data[website]["password"]
                    messagebox.showinfo(title = f"{website}", message = f"Email ID registered: {email} \nPassword: {password}")
                else:
                    messagebox.showinfo(title = "Oops!", message = "No details for the website exists yet!")
        except FileNotFoundError:
            messagebox.showinfo(title = "Oops!", message = "No details for the website exists yet!")
       
        finally:
            website_entry.delete(0,END)



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generatepassword():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_number + password_symbol

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password= password_entry.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
       messagebox.showinfo(title = "Oops!", message = "Please ensure that there are no empty fields.")
    
    else:
        try:
            with open("data.json", mode = "r") as data_file:
                data = json.load(data_file)
                
        except FileNotFoundError:
            with open("data.json", mode = "w") as data_file:
                json.dump(new_data, data_file, indent = 4)

        else:
            data.update(new_data)

            with open("data.json", mode = "w") as data_file:
                json.dump(data, data_file, indent = 4)
        
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(height = 200, width = 200)
logo_img = PhotoImage(file = "logo.gif")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column = 1, row = 0)

website_text = Label(text = "Website: ")
website_text.grid(column = 0, row = 1)

email_text = Label(text = "Email/Username: ")
email_text.grid(column = 0, row = 2)

password_text = Label(text = "Password: ")
password_text.grid(column = 0, row = 3)

website_entry = Entry()
website_entry.focus()
website_entry.grid(column = 1, row=1, columnspan = 2, sticky="EW", ipady = 4)


search_button = Button(text = "Search", command = find_password)
search_button.grid(row = 1, column = 2, sticky="EW")


email_entry = Entry()
email_entry.insert(0, "oiji2504@gmail.com")
email_entry.grid(column = 1, row = 2, columnspan = 2, sticky="EW", ipady = 4)


password_entry = Entry()
password_entry.grid(column = 1, row = 3, sticky="EW", ipady = 4)


generate_password_button = Button(text = "Generate Password", command = generatepassword)
generate_password_button.grid(row = 3, column = 2, sticky="EW")


add_button = Button(text = "Add", width = 35, command = save)
add_button.grid(row = 4, column = 1, columnspan = 2, sticky="EW")


window.mainloop()