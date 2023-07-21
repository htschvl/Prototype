from colorama import init, Fore, Style

# Initialize colorama for Windows support
init(autoreset=True)

class MemberManager:
    def __init__(self):
        self.members = {}
        self.undistributed_yield = 0

    def add_member(self):
        """Add a new member to the list."""
        member_name = input(f"{Fore.CYAN}Enter the name of a new member: ")
        self.members[member_name] = 0
        print(f"{Fore.GREEN}✓ {member_name} has been added as a new member.")

    def show_members(self):
        """Display the list of members."""
        if not self.members:
            print(f"{Fore.RED}No members found.")
        else:
            print(f"{Fore.YELLOW}List of members:")
            for member in self.members:
                print(member)

    def show_undistributed_yield(self):
        """Display the undistributed yield."""
        print(f"{Fore.CYAN}Undistributed yield: {self.undistributed_yield}")

    def show_member_yield(self):
        """Show how much each member has for each yield."""
        if not self.members:
            print(f"{Fore.RED}No members found.")
            return

        print(f"{Fore.YELLOW}Member yields:")
        for member, yield_value in self.members.items():
            print(f"{member}: {yield_value}")

    def record_undistributed_yield(self):
        """Record a new undistributed yield."""
        while True:
            try:
                yield_value = int(input(f"{Fore.CYAN}Enter the yield value (non-negative integer): "))
                if yield_value >= 0:
                    break
                else:
                    print(f"{Fore.RED}The yield value must be a non-negative integer.")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a non-negative integer.")

        member_name = input(f"{Fore.CYAN}Enter the project name: ")
        self.undistributed_yield += yield_value
        print(f"{Fore.GREEN}✓ Recorded {yield_value} for {member_name}.")

    def distribute_yield(self):
        """Distribute the accumulated yields among members."""
        total_members = len(self.members)
        if total_members == 0:
            print(f"{Fore.RED}Cannot distribute yield as there are no members.")
            return
        if self.undistributed_yield == 0:
            print(f"{Fore.RED}No undistributed yield to distribute.")
            return

        equal_yield_amount = self.undistributed_yield // total_members
        self.undistributed_yield -= equal_yield_amount * total_members

        for member in self.members:
            self.members[member] += equal_yield_amount

        print(f"{Fore.GREEN}✓ Yield distributed among members.")

    def display_menu(self):
        """Display the main menu."""
        print("\n" + Fore.BLUE + r"""
  ____            _        _                        ____    _    ___  
 |  _ \ _ __ ___ | |_ ___ | |_ _   _ _ __   ___    |  _ \  / \  / _ \ 
 | |_) | '__/ _ \| __/ _ \| __| | | | '_ \ / _ \   | | | |/ _ \| | | |
 |  __/| | | (_) | || (_) | |_| |_| | |_) |  __/   | |_| / ___ \ |_| |
 |_|   |_|  \___/ \__\___/ \__|\__, | .__/ \___|___|____/_/   \_\___/ 
                               |___/|_|       |_____|                 """ + Style.RESET_ALL)
        print(Fore.YELLOW + "1- Show members")
        print(Fore.YELLOW + "2- Add member")
        print(Fore.YELLOW + "3- New yield")
        print(Fore.YELLOW + "4- Show undistributed yield")
        print(Fore.YELLOW + "5- Show member yields")
        print(Fore.YELLOW + "6- Distribute yield")
        print(Fore.RED + "0- Exit" + Style.RESET_ALL)

    def process_choice(self, choice):
        """Process the user's choice."""
        if choice == "1":
            self.show_members()
        elif choice == "2":
            self.add_member()
        elif choice == "3":
            self.record_undistributed_yield()
        elif choice == "4":
            self.show_undistributed_yield()
        elif choice == "5":
            self.show_member_yield()
        elif choice == "6":
            self.distribute_yield()
        elif choice == "0":
            print(f"{Fore.YELLOW}Exiting the application. Goodbye!")
            exit()
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.")

    def run(self):
        """Run the member manager application."""
        print(f"{Fore.CYAN}Welcome to the Member Manager Application!")
        while True:
            self.display_menu()
            selected_choice = input(f"{Fore.MAGENTA}Select your function (0-6): ")
            self.process_choice(selected_choice)


if __name__ == "__main__":
    member_manager = MemberManager()
    member_manager.run()
