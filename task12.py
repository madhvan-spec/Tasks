import json
import os

class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                return json.load(file)
        else:
            print(f"Config file {self.config_file} not found.")
            return {}

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)
        print(f"Configuration saved to {self.config_file}")

    def get(self, section, key=None):
        if section in self.config:
            if key:
                return self.config[section].get(key)
            return self.config[section]
        return None

    def set(self, section, key, value):
        if section not in self.config:
            self.config[section] = {}
        self.config[section][key] = value
        print(f"Updated {section} -> {key} to {value}")

    def remove(self, section, key):
        if section in self.config:
            if key in self.config[section]:
                del self.config[section][key]
                print(f"Removed {key} from {section}")
            else:
                print(f"{key} not found in {section}")
        else:
            print(f"{section} section not found.")

    def print_config(self):
        print(json.dumps(self.config, indent=4))


def display_menu():
    
    print("\nConfiguration Manager Menu:")
    print("1. View Current Configuration")
    print("2. Get Configuration Value")
    print("3. Set Configuration Value")
    print("4. Remove Configuration Value")
    print("5. Save Changes")
    print("6. Exit")


def main():
    config_manager = ConfigManager('config.json')
    
    while True:
        input("Press Any Key to Continue: ")

        display_menu()
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == '1':
            config_manager.print_config()


        elif choice == '2':
            section = input("Enter section name (e.g., 'database', 'server'): ").strip()
            key = input("Enter key name (or leave blank to view entire section): ").strip()
            if key:
                value = config_manager.get(section, key)
                if value:
                    print(f"{section} -> {key}: {value}")
                else:
                    print(f"{key} not found in {section}.")
            else:
                section_data = config_manager.get(section)
                if section_data:
                    print(f"{section}: {json.dumps(section_data, indent=4)}")
                else:
                    print(f"Section '{section}' not found.")

        elif choice == '3':
            section = input("Enter section name (e.g., 'database', 'api_keys'): ").strip()
            key = input("Enter key name: ").strip()
            value = input("Enter value: ").strip()
            config_manager.set(section, key, value)

        elif choice == '4':
            section = input("Enter section name (e.g., 'database', 'api_keys'): ").strip()
            key = input("Enter key name to remove: ").strip()
            config_manager.remove(section, key)

        elif choice == '5':
            config_manager.save_config()

        elif choice == '6':
            print("Exiting the configuration manager.")
            break

        else:
            print("Invalid choice, please try again.")


main()
