import os, shutil

class FileManager:

    def create_file(self):
        filename = input("Enter the name of the file you want to create (with extension): ")
        if filename in os.listdir():
            print("A file with the given name already exists.")
            return
        should_write = input("Do you want to write something to the file? Choose: y/n: ")
        if should_write.lower() == "y":
            text = input("Enter the text you want to write to the file: ")
            with open(filename, "w") as file:
                file.write(text)
        else:
            with open(filename, "w"):
                pass

    def create_dir(self):
        dirname = input("Enter the name of the folder you want to create: ")
        os.mkdir(dirname)

    def remove_file(self):
        filename = input("Enter the name of the file you want to remove: ")
        os.remove(filename)

    def remove_dir(self):
        dirname = input("Enter the name of the folder you want to remove: ")
        try:
            os.rmdir(dirname)
        except FileNotFoundError:
            print(f"The folder {dirname} does not exist.")

    def copy_file(self):
        copied_filename = input("Enter the name of the file you want to copy: ")
        copy_filename = input("Enter the name of the copy file: ")
        try:
            shutil.copy(copied_filename, copy_filename)
        except FileNotFoundError:
            print(f"The file {copied_filename} does not exist.")

    def copy_dir(self):
        copied_dirname = input("Enter the name of the directory you want to copy: ")
        copy_dirname = input("Enter the name of the copy directory: ")

        try:
            shutil.copytree(copied_dirname, copy_dirname)
        except FileNotFoundError:
            print(f"The folder {copied_dirname} does not exist.")

    def move_file(self):
        filename = input("Enter the name of the file you want to move: ")
        dst_path = input("Enter the destination path to move the file to: ")
        shutil.move(filename, f"{dst_path}/{filename}")

    def move_dir(self):
        dirname = input("Enter the name of the directory you want to move: ")
        dst_path = input("Enter the destination path to move the directory to: ")
        shutil.move(dirname, f"{dst_path}/{dirname}")

    def show_dirs(self):
        dirs = os.listdir()
        for dirname in dirs:
            print(dirname)

    def show_border(self):
        print("-------------------")

    def get_choice(self):
        choice = int(input("Choose an option: "))
        return choice

    def show_menu(self):
        self.show_border()
        print("1. Create a file")
        print("2. Create a folder")
        print("3. Remove a file")
        print("4. Remove a folder")
        print("5. Copy a file")
        print("6. Copy a folder")
        print("7. Move a file")
        print("8. Move a folder")
        print("9. Display files and folders")
        print("10. Exit")
        self.show_border()
        choice = self.get_choice()

        if choice == 1:
            self.create_file()

        elif choice == 2:
            self.create_dir()

        elif choice == 3:
            self.remove_file()

        elif choice == 4:
            self.remove_dir()

        elif choice == 5:
            self.copy_file()

        elif choice == 6:
            self.copy_dir()

        elif choice == 7:
            self.move_file()

        elif choice == 8:
            self.move_dir()

        elif choice == 9:
            self.show_dirs()

        if choice == 10:
            print("Exiting...")
            exit()
            return

        if choice != 9:
            self.show_menu()

        else:
            input("Press any key to continue...")
            self.show_menu()

if __name__ == "__main__":
    fm = FileManager()

    fm.show_menu()
