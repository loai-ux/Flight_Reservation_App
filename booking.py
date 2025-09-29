import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime

class BookingPage:
    def __init__(self, parent, controller, database):
        self.parent = parent
        self.controller = controller
        self.database = database
        self.create_widgets()
    
    def create_widgets(self):
        # Clear the parent frame
        for widget in self.parent.winfo_children():
            widget.destroy()
        
        # Title
        title_label = tk.Label(
            self.parent,
            text="Book a Flight",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=20)
        
        # Form frame
        form_frame = tk.Frame(self.parent, bg="#f0f0f0")
        form_frame.pack(pady=20, padx=50)
        
        # Name
        tk.Label(form_frame, text="Passenger Name:", font=("Arial", 11), bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=10, padx=10)
        self.name_entry = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.name_entry.grid(row=0, column=1, pady=10, padx=10)
        
        # Flight Number
        tk.Label(form_frame, text="Flight Number:", font=("Arial", 11), bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=10, padx=10)
        self.flight_number_entry = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.flight_number_entry.grid(row=1, column=1, pady=10, padx=10)
        
        # Departure
        tk.Label(form_frame, text="Departure:", font=("Arial", 11), bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=10, padx=10)
        self.departure_entry = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.departure_entry.grid(row=2, column=1, pady=10, padx=10)
        
        # Destination
        tk.Label(form_frame, text="Destination:", font=("Arial", 11), bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=10, padx=10)
        self.destination_entry = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.destination_entry.grid(row=3, column=1, pady=10, padx=10)
        
        # Date
        tk.Label(form_frame, text="Date:", font=("Arial", 11), bg="#f0f0f0").grid(row=4, column=0, sticky="w", pady=10, padx=10)
        self.date_entry = DateEntry(form_frame, font=("Arial", 11), width=28, date_pattern='yyyy-mm-dd', mindate=datetime.date.today())
        self.date_entry.grid(row=4, column=1, pady=10, padx=10)
        
        # Seat Number
        tk.Label(form_frame, text="Seat Number:", font=("Arial", 11), bg="#f0f0f0").grid(row=5, column=0, sticky="w", pady=10, padx=10)
        self.seat_number_entry = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.seat_number_entry.grid(row=5, column=1, pady=10, padx=10)
        
        # Button frame
        button_frame = tk.Frame(self.parent, bg="#f0f0f0")
        button_frame.pack(pady=30)
        
        # Submit button
        submit_btn = tk.Button(
            button_frame,
            text="Book Flight",
            command=self.submit_booking,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=15,
            height=2,
            cursor="hand2"
        )
        submit_btn.pack(side=tk.LEFT, padx=10)
        
        # Back button
        back_btn = tk.Button(
            button_frame,
            text="Back to Home",
            command=self.controller.show_home_page,
            font=("Arial", 12),
            bg="#757575",
            fg="white",
            width=15,
            height=2,
            cursor="hand2"
        )
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def submit_booking(self):
        # Get values from entries
        name = self.name_entry.get().strip()
        flight_number = self.flight_number_entry.get().strip()
        departure = self.departure_entry.get().strip()
        destination = self.destination_entry.get().strip()
        date = self.date_entry.get()
        seat_number = self.seat_number_entry.get().strip()
        
        # Validate inputs
        if not all([name, flight_number, departure, destination, date, seat_number]):
            messagebox.showerror("Error", "All fields are required!")
            return
        
        # Save to database
        success = self.database.create_reservation(
            name, flight_number, departure, destination, date, seat_number
        )
        
        if success:
            messagebox.showinfo("Success", "Flight booked successfully!")
            self.clear_form()
        else:
            messagebox.showerror("Error", "Failed to book flight. Please try again.")
    
    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.flight_number_entry.delete(0, tk.END)
        self.departure_entry.delete(0, tk.END)
        self.destination_entry.delete(0, tk.END)
        self.seat_number_entry.delete(0, tk.END)
        self.date_entry.set_date(datetime.date.today())