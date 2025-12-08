from faker import Faker


fake = Faker()
Faker.seed(1234)


def generate(size):
    users = []
    for _ in range(size):
        users.append({
            'name': fake.name,
            'email': fake.email
        })
    return users


users = generate(20)
