import tkinter as tk
from tkinter import ttk

class HomePage:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        # Clear the parent frame
        for widget in self.parent.winfo_children():
            widget.destroy()
        
        # Title
        title_label = tk.Label(
            self.parent, 
            text="Flight Reservation System",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=40)
        
        # Subtitle
        subtitle_label = tk.Label(
            self.parent,
            text="Manage your flight bookings with ease",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666666"
        )
        subtitle_label.pack(pady=10)
        
        # Button frame
        button_frame = tk.Frame(self.parent, bg="#f0f0f0")
        button_frame.pack(pady=50)
        
        # Book Flight Button
        book_btn = tk.Button(
            button_frame,
            text="Book Flight",
            command=self.controller.show_booking_page,
            font=("Arial", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            height=2,
            cursor="hand2",
            relief=tk.RAISED,
            bd=3
        )
        book_btn.pack(pady=15)
        
        # View Reservations Button
        view_btn = tk.Button(
            button_frame,
            text="View Reservations",
            command=self.controller.show_reservations_page,
            font=("Arial", 14, "bold"),
            bg="#2196F3",
            fg="white",
            width=20,
            height=2,
            cursor="hand2",
            relief=tk.RAISED,
            bd=3
        )
        view_btn.pack(pady=15)
        
        # Footer
        footer_label = tk.Label(
            self.parent,
            text="© 2025 Flight Reservation System",
            font=("Arial", 9),
            bg="#f0f0f0",
            fg="#999999"
        )
        footer_label.pack(side=tk.BOTTOM, pady=20)