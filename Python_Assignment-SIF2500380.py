# -*- coding: utf-8 -*-
Python Assignment
SIF2500380
Hasaru Wijesundara


from datetime import datetime
bookings = []
TOTAL_ROOMS = 10
room_type = {"Room 100" : "Single" , "Room 103" : "Single" , "Room 105" : "Single" , "Room 107" : "Single" , "Room 102" : "Double" , "Room 104" : "Double" , "Room 106" : "Double" , "Room 108" : "Double" , "Room 109" : "Triple" , "Room 110" : "Triple" }

room_status = {
    "Room 100": "Available",
    "Room 102": "Available",
    "Room 103": "Available",
    "Room 104": "Available",
    "Room 105": "Available",
    "Room 106": "Available",
    "Room 107": "Available",
    "Room 108": "Available",
    "Room 109": "Available",
    "Room 110": "Available"
}

def add_booking():
  guest_name = input("Enter guest name : ")

  while True:
      print("Available room types : Single , Double , Triple")
      chosen_type = input("Enter the type of room you prefer : ")

      available_rooms= []
      room_ids = ["Room 100", "Room 102", "Room 103", "Room 104", "Room 105",
                "Room 106", "Room 107", "Room 108", "Room 109", "Room 110"]

      for room_id in room_ids:
          if room_type[room_id] == chosen_type and room_status[room_id] == "Available":
              available_rooms.append(room_id)

      if not available_rooms:
        print(f"No available rooms of type '{chosen_type}'.")
      else:
        print("Available rooms are : ", available_rooms)

        while True:
          check_in_td = input("Enter check-in date (YYYY-MM-DD HH:MM): ")
          try:
              check_in_date = datetime.strptime(check_in_td, "%Y-%m-%d %H:%M")
              break
          except ValueError:
              print("Invalid date format. Please use YYYY-MM-DD HH:MM format.")

        while True:
          check_out_td = input("Enter check-out date (YYYY-MM-DD HH:MM): ")
          try:
              check_out_date = datetime.strptime(check_out_td, "%Y-%m-%d %H:%M")
              if check_out_date <= check_in_date:
                  print("Check-out date must be after check-in date.")
                  continue
              break
          except ValueError:
              print("Invalid date format. Please use YYYY-MM-DD HH:MM format.")

        selected_room_number = None
        while selected_room_number not in available_rooms:
            selected_room_number = input("Enter the specific room number you want to book: ")
            if selected_room_number not in available_rooms:
                print("Invalid room number or not available. Please choose from the listed available rooms.")

        bookings.append({
            "Guest Name" : guest_name,
            "Room Number": selected_room_number,
            "Room Type" : chosen_type,
            "Check-in Date" : check_in_date.strftime("%Y-%m-%d"),
            "Check-in Time" : check_in_date.strftime("%H:%M"),
            "Check-out Date" : check_out_date.strftime("%Y-%m-%d"),
            "Check-out Time" : check_out_date.strftime("%H:%M"),
            "Status" : "Booked"
        })

        room_status[selected_room_number] = "Booked"
        print(f"Booking added successfully. {guest_name} booked {selected_room_number} ({chosen_type}) from {check_in_date} to {check_out_date}")

      another = input(f"Does {guest_name} want to book another room? (yes/no): ").lower()
      if another != "yes":
          break


def view_bookings():
  if not bookings:
    print("No bookings found.")
  else:
    for booking in bookings:
      print(booking)


def search_booking():
  room_number = input("Enter room number to search : ")
  for booking in bookings:
    if booking["Room Number"] == room_number and booking["Status"] == "Booked":
      print(f"Guest booked into {room_number}.")
      return
  print("Booking not found or room is not currently booked.")

def check_in_guest():
    room_number = input("Enter room number to check in : ")
    found_booking = False
    for booking in bookings:
        if booking["Room Number"] == room_number and booking["Status"] == "Booked":
            booking["Status"] = "Checked In"
            print(f"Guest checked into {room_number}.")
            found_booking = True
            return
    if not found_booking:
        print("Booking not found or guest has already checked in.")

def check_out_guest():
    room_number = input("Enter room number to check out : ")
    found_booking = False
    for booking in bookings:
        if booking["Room Number"] == room_number and booking["Status"] == "Checked In":
            booking["Status"] = "Checked Out"
            print(f"Guest checked out from {room_number}.")
            room_status[room_number] = "Available"
            found_booking = True
            return
    if not found_booking:
        print("Booking not found or guest has not checked in.")

def count_available_rooms():
    available = 0
    for status_value in room_status.values():
      if status_value == "Available":
        available += 1
    print(f"Available rooms : {available}")

def menu():
    while True:
      print("==============Annapurna Hotels===============")
      print("\nHotel Room Booking System")
      print("1. Add Booking")
      print("2. View Bookings")
      print("3. Search Booking ")
      print("4. Check In Guest")
      print("5. Check Out Guest ")
      print("6. Count Available Rooms")
      print("7. Exit")


      choice = input("Enter your choice: ")

      if choice == "1":
          add_booking()
      elif choice == "2":
          view_bookings()
      elif choice == "3":
          search_booking()
      elif choice == "4":
          check_in_guest()
      elif choice == "5":
          check_out_guest()
      elif choice == "6":
          count_available_rooms()
      elif choice == "7":
          print("Thank You for using The Annapurna Hotel Booking System.")
          break
      else:
          print("Invalid choice. Please try again.")


menu()
