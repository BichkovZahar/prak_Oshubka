class UserNotFoundError(Exception) :
    def __init__(self , username):
        self.username = username

class UserDatabase:
    def __init__(self):
       self.dict_user = {
           'nomer_1' : {'name' : 'Zahar' , 'age' : 15} ,
           'nomer_2' : {'name' : 'Anastasia' , 'age' : 17}
       }
    def get_user(self , user_name):
       if user_name in self.dict_user:
           return self.dict_user[user_name]
       else:
           raise UserNotFoundError(user_name)
finish = UserDatabase()
try:
    user_1 = finish.get_user("nomer_1")
    print(f"{user_1} знайдено в базі")
except UserNotFoundError as a :
    print(f"{a.username} не був знайдений")
