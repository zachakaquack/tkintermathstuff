import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkFrame, CTkFont
import settings
import notes_folder.notes_file
import calculator_folder.calculator_file
import maths_folder.maths_file
import physics_folder.physics_file
import calculator_folder.calculator_rendition2_file

import maths

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1920x1080")
        self.bind("<Escape>", lambda x: self.quit())
        self.resizable(False, False)

        # frame
        self.home_frame = CTkFrame(self, fg_color=settings.BACKGROUND)

        # layout setup
        self.home_frame.rowconfigure((0, 1), weight=1, uniform="a")
        self.home_frame.columnconfigure((0, 1), weight=1, uniform="a")

        # big font
        font = CTkFont(family=settings.FONT_FAMILY, size=80)


        # traversal buttons

        self.math_tranversal_button = (ctk.CTkButton(self.home_frame,

                                                     text="Math",
                                                     font=font,
                                                     corner_radius=90,
                                                     command=self.make_maths_page)
                                       .grid(row=0, column=0, sticky="nsew", rowspan=1, padx=45, pady=45))

        self.physics_tranversal_button = (ctk.CTkButton(self.home_frame,
                                                     text="Physics",
                                                     font=font,
                                                     corner_radius=90,
                                                     command=self.make_physics_page)
                                       .grid(row=0, column=1, sticky="nsew", rowspan=1, padx=45, pady=45))

        self.calculator_tranversal_button = (ctk.CTkButton(self.home_frame,
                                                      text="Calculator",
                                                     font=font,
                                                     corner_radius=90,

                                                     command=self.make_second_calculator_page)
                                       .grid(row=1, column=0, sticky="nsew", rowspan=1, padx=45, pady=45))

        self.notes_tranversal_button = (ctk.CTkButton(self.home_frame,
                                                     text="Notes",
                                                     font=font,
                                                     corner_radius=90,
                                                     command=self.make_notes_page)
                                       .grid(row=1, column=1, sticky="nsew", rowspan=1, padx=45, pady=45))

        # sections
        self.math = maths_folder.maths_file.Math(self, self.home_frame, font)
        self.physics = physics_folder.physics_file.Physics(self, self.home_frame, font)
        self.calculator = calculator_folder.calculator_file.Calculator(self, self.home_frame, font)
        self.notes = notes_folder.notes_file.NotesApp(self, self.home_frame, font)
        self.calculator2 = calculator_folder.calculator_rendition2_file.Calculator2(self, self.home_frame)

        self.home_frame.pack(fill="both", expand=True)

    def remove_home_frame(self):
        self.home_frame.pack_forget()

    def make_physics_page(self):
        self.remove_home_frame()
        self.physics.start_physics_page()

    def make_notes_page(self):
        self.remove_home_frame()
        self.notes.start_notes_page()

    def make_maths_page(self):
        self.remove_home_frame()
        self.math.start_maths_page()

    def make_calculator_page(self):
        self.remove_home_frame()
        self.calculator.start_calculator_page()

    def make_second_calculator_page(self):
        self.remove_home_frame()
        self.calculator2.start_second_calculator_page()


app = App()
app.mainloop()

