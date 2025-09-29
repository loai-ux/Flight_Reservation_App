import tkinter as tk
from database import Database
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class FlightReservationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Reservation System")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f0f0")
        
        # Center the window
        self.center_window()
        
        # Initialize database
        self.database = Database()
        
        # Main container frame
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Show home page
        self.show_home_page()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def show_home_page(self):
        HomePage(self.main_frame, self)
    
    def show_booking_page(self):
        BookingPage(self.main_frame, self, self.database)
    
    def show_reservations_page(self):
        ReservationsPage(self.main_frame, self, self.database)
    
    def show_edit_page(self, reservation_id):
        EditReservationPage(self.main_frame, self, self.database, reservation_id)

def main():
    root = tk.Tk()
    app = FlightReservationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()