def greet(name="John", surname="Doe"):
  print(f"Hello {name} {surname}!")

greet()

family = [
  ("Tristram", "Mcbride"),
  ("Baldwin", "Preston"),
  ("Wally", "Collins")
]

for member in family:
  greet(name=member[0], surname=member[1])