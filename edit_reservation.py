import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime

class EditReservationPage:
    def __init__(self, parent, controller, database, reservation_id):
        self.parent = parent
        self.controller = controller
        self.database = database
        self.reservation_id = reservation_id
        self.create_widgets()
        self.load_reservation_data()
    
    def create_widgets(self):
        # Clear the parent frame
        for widget in self.parent.winfo_children():
            widget.destroy()
        
        # Title
        title_label = tk.Label(
            self.parent,
            text="Edit Reservation",
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
        self.date_entry = DateEntry(form_frame, font=("Arial", 11), width=28, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=4, column=1, pady=10, padx=10)
        
        # Seat Number
        tk.Label(form_frame, text="Seat Number:", font=("Arial", 11), bg="#f0f0f0").grid(row=5, column=0, sticky="w", pady=10, padx=10)
        self.seat_number_entry = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.seat_number_entry.grid(row=5, column=1, pady=10, padx=10)
        
        # Button frame
        button_frame = tk.Frame(self.parent, bg="#f0f0f0")
        button_frame.pack(pady=30)
        
        # Update button
        update_btn = tk.Button(
            button_frame,
            text="Update Reservation",
            command=self.update_reservation,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=18,
            height=2,
            cursor="hand2"
        )
        update_btn.pack(side=tk.LEFT, padx=10)
        
        # Cancel button
        cancel_btn = tk.Button(
            button_frame,
            text="Cancel",
            command=self.controller.show_reservations_page,
            font=("Arial", 12),
            bg="#757575",
            fg="white",
            width=18,
            height=2,
            cursor="hand2"
        )
        cancel_btn.pack(side=tk.LEFT, padx=10)
    
    def load_reservation_data(self):
        reservation = self.database.read_reservation_by_id(self.reservation_id)
        
        if reservation:
            # reservation format: (id, name, flight_number, departure, destination, date, seat_number)
            self.name_entry.insert(0, reservation[1])
            self.flight_number_entry.insert(0, reservation[2])
            self.departure_entry.insert(0, reservation[3])
            self.destination_entry.insert(0, reservation[4])
            
            # Parse and set date
            try:
                date_obj = datetime.datetime.strptime(reservation[5], '%Y-%m-%d').date()
                self.date_entry.set_date(date_obj)
            except:
                pass
            
            self.seat_number_entry.insert(0, reservation[6])
        else:
            messagebox.showerror("Error", "Reservation not found!")
            self.controller.show_reservations_page()
    
    def update_reservation(self):
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
        
        # Update in database
        success = self.database.update_reservation(
            self.reservation_id, name, flight_number, departure, destination, date, seat_number
        )
        
        if success:
            messagebox.showinfo("Success", "Reservation updated successfully!")
            self.controller.show_reservations_page()
        else:
            messagebox.showerror("Error", "Failed to update reservation. Please try again.")