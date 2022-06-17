import os
from re import L
from tkinter import *
from sqlite3 import *
from call_database import *

if __name__ == '__main__':
    def add_new_entry(): # -*-*-*-*-*-*-*-*-*-*-*-* ADD NEW ENTRY WINDOW -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        add_new_entry_window = Tk()
        add_new_entry_window.title("Add New Entry")
        add_new_entry_window.geometry("300x140")

        def submit_to_db():
            service_input = service_field.get()
            username_input = username_field.get()
            password_input = password_field.get()
            db = AccessDB()
            
            
            try:
                submit_entry = db.add_new_entry(service_input, username_input, password_input)
            finally:
                for widgets in add_new_entry_window.winfo_children():
                    widgets.destroy()

                successful = Label(add_new_entry_window, text="New entry added successfully!")
                successful.pack(pady=20)
                close_button = Button(add_new_entry_window, text="Close", command=add_new_entry_window.destroy)
                close_button.pack()

            return submit_entry

        def destroy_entry_window():
            add_new_entry_window.destroy()
     

        text_field_width = 20
        frame_padding = 10

        # INIT FRAMES
        top_frame = Frame(add_new_entry_window)
        top_frame.pack()

        bottom_frame = Frame(add_new_entry_window)
        bottom_frame.pack(ipady=frame_padding)

        text_entry_frame = Frame(top_frame)
        text_entry_frame.pack(side=RIGHT, padx=frame_padding, pady=frame_padding)

        label_frame = Frame(top_frame)
        label_frame.pack(side=LEFT, padx=frame_padding, pady=frame_padding)

        button_frame = Frame(bottom_frame)
        button_frame.pack(side=BOTTOM)

        service_label = Label(label_frame, text="Service")
        service_label.pack()
        service_field = Entry(text_entry_frame, width=text_field_width)
        service_field.pack()

        username_label = Label(label_frame, text="Username")
        username_label.pack()
        username_field = Entry(text_entry_frame, width=text_field_width)
        username_field.pack()

        password_field_frame = Frame(text_entry_frame)
        password_field_frame.pack()
        password_label = Label(label_frame, text="Password")
        password_label.pack()
        password_field = Entry(text_entry_frame, width=text_field_width)
        password_field.pack()

        submit_button = Button(bottom_frame, text='Submit', command=submit_to_db)
        submit_button.pack(side=LEFT, padx=frame_padding)

        cancel_button = Button(bottom_frame, text='Cancel', command=destroy_entry_window)
        cancel_button.pack(side=RIGHT, padx=frame_padding)

        add_new_entry_window.mainloop()
        

    def passwordCorrect(): #-*-*-*-*-*-*-*-*-*-*-*-* IF PASSWORD IS CORRECT -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        def add_password_entry():  # opens window to submit new service, username, password
            print("Adding password entry")
            add_new_entry()
            
            
        def add_password_button():
            add_password_entry()
            populate_services()
            
            
        def refresh_listbox():
            pass_list.delete(0, END)
            
            conn = connect("passwords.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM passwords")
            values = cur.fetchall()
            conn.commit()
            conn.close()
            
            for data in values:
                data_row = data[0]
                pass_list.insert(END, data_row)
                
            
        def reveal_login():
            entry_to_delete_get = pass_list.get(0, END)
            entry_to_delete = str(entry_to_delete_get[0])

            print(entry_to_delete)
            print(type(entry_to_delete))

            conn = connect("passwords.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM passwords WHERE service = (?)", entry_to_delete)
            values = cur.fetchall()
            conn.commit()
            conn.close()
            
            print(f"{values}")
            
            # reveal_login_window = Tk()
            # login_listbox = Listbox(reveal_login_window)
            # close_button = Button(reveal_login_window, text = "Close")
            # reveal_login_window.mainloop()
            
            '''
            
            start a new window
            pull username and password from database
            paste it into a listbox in the new window
            
            '''
        
        
        def remove_password_button():
            remove_password_entry()
            populate_services()
            
            
        def remove_password_entry():  # Deletes record being selected
            os.system("clear")
            print("Removing password entry")
            
            entry_to_delete = pass_list.get(ANCHOR)
            str(entry_to_delete)
            
            print(f"Entry to delete: {entry_to_delete}")
            
            conn = connect("passwords.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM passwords WHERE service = (?)", (entry_to_delete,))
            conn.commit()
            conn.close()
        
            print("Deleted Successfully!\n\n")
            
        
        def populate_services():
            pass_list.delete(0, END)
             
            conn = connect("passwords.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM passwords")
            values = cur.fetchall()
            conn.commit()
            conn.close()
            
            for data in values: 
                data_row = data[0]
                pass_list.insert(END, data_row)
                
            
        def copy_pass_to_clipboard():  # Copies recorded password to clipboard to paste into other program
            print("Copying password")


        def close_window():
            main_window.quit()


        main_window = Tk()
        main_window.geometry("500x280")
        main_window.title("Epoxy Password Manager")

        left_frame = Frame(main_window)
        left_frame.pack(side=LEFT)

        button_frame = Frame(main_window)
        button_frame.pack(side=RIGHT, ipady=30)

        global pass_list
        pass_list = Listbox(left_frame, width=43, height=20, selectmode=SINGLE)
        pass_list.pack(padx=10)
        
        print(pass_list)
        
        AccessDB()
        
        conn = connect("passwords.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM passwords ORDER BY service ASC")
        values = cur.fetchall()
        conn.commit()
        conn.close()
        
        pass_list.delete(0, END)
        
        for data in values:
            data_row = data[0]
            pass_list.insert(END, data_row)

        password_window_button_width = 20
        main_window_button_padding = 10

        add_button = Button(button_frame, text="Add Entry", command=add_password_button,
                            width=password_window_button_width)
        add_button.pack(padx=main_window_button_padding)

        refresh_button = Button(button_frame, text="Refresh List", command=refresh_listbox,
                                width=password_window_button_width)
        refresh_button.pack(padx=main_window_button_padding)

        reveal_details = Button(button_frame, text = "Reveal Login Details", command = reveal_login,
                                width=password_window_button_width)
        reveal_details.pack()

        remove_button = Button(button_frame, text="Remove Entry", command=remove_password_button,
                               width=password_window_button_width)
        
        remove_button.pack(padx=main_window_button_padding)

        copy_button = Button(button_frame, text="Copy Password", command=copy_pass_to_clipboard,
                             width=password_window_button_width)
        copy_button.pack(padx=main_window_button_padding)

        close_button = Button(button_frame, text="Close", command=close_window,
                              width=password_window_button_width)
        close_button.pack(padx=main_window_button_padding)

        main_window.mainloop()


if __name__ == "__main__":
    passwordCorrect()
    
    #-*-*-*-*-*-*-*-*-*-*-*-* KEYCHAIN PASSWORD -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
    
    # def submit_button_command():
    #     password_window.destroy()
    #     passwordCorrect()
    
    # def cancel_button_command():
    #     password_window.quit()

    # password_window = Tk()
    # password_window.geometry("300x150")
    # password_window.title("Epoxy Password Entry")
    
    # enter_password_label = Label(password_window, text = "Please enter password")
    # enter_password_label.pack()
    
    # password_entry = Entry(password_window, show = "*", width = 20)
    # password_entry.pack()
    
    # button_padding = 10
    # button_frame = Frame(password_window)
    # button_frame.pack(pady = button_padding)
    
    # submit_button = Button(button_frame, text = "Submit", command = submit_button_command)
    # submit_button.pack(side = LEFT, padx = button_padding)
    
    # cancel_button = Button(button_frame, text = "Cancel", command = cancel_button_command)
    # cancel_button.pack(side = RIGHT, padx = button_padding)
    
    # password_window.mainloop()
