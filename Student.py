class Student:
    def __init__(self, name, dept, sem, event1, event2):
        self.name = name
        self.dept = dept
        self.sem = sem

        if event1 == "SP":
            self.event1 = "Shot Put"
        elif event1 == "DT":
            self.event1 = "Discuss Throw"
        elif event1=="LJ":
            self.event1="Long Jump"
        elif event1=="FOOTBALL" or "VOLLEYBALL" or "CRICKET" or "BASKETBALL":
            self.event1=event1
        else:
            self.event1 = event1 + " Sprint"

        if event2 == "SP":
            self.event2 = "Shot Put"
        elif event2 == "DT":
            self.event2 = "Discuss Throw"
        elif event2 == "":
            self.event2 = ""
        elif event2=="LJ":
            self.event2="Long Jump"
        else:
            self.event2 = event2 + " Sprint"
