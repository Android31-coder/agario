from customtkinter import *

class ConnectWindow(CTk):
    def __init__(self):
        super().__init__()

        self.title('Agar.io')

        self.name = None
        self.host = None
        self.port = None

        self.geometry("300x400")
        CTkLabel(self, text = 'Agario Game', font = ('Comic Sans MS',40,'bold')).pack(pady=15, padx=20, anchor="w")

        self.name_entry = CTkEntry(self, placeholder_text="Введіть нікнейм:", height=50)
        self.name_entry.pack(padx=20,anchor='w', fill="x")

        self.host_entry = CTkEntry(self, placeholder_text="Введіть хост:", height=50)
        self.host_entry.pack(padx=20,anchor='w', fill="x", pady=20)

        self.port_entry = CTkEntry(self, placeholder_text="Введіть порт:", height=50)
        self.port_entry.pack(padx=20,anchor='w', fill="x")

        CTkButton(self, text="GO", height=50).pack(padx=20, pady=20, fill="x")

    def open_game(self):
        self.name = self.name_entry.get()
        self.host = self.host_entry.get()
        self.port = self.port_entry.get()
        self.destroy()
