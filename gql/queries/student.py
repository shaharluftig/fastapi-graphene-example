from graphene import String, ObjectType, List, Int, Float


class Student(ObjectType):
    """ A class that represents a student with its abilities"""
    firstName = String()
    lastName = String()
    grades = List(Int)
    gradesAvg = Float()

    def resolve_gradesAvg(parent, info):
        return sum(parent.grades) / len(parent.grades)
