import weakref

class User:
    def __init__(self, name):
        self.name = name

admin = User('admin')
clone = weakref.ref(admin)

print(clone().name)
del admin
print(clone())
