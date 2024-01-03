
from user import User
from chat_room import ChatRoom


def get_user_input(prompt):
    return input(f"{prompt}: ")

if __name__ == "__main__":

    # My users
    user1 = User(1, "Rama", "ram@gmail.com")
    user2 = User(2, "Hari", "Hari@gmail.com")
    user3 = User(33, "ALex","alexe@gmail.com")
    user4 = User(65, "Bidhan", "bidhanb@gmail.com")
    user5 = User(87, "Minaksi","Minaksi11@gmail.com")

    group_chat = ChatRoom([user1, user2, user3])

    while True:
        print("\n1. Send Message")
        print("2. Display Messages")
        print("3. Create Group Chat")
        print("4. Send Group Message")
        print("5. View Group Members")
        print("6. Exit")

        choice = get_user_input("Enter your choice")

        if choice == "1":
            try:
                sender_id = int(get_user_input("Enter your user ID"))
                recipient_id = int(get_user_input("Enter the recipient's user ID"))
                content = get_user_input("Enter your message content")

                sender = user1 if sender_id == 1 else user2
                recipient = user1 if recipient_id == 1 else user2

                sender.send_message(content, recipient)
                print("Message sent successfully!")

            except ValueError:
                print("Invalid input. Please enter a valid user ID.")

        elif choice == "2":
            user1.display_messages()
            user2.display_messages()

        elif choice == "3":
            try:
                new_user_id = int(get_user_input("Enter user ID to add to the group chat"))
                new_user = user1 if new_user_id == 1 else user2
                group_chat.participants.append(new_user)
                print(f"{new_user.username} added to the group chat!")

            except ValueError:
                print("Invalid input. Please enter a valid user ID.")

        elif choice == "4":
            try:
                sender_id = int(get_user_input("Enter your user ID"))
                content = get_user_input("Enter group message content")

                sender = user1 if sender_id == 1 else user2
                group_chat.send_group_message(content, sender)
                print("Group message sent successfully!")

            except ValueError:
                print("Invalid input. Please enter a valid user ID.")

        elif choice == "5":
            members = group_chat.get_members()
            print(f"\nGroup Members: {', '.join(members)}")

        elif choice == "6":
            print("Exiting the messaging system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
