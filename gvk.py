def wish(name):
    print("good morning",name)
greeting=wish
print(id(wish))
print(id(greeting))

greeting("gvk")
wish("rk")

wish('kumar')
greeting("kumar")
