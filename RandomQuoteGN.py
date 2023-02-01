import tkinter as tk
from turtle import color
from PIL import Image, ImageTk
import random


#crate a window for the about page 
def open_about_page():
    about_page = tk.Toplevel(root)
    about_page.title("About")
    about_page.config(bg='black')
    about_page.geometry("300x300")

    # Add a label to the About page with information about the application
    about_label = tk.Label(about_page, text="My Name is Jaylan Thompson and I created this as a fun little project that i kept improving on", bg='black')
    about_label.pack()

    # Add a close button to close the About page
    close_button = tk.Button(about_page, text="Close", command=about_page.destroy)
    close_button.pack()

#define the themes 
light_theme = {"bg":"white","fg": "black"}
dark_theme = {"bg":"black","fg": "white"}

#Function for the drop down menu
def change_theme(theme):
    if theme == 'Light':
        root.config(bg='white')
        result_label.config(bg='white', fg='black')
        button.config(bg='white', fg='black')
        clear_button.config(bg='white', fg='black')
        about_button.config(bg='white', fg='black')
    elif theme == 'Dark':
        root.config(bg='black')
        result_label.config(bg='black', fg='white')
        button.config(bg='black', fg='white')
        clear_button.config(bg='black', fg='white')
        about_button.config(bg='black', fg='white')

# Define the quotes to be used in the generator
quotes = [
    { "quote": "Do or do not there is no try.", "author": "Yoda", "image": "yoda.jpg" },
    { "quote": "I am Vengeance. I am the Night. I am Batman!", "author": "Kevin Conroy", "image": "Kevin_Conroy.jpg" },
    { "quote": "Don’t eat me. I have a wife and kids. Eat them.","author": "Homer Simpson", "image": "Homer.jpeg" },
]

# Function to generate a random quote
def generate_quote():
    quote = random.choice(quotes)
    return quote

# Function to print the quote and image in the GUI when button is pressed
def print_quote_and_image():
    quote = generate_quote()
    result_label.config(text=quote["quote"] + " - " + quote["author"])
    image = Image.open(quote["image"])
    image = image.resize((200, 200), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    image_label.config(image=image)
    image_label.image = image

# Clear Button    
def clear():
    result_label.config(text="")
    image_label.config(image="")



# Create the GUI window
root = tk.Tk()
root.title("Random Quote Generator")
root.config(bg='black')
root.geometry("800x600")

# Add a label to show the generated quote
result_label = tk.Label(root, text="")
result_label.pack()

# Add a label to show the image
image_label = tk.Label(root)
image_label.pack()

# Add a button to trigger the quote generation
button = tk.Button(root, text="Generate Quote", command=print_quote_and_image)
button.pack()

# Add a clear button to clear the quote and image
clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

# Add an "About" button to the main window
about_button = tk.Button(root, text="About", command=open_about_page)
about_button.pack()

# Drop down menu
themes = ['Light', 'Dark']
theme_var = tk.StringVar()
theme_var.set(themes[0])
theme_dropdown = tk.OptionMenu(root, theme_var, *themes, command=lambda x: change_theme(theme_var.get()))
theme_dropdown.config(text="Themes")
theme_dropdown.pack()

# Start the GUI event loop
root.mainloop()
