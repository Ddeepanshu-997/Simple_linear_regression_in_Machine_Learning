class details:
    name="deepanshu"
    age=23
    address='jaipur'
    phone='nord 2'
    def desc(self):
        print('i m good to go')
    n='asdf'
    a='pqrs'
class details1(details):
    nickname ='himanshu'
    age='twenty three'
    phone=7985645216
class details2(details1):
    def personal(self):
        print(' my personal details are in the details and details1 class respectively')
obj=details2
print(obj.age)
print(obj.name)
print(obj.phone)