import tkinter as tk
from tkinter import messagebox

APP_NAME = "Cafe Management System"
APP_VERSION = "1.0.0"


class ProfessionalApp:
    def __init__(self, root):
        self.root = root                     
        self.root.title(APP_NAME)
        self.root.geometry("600x400")
        self.root.minsize(450, 300)
        self.root.configure(bg="#f5efe6")

        self.new_window_count = 0
        self.about_window = None         

        self.create_main_layout()

        self.create_menu()

        self.root.protocol("WM_DELETE_WINDOW", self.exit_app)

    def create_main_layout(self):
        header = tk.Frame(self.root, bg="#6f4e37")
        header.pack(fill="x")

        tk.Label(
            header, text=APP_NAME, font=("Segoe UI", 20, "bold"),
            bg="#6f4e37", fg="white", pady=15
        ).pack()

        body = tk.Frame(self.root, bg="#f5efe6")
        body.pack(expand=True, fill="both", padx=20, pady=20)

        tk.Label(
            body, text="Welcome!", font=("Segoe UI", 16, "bold"),
            bg="#f5efe6", fg="#3e2a1c"
        ).pack(pady=(10, 5))

        tk.Label(
            body,
            text="This is the main application shell.\nUse the File menu or the buttons below.",
            font=("Segoe UI", 11), bg="#f5efe6", fg="#3e2a1c"
        ).pack(pady=5)

        btn_frame = tk.Frame(body, bg="#f5efe6")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Open New Window", width=18,
                  command=self.open_new_window).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="About", width=18,
                  command=self.open_about_window).grid(row=0, column=1, padx=5)

        self.status = tk.Label(
            self.root, text="Ready", anchor="w", bd=1, relief="sunken",
            font=("Segoe UI", 9)
        )
        self.status.pack(side="bottom", fill="x")

    def create_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", accelerator="Ctrl+N",
                              command=self.open_new_window)
        file_menu.add_command(label="About", command=self.open_about_window)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q",
                              command=self.exit_app)

        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

        self.root.bind("<Control-n>", lambda e: self.open_new_window())
        self.root.bind("<Control-q>", lambda e: self.exit_app())

    def open_new_window(self):
        self.new_window_count += 1
        new_window = tk.Toplevel(self.root)
        new_window.title(f"New Window {self.new_window_count}")
        new_window.geometry("380x250")
        new_window.configure(bg="#fffaf2")
        new_window.transient(self.root) 

        tk.Label(
            new_window, text=f"New Window #{self.new_window_count}",
            font=("Segoe UI", 14, "bold"), bg="#fffaf2"
        ).pack(pady=(20, 5))

        tk.Label(
            new_window,
            text="This is a Toplevel() window.\nIts parent is the main Tk() window.",
            font=("Segoe UI", 10), bg="#fffaf2"
        ).pack(pady=5)

        controls = tk.Frame(new_window, bg="#fffaf2")
        controls.pack(pady=20)

        tk.Button(controls, text="Minimize", width=10,
                  command=new_window.iconify).grid(row=0, column=0, padx=4)
        tk.Button(controls, text="Close", width=10,
                  command=new_window.destroy).grid(row=0, column=1, padx=4)

        self.status.config(text=f"Opened New Window {self.new_window_count}")

    def open_about_window(self):
        if self.about_window is not None and self.about_window.winfo_exists():
            self.about_window.lift()
            self.about_window.focus_force()
            return

        self.about_window = tk.Toplevel(self.root)
        win = self.about_window
        win.title("About")
        win.geometry("400x320")
        win.resizable(False, False)
        win.configure(bg="#fffaf2")
        win.transient(self.root)

        tk.Label(win, text=APP_NAME, font=("Segoe UI", 16, "bold"),
                 bg="#fffaf2", fg="#6f4e37").pack(pady=(20, 2))
        tk.Label(win, text=f"Version {APP_VERSION}", font=("Segoe UI", 10),
                 bg="#fffaf2").pack()

        tk.Label(
            win,
            text=("A professional desktop application shell built with\n"
                  "Python Tkinter. It demonstrates menus, Toplevel()\n"
                  "windows, and parent-child window relationships."),
            font=("Segoe UI", 10), bg="#fffaf2", justify="center"
        ).pack(pady=15)

        tk.Label(win, text="Developed by:", font=("Segoe UI", 10, "bold"),
                 bg="#fffaf2").pack()
        tk.Label(
            win,
            text=("Member 1 - Castro, Kharellyn Joyce I.\n"
                  "Member 2 - Macaraeg, Juan Patrick J.\n"
                  "Member 3 - Mañalac, John Paul L.\n"
                  "Member 4 - Quimado, Jerchris B.\n"
                  "Member 5 - Monderondo, Joseph Zalde B.\n"
                  "Member 6 - Tolentino, Christyn Louise Fatima L.\n"),
            font=("Segoe UI", 9), bg="#fffaf2", justify="center"
        ).pack(pady=5)

        tk.Button(win, text="Close", width=12, command=win.destroy).pack(pady=12)

        self.status.config(text="Opened About window")

    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?",
                               parent=self.root):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()       
    app = ProfessionalApp(root)
    root.mainloop()