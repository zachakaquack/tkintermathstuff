import customtkinter as ctk
import settings

class NotesApp(ctk.CTkFrame):
    def __init__(self, master, home_frame, font):
        super().__init__(master, fg_color="transparent")

        self.frame = ctk.CTkFrame(master, fg_color=settings.BACKGROUND)
        self.home_frame = home_frame
        self.master = master

        self.notes_go_back_button = ctk.CTkButton(self.frame, text="go back", command=self.notes_go_back)

        self.notes_go_back_button.pack()

    def start_notes_page(self):
        print("start_physics_page")
        self.frame.pack(expand=True, fill="both")

    def notes_go_back(self):
        self.home_frame.pack(fill="both", expand=True)
        self.frame.pack_forget()