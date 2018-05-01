class St:
    s = ""

    def get_String(self):
        self.s = input("Enter your string: ")

    def print_String(self):
        print(self.s.upper())


s1 = St()
s1.get_String()
s1.print_String()