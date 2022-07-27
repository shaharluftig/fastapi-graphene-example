from typing import List

import graphene
from graphene import ObjectType, Field, String, Int

from graphql.queries.student import Student


class Query(ObjectType):
    student = Field(Student, fullName=String(), grades=graphene.List(Int))

    def resolve_student(parent, info, fullName: str, grades: List[int]):
        splittedName = fullName.split(" ")
        if len(splittedName) == 2:
            first_name, last_name = splittedName
            return Student(firstName=first_name, lastName=last_name, grades=grades)
        return Student(firstName=fullName, lastName=None, grades=grades)
