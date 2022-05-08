from tkinter import *
from sqlite3 import *

import call_database

if __name__ == '__main__':
    def add_new_entry():
        add_new_entry_window = Tk()
        add_new_entry_window.title("Add New Entry")
        add_new_entry_window.geometry("300x140")

        def submit_to_db():
            service_input = service_field.get()
            username_input = username_field.get()
            password_input = password_field.get()

            try:
                submit_entry = call_database.add_new_entry(service_input, username_input, password_input)
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


    def passwordCorrect():
        def add_password_entry():  # opens window to submit new service, username, password
            print("Adding password entry")
            add_new_entry()

        def remove_password_entry():  # Deletes record being selected
            print("Removing password entry")

        def copy_pass_to_clipboard():  # Copies recorded password to clipboard to paste into other program
            print("Copying password")

        def close_window():
            main_window.quit()

        main_window = Tk()
        main_window.geometry("450x250")
        main_window.title("Epoxy Password Manager")

        left_frame = Frame(main_window)
        left_frame.pack(side=LEFT)

        button_frame = Frame(main_window)
        button_frame.pack(side=RIGHT, ipady=30)

        def getter():
            string = ""
            conn = connect("passwords.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM passwords")
            values = cur.fetchall()
            conn.commit()
            conn.close()

            for data in values:
                return data

        pass_list = Listbox(left_frame, width=30, selectmode=SINGLE)
        pass_list.insert(END, getter())
        pass_list.pack(padx=20)

        password_window_button_width = 15
        main_window_button_padding = 10

        add_button = Button(button_frame, text="Add Entry", command=add_password_entry,
                            width=password_window_button_width)
        add_button.pack(padx=main_window_button_padding)

        remove_button = Button(button_frame, text="Remove Entry", command=remove_password_entry,
                               width=password_window_button_width)
        remove_button.pack(padx=main_window_button_padding)

        copy_button = Button(button_frame, text="Copy Password", command=copy_pass_to_clipboard,
                             width=password_window_button_width)
        copy_button.pack(padx=main_window_button_padding)

        close_button = Button(button_frame, text="Close", command=close_window,
                              width=password_window_button_width)
        close_button.pack(padx=main_window_button_padding)

        main_window.mainloop()


    passwordCorrect()
    # def submit_button_command():
    #     password_window.destroy()
    #     passwordCorrect()
    #
    # def cancel_button_command():
    #     password_window.quit()

    # password_window = Tk()
    # password_window.geometry("300x150")
    # password_window.title("Epoxy Password Entry")
    #
    # enter_password_label = Label(password_window, text = "Please enter password")
    # enter_password_label.pack()
    #
    # password_entry = Entry(password_window, show = "*", width = 20)
    # password_entry.pack()
    #
    # button_padding = 10
    # button_frame = Frame(password_window)
    # button_frame.pack(pady = button_padding)
    #
    # submit_button = Button(button_frame, text = "Submit", command = submit_button_command)
    # submit_button.pack(side = LEFT, padx = button_padding)
    #
    # cancel_button = Button(button_frame, text = "Cancel", command = cancel_button_command)
    # cancel_button.pack(side = RIGHT, padx = button_padding)
    #
    # password_window.mainloop()
