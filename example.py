from graphene import Schema, ObjectType, String, Int, Field, List, Boolean, Mutation


class UserType(ObjectType):
    id = Int()
    name = String()
    email = String()
    is_active = Boolean()


class CreateUser(Mutation):
    class Arguments:
        name = String()
        email = String()
        is_active = Boolean()

    user = Field(UserType)

    @staticmethod
    def mutate(root, info, name, email, is_active):
        user = {"id": len(Query.users_data) + 1, "name": name, "email": email, "is_active": is_active}
        Query.users_data.append(user)
        return CreateUser(user=user)


class UpdateUser(Mutation):
    class Arguments:
        user_id = Int(required=True)
        name = String()
        email = String()

    user = Field(UserType)

    @staticmethod
    def mutate(root, info, user_id, name=None, email=None):
        for user in Query.users_data:
            if user.get("id") == user_id:
                user["name"] = name
                user["email"] = email


class Mutation(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()


class Query(ObjectType):
    user = Field(UserType, user_id=Int())
    user_is_active = List(UserType, is_active=Boolean())

    users_data = [
        {"id": 1, "name": "Alex", "email": "alex@gmail.com", "is_active": False},
        {"id": 2, "name": "Bob", "email": "bob@gmail.com", "is_active": False},
        {"id": 3, "name": "Tony", "email": "tony@gmail.com", "is_active": True},
        {"id": 4, "name": "Logan", "email": "logan@gmail.com", "is_active": True},
    ]

    @staticmethod
    def resolve_user(root, info, user_id):
        for user in Query.users_data:
            if user.get("id") == user_id:
                return user
        return None

    @staticmethod
    def resolve_user_is_active(root, info, is_active):
        return [user for user in Query.users_data if user.get("is_active") == is_active]


schema = Schema(query=Query, mutation=Mutation)

gql_one = """
    query{
        user(userId: 5){
            id
            name
            email
        }
    }
"""

gql_two = """
    mutation {
        createUser(name:"Peter", email: "peter@gmail.com",isActive: true){
            user{
                id
                name
                email
                isActive
            }
        }    
    }

"""

gql_three = """
    mutation {
        updateUser(userId: 2, name: "Clark", email: "cc@gmail.com"){
            user{
                id
                name
                email
            }
        }
    }

"""

if __name__ == "__main__":
    # result_two = schema.execute(gql_two)
    # print(result_two)

    # result_one = schema.execute(gql_one)
    # print(result_one)

    result_three = schema.execute(gql_three)
