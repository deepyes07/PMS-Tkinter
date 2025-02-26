import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import mysql.connector as mysql

# Initialize root window
root = tk.Tk()
root.title("Login Page")
root.geometry("900x550")
root.configure(bg='white')

# Pharmacy Image & Introduction
intro_frame = tk.Frame(root, bg='#007BFF', width=400, height=550)
intro_frame.pack(side=tk.LEFT, fill=tk.Y)

img = tk.PhotoImage(file='./assets/pharma-removebg-preview.png')
tk.Label(intro_frame, image=img, bg='#007BFF').pack(pady=20)

tk.Label(intro_frame, text='A modern pharmacy management system\ndesigned for efficiency and automation.',
         fg='white', bg='#007BFF', font=('Arial', 12, 'bold'), justify='center').pack(pady=20)

tk.Label(intro_frame, text='Developed By:\nDeepesh Chhetri\nSonam Wangdi\nRajiv Yadav\nSuraj Maharjan',
         bg='#007BFF', fg='white', font=('Arial', 10, 'bold')).pack(pady=10)

# Sign-in Function
def signin():
    if not username.get() or not password.get():
        messagebox.showerror("Error", "Please fill all fields")
        return
    try:
        con = mysql.connect(host='localhost', user='root', password='@_Deepyes07', port='3306', database='pms')
        mycursor = con.cursor()
    except Exception as ex:
        messagebox.showerror("Error", "Connection error")
        print(ex)
        return
    
    mycursor.execute('SELECT * FROM admin WHERE email=%s AND password=%s', (username.get(), password.get()))
    if mycursor.fetchone() is None:
        messagebox.showerror("Error", "Invalid username or password")
    else:
        root.destroy()
        import das

# Forgot Password Function
def forget():
    top = tk.Toplevel(root)
    top.title("Forget Password")
    top.geometry("400x300")
    top.configure(bg='white')

    tk.Label(top, text='Enter Email:', bg='white').pack(pady=10)
    email_entry = ctk.CTkEntry(top, width=250)
    email_entry.pack(pady=5)

    tk.Label(top, text='New Password:', bg='white').pack(pady=10)
    new_password_entry = ctk.CTkEntry(top, show='*', width=250)
    new_password_entry.pack(pady=5)

    def save():
        try:
            con = mysql.connect(host='localhost', user='root', password='@_Deepyes07', port='3306', database='pms')
            mycursor = con.cursor()
            mycursor.execute('UPDATE admin SET password=%s WHERE email=%s', (new_password_entry.get(), email_entry.get()))
            con.commit()
            messagebox.showinfo("Success", "Password updated successfully")
        except:
            messagebox.showerror("Error", "Connection error")

    save_btn = ctk.CTkButton(top, text='Save', command=save, fg_color='#007BFF')
    save_btn.pack(pady=20)

# Toggle password visibility
def toggle_password():
    if password.cget('show') == '*':
        password.configure(show='')
        eye_button.configure(text='🙈')
    else:
        password.configure(show='*')
        eye_button.configure(text='👁')

# UI Elements
frame = tk.Frame(root, bg='white', padx=30, pady=30)
frame.pack(expand=True)

heading = tk.Label(frame, text='Sign In', fg='#007BFF', bg='white', font=('Arial', 20, 'bold'))
heading.pack(pady=10)

username = ctk.CTkEntry(frame, placeholder_text='Email', width=280)
username.pack(pady=5)

password_frame = tk.Frame(frame, bg='white')
password_frame.pack(pady=5)

password = ctk.CTkEntry(password_frame, placeholder_text='Password', show='*', width=250)
password.pack(side=tk.LEFT)

eye_button = tk.Button(password_frame, text='👁', command=toggle_password, bg='white', bd=0, font=('Arial', 12))
eye_button.pack(side=tk.LEFT, padx=5)

signin_btn = ctk.CTkButton(frame, text='Sign In', command=signin, fg_color='#007BFF')
signin_btn.pack(pady=10)

forgot_btn = ctk.CTkButton(frame, text='Forgot Password?', fg_color='transparent', text_color='#007BFF', command=forget)
forgot_btn.pack()

root.mainloop()