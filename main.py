from try_integration import create_ticket
# from campusflow.tickets import create_ticket
from campusflow.workflow import (
    list_tickets,
    view_ticket,
    assign_ticket,
    update_ticket_status
)

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

        elif choice == "1":
            print("\n--- Create New Ticket ---")
            
            title = input("Enter ticket title: ")
            category = input("Enter category (Network/Hardware/Software/Other): ")
            urgency = input("Enter urgency (low/medium/high): ")
            affected_users_input = input("Enter number of affected users: ")
            
            try:
                affected_users = int(affected_users_input)
                
                new_ticket = create_ticket(
                    title,
                    category,
                    urgency,
                    affected_users,
                    tickets
                    
                )
                
                tickets.append(new_ticket)
                
                print(f"\nTicket {new_ticket['id']} created successfully!")
                print(f"Priority: {new_ticket['priority']}")
            
            except ValueError as error:
                print(f"\nCould not create ticket: {error}")

        elif choice == "2":
            list_tickets(tickets)

        elif choice == "3":
            print("\n--- View Ticket ---")
            
            ticket_id = input("Enter ticket ID: ").strip().upper()

            ticket = view_ticket(tickets, ticket_id)

            if ticket is None:
                print("\nTicket not found.")

            else:
                print("\nTicket Details")
                print("--------------------------")
                print(f"ID: {ticket['id']}")
                print(f"Title: {ticket['title']}")
                print(f"Category: {ticket['category']}")
                print(f"Urgency: {ticket['urgency']}")
                print(f"Affected Users: {ticket['affected_users']}")
                print(f"Priority: {ticket['priority']}")
                print(f"Status: {ticket['status']}")
                print(f"Assigned To: {ticket['assigned_to'] or 'Unassigned'}")

        elif choice == "4":
            print("\n--- Assign Ticket ---")

            ticket_id = input("Enter ticket ID: ").strip().upper()
            staff_name = input("Enter staff name: ").strip()

            result = assign_ticket(tickets, ticket_id, staff_name)

            print(f"\n{result}")

        elif choice == "5":
            print("\n--- Update Ticket Status ---")

            ticket_id = input("Enter ticket ID: ").strip().upper()

            print("\nAvailable status updates:")
            print("1. Start Work (in_progress)")
            print("2. Resolve Ticket (resolved)")

            status_choice = input("Choose an option (1-2): ").strip()

            if status_choice == "1":
                new_status = "in_progress"

            elif status_choice == "2":
                new_status = "resolved"

            else:
                print("\nInvalid status option.")
                continue

            result = update_ticket_status(tickets, ticket_id, new_status)

            print(f"\n{result}")
            
        elif choice in ("6", "7", "8"):
            print(f"\nOption {choice} is not implemented yet.")

        else:
            print("\nInvalid option. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()