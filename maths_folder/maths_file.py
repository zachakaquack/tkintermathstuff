import customtkinter as ctk
import settings

class Math(ctk.CTkFrame):
    def __init__(self, master, home_frame, font):
        super().__init__(master, fg_color="transparent")

        self.frame = ctk.CTkFrame(master, fg_color=settings.BACKGROUND)
        self.home_frame = home_frame
        self.master = master

        self.maths_go_back_button = ctk.CTkButton(self.frame, text="go back", command=self.maths_go_back)

        self.maths_go_back_button.pack()

    def start_maths_page(self):
            print("matgh")
            self.frame.pack(expand=True, fill="both")

    def maths_go_back(self):
        self.home_frame.pack(fill="both", expand=True)
        self.frame.pack_forget()