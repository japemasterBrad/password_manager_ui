from tkinter import *
from sqlite3 import *

import call_database
import main

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