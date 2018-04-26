class st:
    s = ""

    def get_String(self, ss):
        self.s = ss

    def print_String(self):
        return print(self.s.upper())


s1 = st()
st.get_String(s1, "hello")
st.print_String(s1)
