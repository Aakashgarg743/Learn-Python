import datetime
class Library:
    def __init__(self, libooks, liname):
        self._libooks = libooks
        self._linames = liname
        self.lenddic = {}

    def display(self):
        print(f"We have the following books in our library {self._linames}")
        for i in self._libooks:
            print(i)

    def lend(self, user, book):
        if book not in self.lenddic.keys():
            self.lenddic.update({book:user})
            with open("library.txt", "a") as f:
                f.write(f"{datetime.datetime.now()} : {book} - {user}\n")
            print("Database has been updated. You can take this book now...")
        else:
            print(f"This book {book} is already owned by {self.lenddic[book]}")

    def add(self, book):
        self._libooks.append(book)
        print("Book has been added...")

    def returnBook(self, book):
        self.lenddic.pop(book)


if __name__ == '__main__':
    aakash = Library(["python", "java", "c", "database"], "aakash")
    while True:
        print(f"Welcome to the {aakash._linames} library.\n")
        inpu = int(input("What you want to do??\nType-\n1: Display Books\n2: Lend Books\n3: Add Books\n4: Return Books\n"))
        if inpu == 1:
            aakash.display()
        elif inpu == 2:
            name = input("Enter your name: \n")
            book = input("Enter the book name you want to lend: \n")
            aakash.lend(name, book)
        elif inpu == 3:
            book = input("Enter the book name you want to add\n")
            aakash.add(book)
        elif inpu == 4:
            book = input("Enter the book name you want ot return: \n")
            aakash.returnBook(book)
        else:
            print("Enter a valid option...")

        print("Press q to quit and c to continue....\n")
        choice = input("Type here: \n")
        if choice == "c":
            continue
        elif choice == "q":
            quit()
        else:
            print("Wrong input")