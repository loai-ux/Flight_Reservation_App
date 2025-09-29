import sqlite3
from typing import List, Tuple, Optional

class Database:
    def __init__(self, db_name: str = "flights.db"):
        self.db_name = db_name
        self.setup_database()
    
    def get_connection(self):
        """Create and return a database connection"""
        return sqlite3.connect(self.db_name)
    
    def setup_database(self):
        """Create the reservations table if it doesn't exist"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                flight_number TEXT NOT NULL,
                departure TEXT NOT NULL,
                destination TEXT NOT NULL,
                date TEXT NOT NULL,
                seat_number TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_reservation(self, name: str, flight_number: str, departure: str, 
                          destination: str, date: str, seat_number: str) -> bool:
        """Create a new reservation"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, flight_number, departure, destination, date, seat_number))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error creating reservation: {e}")
            return False
    
    def read_all_reservations(self) -> List[Tuple]:
        """Read all reservations from the database"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM reservations ORDER BY date')
            reservations = cursor.fetchall()
            
            conn.close()
            return reservations
        except Exception as e:
            print(f"Error reading reservations: {e}")
            return []
    
    def read_reservation_by_id(self, reservation_id: int) -> Optional[Tuple]:
        """Read a specific reservation by ID"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM reservations WHERE id = ?', (reservation_id,))
            reservation = cursor.fetchone()
            
            conn.close()
            return reservation
        except Exception as e:
            print(f"Error reading reservation: {e}")
            return None
    
    def update_reservation(self, reservation_id: int, name: str, flight_number: str, 
                          departure: str, destination: str, date: str, seat_number: str) -> bool:
        """Update an existing reservation"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE reservations 
                SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
                WHERE id = ?
            ''', (name, flight_number, departure, destination, date, seat_number, reservation_id))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error updating reservation: {e}")
            return False
    
    def delete_reservation(self, reservation_id: int) -> bool:
        """Delete a reservation"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM reservations WHERE id = ?', (reservation_id,))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error deleting reservation: {e}")
            return False