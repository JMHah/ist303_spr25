# demonstration of observer pattern

class Person:
    def __init__(self, fname="Jane", lname="Doe", posts:list=[]):
        self.fname = fname 
        self.lname = lname
        self.posts = posts
        self.observers = []
        self.events = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def view_observers(self):
        print(f'{self.fname} {self.lname} has {len(self.observers)} observers:')
        for observer in self.observers:
            print(f'{observer.fname} {observer.lname}')
    
    #loop through subscribed observers; self represents broadcasting object
    # messager passes broadcasting object to the update method
    def notify_observers(self, event_data):
        self.posts.append(event_data)
        messager = self # broadcaster/messager
        for observer in self.observers:
            observer.update(messager=messager, event_data=event_data)
    
    #function called by each observer; self represents an observer obj
    def update(self, messager, event_data):
        self.events.append(event_data)
        print(f"{self.fname} {self.lname} got a message from {messager.fname} {messager.lname}: {event_data}")

#instantiate some sample objects
# for use in an interactive session: import observer, then assign p1,p2,p3,p4 = observer.main()
def main():
  p1 = Person(fname="Paul",lname="McCartney",posts=[23,45,66])
  p2 = Person(fname="Ringo",lname="Starr",posts=[12,13])
  p3 = Person(fname="George",lname="Harrison")
  p4 = Person(fname="John",lname="Lennon")
  p1.add_observer(p2)
  p1.add_observer(p3)
  return p1, p2, p3, p4