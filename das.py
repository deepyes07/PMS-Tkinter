from tkinter import *
from PIL import ImageTk, Image
import mysql.connector as mysql
from tkinter import messagebox

root = Tk()
width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()
root.title("Pharmacy Management System")
root.geometry(f"{width_screen}x{height_screen}")
root.minsize("550", "600")
root.iconbitmap('./assets/medicine.ico')
root.state("zoomed")

# Track the active section
active_section = None

# ****************************Dashboard Frame************************************
frame = Frame(width=160, padx=40, bg='#A9CCE3')  # Light blue background for the sidebar
frame.pack(side=LEFT, fill=Y)

# ****************************Logo Image************************************
logoImg = Image.open('./assets/logo.png')
logoImg = logoImg.resize((100, 50))  # Resize logo
logoImg = ImageTk.PhotoImage(logoImg)

logo = Label(image=logoImg, bg='#A9CCE3', fg='lightblue', width=159, height=27)
logo.place(x=0, y=0)

# Logout Function
def logout():
    root.destroy()
    import login

# Dashboard Function
def dashboard():
    global active_section
    if active_section != 'dashboard':  # Only change if not already on this section
        root.destroy()
        import das
        active_section = 'dashboard'
        

# Medicine Function
def medicine():
    global active_section
    if active_section != 'medicine':  # Only change if not already on this section
        root.destroy()
        import medicine1
        active_section = 'medicine'

# Category Function
def category():
    global active_section
    if active_section != 'category':  # Only change if not already on this section
        root.destroy()
        import category1
        active_section = 'category'

# Billing Function
def billing():
    global active_section
    if active_section != 'billing':  # Only change if not already on this section
        root.destroy()
        import billing
        active_section = 'billing'


# Database Connection
try:
    con = mysql.connect(host='localhost', user='root',
                        password="@_Deepyes07", port="3306", database='pms')
    mycursor = con.cursor()
except:
    messagebox.showerror("Error", "Connection error")

query1 = 'select * from category'
mycursor.execute(query1)
row1 = mycursor.fetchall()
count1 = len(row1)

query2 = 'select * from user'
mycursor.execute(query2)
row2 = mycursor.fetchall()
count2 = len(row2)

query = 'select * from medicine'
mycursor.execute(query)
row = mycursor.fetchall()
count = len(row)

# ***************Buttons of the Dashboard Side********************************
def create_button(text, y_position, command, active=False):
    button = Button(
        text=text, width=19, height=2, border=0, bg='#A9CCE3' if not active else '#2980B9',  # Light blue background or blue for active
        fg='black', font=("Inter", 10, "bold"), cursor='hand2', command=command
    ).place(x=1, y=y_position)
    return button

dash = create_button('Dashboard', 30, dashboard, active=True)
medicine = create_button('Medicine', 90, medicine)
category = create_button('Category', 130, category)
billing = create_button('Billing', 170, billing)


# Log Out Button
logout = Button(
    text='Log Out', border=0, bg='#A9CCE3', fg='black', font=("Inter", 10, "bold"),
    cursor='hand2', command=logout
)
logout.place(x=10, y=250)

# Indicator for Dashboard
dashboard_indicator = Button(root, text='', bg='#2980B9')  # Blue indicator for active section
dashboard_indicator.place(x=2, y=30, width=5, height=40)

# *******Header Frame *******
frame1 = Frame(root, bg='#ECF0F1')  # Same light background color for consistency
frame1.place(x=164, y=0, width=1150, height=60)

# ***********Heading********************************
heading = Label(frame1, text='ABC Pharmacy Store', bg='#ECF0F1',
                fg='black', font=("camb", 20, 'bold'))
heading.place(x=100, y=5)

# Profile Image
profileImg = PhotoImage(file='./assets/profile.png')
profile = Label(image=profileImg, fg='black', bg='#ECF0F1')
profile.place(x=1050, y=0)

name = Label(text="Admin", fg='black', bg='#ECF0F1', font=("Poppins", 10))
name.place(x=1100, y=25)

# **********Medicine Buttons****************************
def create_section_button(text, y_position, command):
    return Button(
        root, text=text, border=0, fg='black', bg='#3498DB',
        font=("Inter", 14), cursor='hand2', command=command
    ).place(x=180, y=y_position)

med = create_section_button("Medicine", 100, medicine)
cate = create_section_button("Categories", 200, category)

# Consistent design across all sections: Text, Labels, etc.
med_num = Label(root, text=count, fg='black', bg='#ECF0F1', font=("Inter", 14))
med_num.place(x=190, y=150)

