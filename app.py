import graphene
from graphene import Field, List, String
from mutation import CreateUser, UpdateUser, DeleteUser
from query import Query
from type import User

class MyMutations(graphene.ObjectType):

    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

class MyQuery(Query):
    user = Field(User)
    get_user = Field(User, id=String())
    get_users = List(User)


schema = graphene.Schema(query=MyQuery, mutation=MyMutations)

# result = schema.execute(
#     '''
#    mutation {
#         createUser(id: "1", name: "Bubi", email: "k@p.com", password: "123456"){
#             user {
#                   id
#                   name
#                   email
#                   password
#                 }
#             }
#     }
#     '''
# )
result = schema.execute(
        '''

            query {
                    getUser(id: "1") {
                                        name
                                        email
                        }
                    getUsers {
                                    id
                    }
                }

        '''
)

print(result)
