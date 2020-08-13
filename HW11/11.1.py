class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def compare_age(self):
        if self.age > 34:
            self.compare = "%s is older than me" %self.name
            return self.compare
        elif self.age < 34:
            self.compare = '%s is yonger than me' %self.name
            return self.compare
        else:
            self.compare = '%s the same age as me' %self.name
            return self.compare
    def __repr__(self):
        return self.compare
