def main():
    name = input("whats your name? ").strip().title()
    hello(name)

def hello(name="world"):
    print("hello ",name)


main()


# asking the user for their name
# & clean and capitalize via chained
#name = input("whats your name? ").strip().title()

# say hi to user (First name)
# the f makes it formated it properly accepting the inserted variable string
#print(f"hello, {name}")


# split user name into first and last
#first, last = name.split(" ")
# clean input, ie remove whitespace
#name.strip()
#capitalize input
#name.capitalize() -- only does first letter
#name.title() 