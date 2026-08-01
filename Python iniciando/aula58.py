from datetime import datetime
import time
from tkinter import Tk, messagebox

TARGET_HOUR = 15
TARGET_MINUTE = 47

while True:
    now = datetime.now()

    if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
        root = Tk()
        root.withdraw()  # Esconde a janela principal
        messagebox.showinfo(
            "Lembrete",
            "💈 Está na hora de sair para cortar o cabelo!"
        )
        break

    time.sleep(20)