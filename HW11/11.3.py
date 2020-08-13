class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.fullname = fname + ' ' + lname
        self.initials = fname[0]+'.'+lname[0]+'.'
    def __repr__(self):
        return 'Your fullname is: %s\nYour initials are: %s' %(self.fullname, self.initials)
