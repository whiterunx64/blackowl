
#!/usr/bin/env python3

from modules.system import System
from modules.blackarch import BlackArchData
from modules.installer import Installer
from modules.menu import MenuManager

def main():
    system = System()
    data = BlackArchData()
    installer = Installer(system)
    menu = MenuManager(system, data, installer)
    menu.main_menu()

if __name__ == "__main__":
    main()

