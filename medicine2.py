from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox

root = Tk()
width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()
root.title("Medicine/pms")
root.geometry(f"{width_screen}x{height_screen}")
root.minsize("400", "300")
root.iconbitmap('./assets/medicine.ico')
root.state("zoomed")

# ****************************dashboard frame************************************
frame = Frame(width=160, padx=30, bg='#ADD8E6')  # Changed to light blue background
frame.pack(side=LEFT, fill=Y)

# ****************************logo image************************************
logoImg = PhotoImage(file='./assets/logo.png')
logo = Label(image=logoImg, bg='white', fg='black', width=159, height=27)
logo.place(x=0, y=0)

# logout function
def logout():
    root.destroy()
    import login

# dashboard function
def dashboard():
    root.destroy()
    import das

# medicine function
def medicine():
    root.destroy()
    import medicine1

# category function
def category():
    root.destroy()
    import category1

# billing function
def billing():
    root.destroy()
    import billing

# save function
def save():
    name = user_name_entry.get()
    category = user_category_entry.get()
    rate = user_price_entry.get()
    qan = quantity_entry.get()
    if name == '' or category == '' or rate == '' or qan == '':
        messagebox.showerror("error", "please fill all fields")
    else:
        try:
            con = mysql.connect(host='localhost', user='root', password="@_Deepyes07", port="3306", database='pms')
            mycursor = con.cursor()
        except:
            messagebox.showerror("error", "connection error!please add your medicine again")
            return
        try:
            vals = {
                "name": name,
                "category": category,
                "price": rate,
                "quantity": qan
            }
            insert_query = """INSERT INTO medicine( name, category, price, quantity) VALUES( %s, %s, %s, %s)""", (
                vals['name'], vals['category'], int(vals['price']), int(vals['quantity']))
            mycursor.execute(*insert_query)
            con.commit()
            mycursor.close()
            con.close()
            user_name_entry.delete(0, 'end')
            user_category_entry.delete(0, 'end')
            user_price_entry.delete(0, 'end')
            quantity_entry.delete(0, 'end')
            messagebox.showinfo("success", "added successfully")
        except:
            user_name_entry.delete(0, 'end')
            user_category_entry.delete(0, 'end')
            user_price_entry.delete(0, 'end')
            quantity_entry.delete(0, 'end')
            messagebox.showerror("error", "invlid inputs")

def back():
    root.destroy()
    import medicine1

# ***************buttons of the dashboard side********************************
dash = Button(text='Dashboard', width=19, height=2, border=0, bg='#ADD8E6', fg='black', font=("Inter", 10, "bold"), cursor='hand2', command=dashboard)
dash.place(x=1, y=30)
medicine = Button(text='Medicine', width=19, height=2, border=0, bg='#ADD8E6', fg='black', font=("Inter", 10, "bold"), cursor='hand2', command=medicine)
medicine.place(x=1, y=90)
medicineimg = PhotoImage(file='./assets/medicine.png')
img = Label(root, image=medicineimg, bg='#ADD8E6')
img.place(x=1, y=95)
# indicator for medicine
medicine_indicator = Button(root, text='', bg='#FF702A')
medicine_indicator.place(x=1, y=90, width=5, height=40)

category = Button(text='Category', border=0, bg='#ADD8E6', fg='black', font=("Inter", 10, "bold"), cursor='hand2', command=category)
category.place(x=10, y=130)
billing = Button(text='Billing', border=0, bg='#ADD8E6', fg='black', font=("Inter", 10, "bold"), cursor='hand2', command=billing)
billing.place(x=10, y=170)

# ***************log out button*******************************
logout = Button(text='Log Out', border=0, bg='#ADD8E6', fg='black', font=("Inter", 10, "bold"), cursor='hand2', command=logout)
logout.place(x=10, y=250)

# *******header frame *******
frame1 = Frame(root, bg='#FAFAFA')
frame1.place(x=164, y=0, width=1150, height=60)

# ***********heading********************************
heading = Label(frame1, text='ABC Pharmacy Store', bg='#FAFAFA', fg='black', font=("camb", 20, 'bold'))
heading.place(x=100, y=5)

# ************* profile image****************************
profileImg = PhotoImage(file='./assets/profile.png')
profile = Label(image=profileImg, fg='black', bg='#FAFAFA')
profile.place(x=1050, y=0)
admin = Label(text="Admin", fg='black', bg='#FAFAFA', font=("Poppins", 10))
admin.place(x=1100, y=25)
name = Label(text="Test", bg='#FAFAFA', fg='black', font=("Poppins", 10))
name.place(x=1100, y=5)

# ********add medicine product ****************************
add_medicine = Label(root, text='Add Medicine', fg='#363740', font=("Poppins", 20, "bold"))
add_medicine.place(x=600, y=150)
info = Label(root, text='Information', fg='#363740', font=("Poppins", 15, "bold"))
info.place(x=200, y=200)
a = Label(root, text='________________________________________________________________________________________________________________________________________________________________________________________________')
a.place(x=190, y=230)

user_name = Label(root, text='Name', fg='#363740', width=5, font=("Poppins", 15))
user_name.place(x=190, y=260)
user_name_entry = Entry(root, text='', width=100)
user_name_entry.place(x=400, y=260, height=35)

user_category = Label(root, text='Category', fg='#363740', font=("Poppins", 15))
user_category.place(x=190, y=310)
user_category_entry = Entry(root, text='', width=100)
user_category_entry.place(x=400, y=310, height=35)

user_price = Label(root, text='Price', fg='#363740', font=("Poppins", 15))
user_price.place(x=190, y=360)
user_price_entry = Entry(root, text='', width=100)
user_price_entry.place(x=400, y=360, height=35)

quantity = Label(root, text='Quantity', fg='#363740', font=("Poppins", 15))
quantity.place(x=190, y=410)
quantity_entry = Entry(root, text='', width=100)
quantity_entry.place(x=400, y=410, height=35)

save_button = Button(root, text='SAVE', border=1, width=15, height=2, bg='#000000', fg='#FAFAFA', font=("Poppins", 10), command=save)
save_button.place(x=880, y=520)

back_button = Button(root, text='BACK', border=1, width=15, height=2, bg='#000000', fg='#FAFAFA', font=("Poppins", 10), command=back)
back_button.place(x=350, y=520)

root.mainloop()