# Categories Section
cate_num = Label(root, text=count1, fg='black', bg='#ECF0F1', font=("Inter", 14))
cate_num.place(x=590, y=150)

# Users Section
userframe = Frame(width=250, height=90, bg="#ECF0F1")
userframe.place(x=1000, y=100)

userimg = PhotoImage(file='./assets/3-Friends.png')
use = Label(root, image=userimg, bg='#ECF0F1', fg='black')
use.place(x=1185, y=120)

cate_num = Label(root, text=count2, fg='black', bg='#ECF0F1', font=("Inter", 14))
cate_num.place(x=1010, y=150)

# *************Appointment Booked****************
appoinmentframe = Frame(root, bg='#D2C8C8')
appoinmentframe.place(x=164, y=250, width=1100, height=40)

appo = Label(root, text='Latest Products', bg='#D2C8C8', fg='black', font=("Inter", 15, "bold"))
appo.place(x=190, y=254)

# Form Frame
frame3 = Frame(root, width=1050, height=300, bg='#ECF0F1')  # Consistent color for frame background
frame3.place(x=200, y=310)

# Frame to store usernames
frame2 = Frame(root, bg='#3498DB')
frame2.place(x=230, y=320, width=1000, height=35)

id = Label(text="Product Id", bg='#3498DB', font=("Poppins", 12, "bold"))
id.place(x=230, y=328)

product_name = Label(text="Product Name", bg='#3498DB', font=("Poppins", 12, "bold"))
product_name.place(x=370, y=328)

product_status = Label(text="Product Status", bg='#3498DB', font=("Poppins", 12, "bold"))
product_status.place(x=620, y=328)

product_quantity = Label(text="Quantity", bg='#3498DB', font=("Poppins", 12, "bold"))
product_quantity.place(x=880, y=328)

product_price = Label(text="Price", bg='#3498DB', font=("Poppins", 12, "bold"))
product_price.place(x=1100, y=328)

# Now correctly iterate over rows and dynamically position the labels for products
row_data = list(row)
y_offset = 50  # Starting y position for first row

# Delete function
def delete_medicine(product_id):
    try:
        # Connect to the database
        con = mysql.connect(host='localhost', user='root', password="@_Deepyes07", port="3306", database='pms')
        mycursor = con.cursor()

        # Delete query
        delete_query = "DELETE FROM medicine WHERE product_id = %s"
        mycursor.execute(delete_query, (product_id,))
        
        con.commit()
        con.close()

        # Refresh the product list after deletion
        messagebox.showinfo("Success", "Medicine deleted successfully")
        refresh_medicine_list()

    except Exception as e:
        messagebox.showerror("Error", f"Error deleting medicine: {e}")

# Refresh the medicine list
def refresh_medicine_list():
    try:
        con = mysql.connect(host='localhost', user='root', password="@_Deepyes07", port="3306", database='pms')
        mycursor = con.cursor()

        # Query to get all medicines
        query = 'SELECT * FROM medicine'
        mycursor.execute(query)
        row = mycursor.fetchall()
        con.close()

        # Clear the current displayed list
        for widget in frame3.winfo_children():
            widget.destroy()

        # Display the new list of medicines
        y_offset = 50  # Starting y position for first row
        for product in row:
            product_id = product[0]
            product_name = product[1]
            product_status = "In Stock" if product[4] > 0 else "Out of Stock"
            quantity = product[3]
            price = product[4]

            # Display the data in columns
            Label(frame3, text=product_id, bg='#ECF0F1', font=("Poppins", 10)).place(x=40, y=y_offset)
            Label(frame3, text=product_name, bg='#ECF0F1', font=("Poppins", 10)).place(x=180, y=y_offset)
            Label(frame3, text=product_status, bg='#ECF0F1', font=("Poppins", 10)).place(x=440, y=y_offset)
            Label(frame3, text=quantity, bg='#ECF0F1', font=("Poppins", 10)).place(x=700, y=y_offset)
            Label(frame3, text=price, bg='#ECF0F1', font=("Poppins", 10)).place(x=880, y=y_offset)

            # Add delete button for each product
            delete_button = Button(
                frame3, text="Delete", fg="white", bg="red", font=("Poppins", 8),
                command=lambda product_id=product_id: delete_medicine(product_id)
            )
            delete_button.place(x=1030, y=y_offset, width=80, height=30)

            y_offset += 30  # Increase the y-offset for the next row

    except Exception as e:
        messagebox.showerror("Error", f"Error refreshing product list: {e}")

# Call refresh_medicine_list when the app starts
refresh_medicine_list()

root.mainloop()