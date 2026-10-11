from campusflow.workflow import list_tickets

def display_menu():
    print("\n========== CAMPUSFLOW ==========")
    print("Campus Helpdesk Ticket Manager")
    print("================================")
    print("1. Create Ticket")
    print("2. List All Tickets")
    print("3. View Ticket")
    print("4. Assign Ticket")
    print("5. Update Ticket Status")
    print("6. Reopen Ticket")
    print("7. View Priority Work Queue")
    print("8. Generate Report")
    print("9. Exit")


def main():
    tickets = []

    while True:
        display_menu()

        choice = input("\nEnter your choice (1-9): ").strip()

        if choice == "9":
            print("\nThank you for using CampusFlow!")
            break

        elif choice == "2":
            list_tickets(tickets)
            
        elif choice in ("1", "3", "4", "5", "6", "7", "8"):
            print(f"\nOption {choice} is not implemented yet.")

        else:
            print("\nInvalid option. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()