class Employee:
    def __init__(self, firs_name, last_name):
        self.firs_name = firs_name
        self.last_name = last_name
        self.fullname = firs_name + ' ' + last_name
        self.email = firs_name.lower() + '.' + last_name.lower() + '@company.com'
    def __repr__(self):
        return "Your fullname is: %s\nYour email is: %s" %(self.fullname, self.email)
