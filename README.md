# Flight Reservation System

A comprehensive flight reservation management system built with Python and Tkinter, featuring a modern GUI and SQLite database backend.

## Features

- *Book Flights*: Create new flight reservations with passenger details
- *View Reservations*: Display all reservations in an organized table
- *Edit Reservations*: Update existing reservation information
- *Delete Reservations*: Remove reservations with confirmation
- *Modern UI*: Clean and intuitive graphical user interface
- *Database Storage*: Persistent data storage using SQLite

## Requirements

- Python 3.7 or higher
- tkinter (usually comes with Python)
- tkcalendar
- pyinstaller (for creating executable)

## Installation

### Option 1: Run from Source

1. *Clone the repository*
bash
git clone <your-repository-url>
cd flight_reservation_app


2. *Install required packages*
bash
pip install -r requirements.txt


3. *Run the application*
bash
python main.py


### Option 2: Run the Executable

1. Download the FlightReservation.exe file
2. Double-click to run (no installation required)

## Project Structure


/flight_reservation_app
├── main.py                 # Main application entry point
├── database.py             # Database connection and CRUD operations
├── home.py                 # Home page UI
├── booking.py              # Flight booking form
├── reservations.py         # View all reservations page
├── edit_reservation.py     # Update/Delete functionality
├── flights.db              # SQLite database (auto-generated)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Git ignore file


## Usage Guide

### Booking a Flight

1. Click *"Book Flight"* on the home page
2. Fill in all required fields:
   - Passenger Name
   - Flight Number
   - Departure City
   - Destination City
   - Date (use the calendar picker)
   - Seat Number
3. Click *"Book Flight"* to confirm

### Viewing Reservations

1. Click *"View Reservations"* on the home page
2. All bookings will be displayed in a table
3. Use the scrollbar to view more entries if needed

### Editing a Reservation

1. Go to the Reservations page
2. Select a reservation from the table
3. Click *"Edit Selected"*
4. Modify the fields as needed
5. Click *"Update Reservation"* to save changes

### Deleting a Reservation

1. Go to the Reservations page
2. Select a reservation from the table
3. Click *"Delete Selected"*
4. Confirm the deletion in the popup dialog

## Creating an Executable

To create a standalone Windows executable:

1. *Install PyInstaller*
bash
pip install pyinstaller


2. *Navigate to the project directory*
bash
cd flight_reservation_app


3. *Create the executable*
bash
pyinstaller --onefile --windowed --name FlightReservation main.py


4. *Find the executable*
The .exe file will be in the dist/ folder

### Alternative Command (with icon)
If you have an icon file:
bash
pyinstaller --onefile --windowed --icon=icon.ico --name FlightReservation main.py


## Database Schema

The SQLite database contains one table:

*reservations*
- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- name (TEXT, NOT NULL) - Passenger name
- flight_number (TEXT, NOT NULL) - Flight number
- departure (TEXT, NOT NULL) - Departure city
- destination (TEXT, NOT NULL) - Destination city
- date (TEXT, NOT NULL) - Flight date (YYYY-MM-DD)
- seat_number (TEXT, NOT NULL) - Seat assignment

## Technologies Used

- *Python 3* - Programming language
- *Tkinter* - GUI framework
- *SQLite3* - Database management
- *tkcalendar* - Date picker widget
- *PyInstaller* - Executable creation
