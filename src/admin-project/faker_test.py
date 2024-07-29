from faker import Faker
# from faker.providers import 


fake = Faker()

for _ in range(1000):
    print(fake.unique.user_name())
    # print(fake.address())
    
