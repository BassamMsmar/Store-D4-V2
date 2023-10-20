import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()



from faker import Faker
import random
from product.models import Brand, Product



def seed_brand(n):
    fake = Faker()
    image = ['samsung.png', 'PlayStation.png', 'apple.png']
    for _ in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f'brand/{image[random.randint(0,2)]}'
        )
    
    print(f'seed {n} Brands succssfuly')



def seed_product(n):
    fake = Faker()
    image = [
        'N40633047A_1.webp',
        'N50910420A_1.webp', 
        'N53374466A_3.webp' ,
        'N53374466A_2.webp', 
        'N50910420A_4.webp', 
        'N53374466A_3.webp', 
        'N53374466A_2.webp', 
        'N53346840A_2.webp', 
        'N50910420A_1.webp', 
        'N50863794A_2.webp', 
           ]
    
    falgs = ['Sale','New','Feature',]

    for _ in range(n):
        Product.objects.create(
            name = fake.name(),
            image = f'products/{image[random.randint(0,9)]}',
            flag = falgs[random.randint(0,2)],
            price = round(random.uniform(500.99,1990.99), 2),
            sku = random.randint(1000,9999),
            subtitle = fake.text(max_nb_chars=300),
            tag = fake.name(),
            descriptions = fake.text(max_nb_chars=2000 ),
            quantity = random.randint(24, 100),
            brand = Brand.objects.get(id=random.randint(109,205))

        )
    
    print(f'seed {n} Product succssfuly')


seed_product(1500)