
main_menu = """
WELCOME TO NOKIA

1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
0. Exit
"""

print(main_menu)
main_menu_choice = int(input())

match main_menu_choice:
    case 1:
        print("Phone book")
        phone_book_menu = """
        Enter: 1 Search
        Enter: 2 Service Nos
        Enter: 3 Add Name
        Enter: 4 Erase
        Enter: 5 Edit
        Enter: 6 Assign tone
        Enter: 7 Send b'card
        Enter: 8 Options
        Enter: 9 Speed dials
        Enter: 10 Voice tags
        """
        print(phone_book_menu)
        phone_book_choice = int(input())

        match phone_book_choice:
            case 1:
                print("Search")
            case 2:
                print("Service Nos")
            case 3:
                print("Add Name")
            case 4:
                print("Erase")
            case 5:
                print("Edit")
            case 6:
                print("Assign tone")
            case 7:
                print("send b'card")
            case 8:
                print("Options")
                options_menu = """
                Enter: 1 Type of view
                Enter: 2 Memory status
                """
                print(options_menu)
                option_choice = int(input())

                match option_choice:
                    case 1:
                        print("Type of view")
                    case 2:
                        print("Memory status")
                    case _:
                        print("Error")
            case 9:
                print("Speed Dial")
            case 10:
                print("Voice Tag")
            case _:
                print("Error")

    case 2:
        print("Message")
        message_menu = """
        Enter: 1 Write messages
        Enter: 2 inbox
        Enter: 3 Outbox
        Enter: 4 Picture messages
        Enter: 5 Templates
        Enter: 6 Smileys
        Enter: 7 Message settings
        Enter: 8 Info services
        Enter: 9 Voice mailbox
        Enter: 10 Services
        """
        print(message_menu)
        message_choice = int(input())

        match message_choice:
            case 1:
                print("Write messages")
            case 2:
                print("inbox")
            case 3:
                print("Outbox")
            case 4:
                print("Picture Messages")
            case 5:
                print("Templates")
            case 6:
                print("Smileys")
            case 7:
                print("Message settings")
                message_settings_menu = """
                Enter: 1 Set1
                Enter: 2 Common
                """
                print(message_settings_menu)
                message_settings_choice = int(input())

                match message_settings_choice:
                    case 1:
                        print("set1")
                        set1_menu = """
                        Enter 1: Message centre number
                        Enter 2: Message sent as
                        Enter 3: Message validity
                        """
                        print(set1_menu)
                    case 2:
                        print("Common")
                        common_menu = """
                        Enter 1: Delivery Reports
                        Enter 2: Reply via same centre
                        Enter 3: Character support
                        """
                        print(common_menu)
                    case _:
                        print("Error")
            case 8:
                print("Info services")
            case 9:
                print("Voice mailbox")
            case 10:
                print("Services")
            case _:
                print("Error")

    case 3:
        print("Chat Loading....")

    case 4:
        print("Call Register")
        call_register_menu = """
        Enter: 1 Missed calls
        Enter: 2 Recived
        Enter: 3 Dialled number
        Enter: 4 Erased recent call lists
        Enter: 5 Show call duration
        Enter: 6 Show call cost
        Enter: 7 All calls settings
        Enter: 8 Prepaid Credit
        """
        print(call_register_menu)
        call_register_choice = int(input())

        match call_register_choice:
            case 1:
                print("Missed calls")
            case 2:
                print("Recieved")
            case 3:
                print("Dialled number")
            case 4:
                print("Erased recent call list")
            case 5:
                print("Show call duration")
                show_call_duration_menu = """
                Enter: 1 Last call Duration
                Enter: 2 All calls duration
                Enter: 3 Recieved Calls duration
                Enter: 4 Dailled calls duration
                Enter: 5 Clear timmers
                """
                print(show_call_duration_menu)
            case 6:
                print("Show call cost")
                show_call_cost_menu = """
                Enter: 1 Last call cost
                Enter: 2 All calls cost
                Enter: 3 Clear account
                """
                print(show_call_cost_menu)
            case 7:
                print("All calls Settings")
                call_cost_list = """
                Enter: 1 Call cost limit
                Enter: 2 Show costs in
                """
                print(call_cost_list)
            case 8:
                print("Prepaid credit loading.....")
            case _:
                print("Error")

    case 5:
        print("Tones")
        tones_menu = """
        Enter: 1 Ringing tone
        Enter: 2 Ringing Volume
        Enter: 3 Incoming
        Enter: 4 Composer
        Enter: 5 Message alert tone
        Enter: 6 Keypad tones
        Enter: 7 Warning and game tones
        Enter: 8 Vibrating alert
        Enter: 9 Screen saver
        """
        print(tones_menu)

    case 6:
        print("Settings")
        settings_menu = """
        Enter: 1 Call settings
        Enter: 2 Phone Settings
        Enter: 3 Security settings
        Enter: 4 Restore factory settings
        """
        print(settings_menu)
        settings_choice = int(input())

        match settings_choice:
            case 1:
                print("Call settings")
                call_setting_list = """
                Enter: 1 Automatic redial
                Enter: 2 Speed dialling
                Enter: 3 Call waiting options
                Enter: 4 Own number sending
                Enter: 5 Phone line in use
                Enter: 6 Automatic answer
                """
                print(call_setting_list)
            case 2:
                print("Phone Settings")
                phone_setting_list = """
                Enter: 1 Language
                Enter: 2 Cell info display
                Enter: 3 Welcome note
                Enter: 4 Network selection
                Enter: 5 Lights
                Enter: 6 Confirm SIM service actions
                """
                print(phone_setting_list)
            case 3:
                print("Security settings")
                security_setting_list = """
                Enter: 1 PIN code request
                Enter: 2 Call barring service
                Enter: 3 Fixed dialling
                Enter: 4 Closed user group
                Enter: 5 Phone security
                Enter: 6 Change access code
                """
                print(security_setting_list)
            case 4:
                print("Restore factory settings loading....")
            case _:
                print("Error")

    case 7:
        print("call divert loading...")

    case 8:
        print("Games loading...")

    case 9:
        print("calculator loading....")

    case 10:
        print("Reminder loading....")

    case 11:
        print("Clock")
        clock_list = """
        1: Alarm clock
        2: Clock Settings
        3: Date settings
        4: Stopwatch
        5: Countdown timer
        6: Auto update of date and Time
        """
        print(clock_list)

    case 12:
        print("Profile Loading....")

    case 13:
        print("SIM services loading....")

    case _:
        print("Error")
