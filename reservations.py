import tkinter as tk
from tkinter import ttk, messagebox

class ReservationsPage:
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
            text="All Reservations",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=20)
        
        # Table frame with scrollbar
        table_frame = tk.Frame(self.parent, bg="#f0f0f0")
        table_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Scrollbars
        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
        scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        
        # Treeview
        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat"),
            show="headings",
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set,
            height=15
        )
        
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Define columns
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Passenger Name")
        self.tree.heading("Flight", text="Flight Number")
        self.tree.heading("Departure", text="Departure")
        self.tree.heading("Destination", text="Destination")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Seat", text="Seat")
        
        # Column widths
        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Name", width=150, anchor=tk.W)
        self.tree.column("Flight", width=100, anchor=tk.CENTER)
        self.tree.column("Departure", width=120, anchor=tk.W)
        self.tree.column("Destination", width=120, anchor=tk.W)
        self.tree.column("Date", width=100, anchor=tk.CENTER)
        self.tree.column("Seat", width=80, anchor=tk.CENTER)
        
        # Load data
        self.load_reservations()
        
        # Button frame
        button_frame = tk.Frame(self.parent, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        # Edit button
        edit_btn = tk.Button(
            button_frame,
            text="Edit Selected",
            command=self.edit_reservation,
            font=("Arial", 11, "bold"),
            bg="#FF9800",
            fg="white",
            width=15,
            cursor="hand2"
        )
        edit_btn.pack(side=tk.LEFT, padx=10)
        
        # Delete button
        delete_btn = tk.Button(
            button_frame,
            text="Delete Selected",
            command=self.delete_reservation,
            font=("Arial", 11, "bold"),
            bg="#F44336",
            fg="white",
            width=15,
            cursor="hand2"
        )
        delete_btn.pack(side=tk.LEFT, padx=10)
        
        # Refresh button
        refresh_btn = tk.Button(
            button_frame,
            text="Refresh",
            command=self.load_reservations,
            font=("Arial", 11, "bold"),
            bg="#2196F3",
            fg="white",
            width=15,
            cursor="hand2"
        )
        refresh_btn.pack(side=tk.LEFT, padx=10)
        
        # Back button
        back_btn = tk.Button(
            button_frame,
            text="Back to Home",
            command=self.controller.show_home_page,
            font=("Arial", 11),
            bg="#757575",
            fg="white",
            width=15,
            cursor="hand2"
        )
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def load_reservations(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Load from database
        reservations = self.database.read_all_reservations()
        
        for reservation in reservations:
            self.tree.insert("", tk.END, values=reservation)
    
    def edit_reservation(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation to edit.")
            return
        
        item = self.tree.item(selected[0])
        reservation_id = item['values'][0]
        self.controller.show_edit_page(reservation_id)
    
    def delete_reservation(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation to delete.")
            return
        
        item = self.tree.item(selected[0])
        reservation_id = item['values'][0]
        passenger_name = item['values'][1]
        
        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete the reservation for {passenger_name}?"
        )
        
        if confirm:
            success = self.database.delete_reservation(reservation_id)
            if success:
                messagebox.showinfo("Success", "Reservation deleted successfully!")
                self.load_reservations()
            else:
                messagebox.showerror("Error", "Failed to delete reservation.")