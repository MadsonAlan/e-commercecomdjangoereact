from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Product, Order, OrderItem, ShippingAddress, Review
from faker import Faker
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados fictícios para testes'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')

        # Usuários
        users = []
        for _ in range(50):
            user = User.objects.create_user(
                username=fake.unique.user_name(),
                email=fake.unique.email(),
                password='123456',
                first_name=fake.first_name(),
                last_name=fake.last_name()
            )
            users.append(user)
        self.stdout.write(self.style.SUCCESS('Usuários criados.'))

        # Produtos
        products = []
        for _ in range(150):
            product = Product.objects.create(
                user=random.choice(users),
                name=fake.unique.word().capitalize(),
                image='/images/placeholder.png',
                brand=fake.company(),
                category=fake.word(),
                description=fake.text(max_nb_chars=200),
                rating=round(random.uniform(1, 5), 2),
                numReviews=random.randint(0, 100),
                price=round(random.uniform(10, 1000), 2),
                countInStock=random.randint(0, 50),
            )
            products.append(product)
        self.stdout.write(self.style.SUCCESS('Produtos criados.'))

        # Reviews
        for product in products:
            for _ in range(random.randint(1, 3)):
                Review.objects.create(
                    product=product,
                    user=random.choice(users),
                    name=fake.first_name(),
                    rating=random.randint(1, 5),
                    comment=fake.sentence(),
                )
        self.stdout.write(self.style.SUCCESS('Reviews criadas.'))

        # Pedidos
        orders = []
        for _ in range(100):
            user = random.choice(users)
            order = Order.objects.create(
                user=user,
                paymentMethod=random.choice(['pix', 'boleto', 'cartao']),
                taxPrice=round(random.uniform(1, 50), 2),
                shippingPrice=round(random.uniform(10, 100), 2),
                totalPrice=round(random.uniform(100, 2000), 2),
                isPaid=random.choice([True, False]),
                paidAt=fake.date_time_this_year() if random.choice([True, False]) else None,
                isDeliver=random.choice([True, False]),
                deliveredAt=fake.date_time_this_year() if random.choice([True, False]) else None,
            )
            orders.append(order)
        self.stdout.write(self.style.SUCCESS('Pedidos criados.'))

        # Itens do Pedido
        for order in orders:
            for _ in range(random.randint(1, 40)):
                product = random.choice(products)
                OrderItem.objects.create(
                    product=product,
                    order=order,
                    name=product.name,
                    qty=random.randint(1, 5),
                    price=product.price,
                    image=product.image or '/images/placeholder.png',
                )
        self.stdout.write(self.style.SUCCESS('Itens de pedidos criados.'))

        # Endereços de entrega
        for order in orders:
            ShippingAddress.objects.create(
                order=order,
                address=fake.street_address(),
                city=fake.city(),
                postalCode=fake.postcode(),
                country='Brasil',
                shippingPrice=order.shippingPrice,
            )
        self.stdout.write(self.style.SUCCESS('Endereços de entrega criados.'))

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))