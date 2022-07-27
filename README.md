# fastapi-graphene-example

A simple fastapi and graphene example using python

Routes:
- /graphql: GraphQL endpoint

### GraphQL query sample:
```
{
  student(fullName:"John Doe",grades:[100,80,70,90]) `{
    firstName
    lastName
    grades
    gradesAvg
  }
}
```
