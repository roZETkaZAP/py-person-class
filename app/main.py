class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people):
    result = []
    for person in people:
        p = Person(person["name"], person["age"])
        result.append(p)
    for pep_data in people:
        pers = Person.people[pep_data["name"]]
        wife_name = pep_data.get("wife")
        if wife_name:
            pers.wife = Person.people[wife_name]
        husband_name = pep_data.get("husband")
        if husband_name:
            pers.husband = Person.people[husband_name]
    return result
