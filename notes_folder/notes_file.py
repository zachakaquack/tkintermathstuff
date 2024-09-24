from tkinter import StringVar, Scrollbar

import customtkinter as ctk


class NotesApp(ctk.CTkFrame):
    def __init__(self, master, home_frame, font):
        super().__init__(master, fg_color="transparent")

        self.font = font

        self.frame = ctk.CTkFrame(master)

        self.frame.rowconfigure(0, weight=1, uniform="a")
        self.frame.columnconfigure((0, 1, 2), weight=1, uniform="a")



        self.home_frame = home_frame
        self.master = master

        self.notes_go_back_button = ctk.CTkButton(self.frame, text="go back", command=self.notes_go_back)

        #self.notes_go_back_button.pack()

    def start_notes_page(self):
        self.frame.pack(expand=True, fill="both")

    def notes_go_back(self):
        self.home_frame.pack(fill="both", expand=True)
        self.frame.pack_forget()



