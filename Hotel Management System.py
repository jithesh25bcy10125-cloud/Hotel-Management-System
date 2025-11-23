rooms = []

def add_room():
    room_no = input("Enter Room Number: ")
    for r in rooms:
        if r["room_no"] == room_no:
            print("Room already exists!")
            return

    room_type = input("Enter Room Type (Single/Double): ")
    price = float(input("Enter Room Price: "))

    room_data = {
        "room_no": room_no,
        "type": room_type,
        "price": price,
        "booked": False
    }

    rooms.append(room_data)
    print("Room added successfully!")

def search_room():
    room_no = input("Enter Room Number: ")
    for r in rooms:
        if r["room_no"] == room_no:
            print("Room Found!")
            print("Room No:", r["room_no"])
            print("Type:", r["type"])
            print("Price:", r["price"])
            print("Status:", "Booked" if r["booked"] else "Available")
            return
    print("Room not found!")

def book_room():
    room_no = input("Enter Room Number: ")
    for r in rooms:
        if r["room_no"] == room_no:
            if not r["booked"]:
                r["booked"] = True
                print("Room booked successfully!")
            else:
                print("Room already booked!")
            return
    print("Room not found!")

def checkout_room():
    room_no = input("Enter Room Number: ")
    for r in rooms:
        if r["room_no"] == room_no:
            if r["booked"]:
                r["booked"] = False
                print("Room checkout successful!")
            else:
                print("Room is not booked!")
            return
    print("Room not found!")

def display_all_rooms():
    if not rooms:
        print("No rooms available!")
        return
    for r in rooms:
        print("\nRoom No:", r["room_no"])
        print("Type:", r["type"])
        print("Price:", r["price"])
        print("Status:", "Booked" if r["booked"] else "Available")

def main():
    while True:
        print("\n1. Add Room")
        print("2. Search Room")
        print("3. Book Room")
        print("4. Checkout Room")
        print("5. Display All Rooms")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_room()
        elif choice == "2":
            search_room()
        elif choice == "3":
            book_room()
        elif choice == "4":
            checkout_room()
        elif choice == "5":
            display_all_rooms()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

main()
