class SingletonClass(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'instance'):
            cls.instance = super(SingletonClass,cls).__new__(cls)
        return cls.instance

singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton is new_singleton)
singleton.singl_var = "Singleton Variable"
print(new_singleton.singl_var)

# One instance created . Child will have same state in instance as parent.
class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(SingletonClass,cls).__new__(cls)
        return cls.instance

class SingletonChild(SingletonClass):
    pass

singleton = SingletonClass()
child = SingletonChild()
print(child is singleton)

singleton.singl_var = "Single Variable"
print(child.single_var)



