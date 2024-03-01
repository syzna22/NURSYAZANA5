'''
    Program purpose: To to develop for Cahaya Kasih Hotel Reservation System
    Programmer: NURSYAZANA BINTI MOHAMAD NOH EZAM
    Date: 1 March 2024
'''

import datetime

print ("\n")
print("Welcome to Cahaya Kasih Hotel Reservation System")
print ("\n")
#Display Room Types
print("Available Room Type in Cahaya Kasih: ")
print("1. Single - RM100 per night")
print("2. Double - RM150 per night")
print("3. Suite - RM250 per night")
print ("\n")
#Prompt user to input number to choose room type
room_types = int(input("Please select a room type (1/2/3): "))
#Prompt user to input number of room
num_room = int(input("Enter the number of rooms: "))
#Prompt user to input check in date and check out date
check_in = datetime.datetime.strptime(input("Enter check-in date (YYYY-MM-DD): "), "%Y-%m-%d")
check_out = datetime.datetime.strptime(input("Enter check-out date (YYYY-MM-DD): "), "%Y-%m-%d")
print ("\n")
#Prompt user to input additional services
print("Additional Services: ")
print("1. Breakfast -  RM20 per person")
print("2. WiFi - RM10 per day")
print("3. Parking - RM15 per day")

#Error
if room_types not in [1, 2, 3]:
    print("Error: Invalid option number of room. Please try again !")
if num_room <= 0 :
    print("Error: Number of rooms and nights must be positive")
if check_out <= check_in:
    print("Check-out date must be after check-in date.")


room_types = ["Single", "Double", "Suite"]
nightly_rates = [100, 150, 250]

add_services = {
    "Breakfast": 20,
    "WiFi": 10,
    "Parking": 15
}

def display_room_types():
    print("Room Types:")
    for i, room_type in enumerate(room_types):
        print(f"{i+1}. {room_type} - RM{nightly_rates[i]} per night")
def calculate_total_cost(room_type, num_room, check_in, check_out, nightly_rate, add_services):
    duration = (check_out - check_in).days
    base_cost = nightly_rate * num_room * duration
    service_cost = sum(add_services.values())
    total_cost = base_cost + service_cost
    return total_cost

selected_services = []
while True:
    print("\nAdditional Services:")
    for i, service in enumerate(add_services.keys()):
        print(f"{i+1}. {service} - ${add_services[service]}")

    choice = input("Select additional service (or enter 'done' to proceed): ").strip().capitalize()
    if choice == 'Done':
        break
    elif choice in add_services:
        selected_services.append(choice)
    else:
        print("Invalid service choice.")


total_cost = calculate_total_cost(room_types, num_room, check_in, check_out, add_services)

#Display
print("\nReservation Details:")
print(f"Room Type: {room_types}")
print(f"Number of Rooms: {num_room}")
print(f"Check-in Date: {check_in}")
print(f"Check-out Date: {check_out}")
print("Selected Additional Services:")
for service in add_services:
    print(f"- {service}")
print(f"Total Cost: ${total_cost}")

confirmation = input("\nConfirm reservation (yes/no): ").strip().lower()
if confirmation == 'yes':
    print("Reservation confirmed. Thank you!")
else:
    print("Reservation cancelled.")


