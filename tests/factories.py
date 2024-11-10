# tests/factories.py
from faker import Faker
import random

fake = Faker()

class ProductFactory:
    @staticmethod
    def create_fake_product():
        product = {
            "product_id": fake.uuid4(),
            "name": fake.word().capitalize(),
            "description": fake.sentence(),
            "price": round(random.uniform(10.0, 100.0), 2),
            "category": fake.word().capitalize(),
            "stock_quantity": random.randint(1, 100),
            "created_at": fake.date_time_this_year(),
            "updated_at": fake.date_time_this_year(),
        }
        return product

# Example usage: creating a list of fake products
def create_fake_products_list(count=10):
    return [ProductFactory.create_fake_product() for _ in range(count)]

# Generating a sample list of fake products for testing
if __name__ == "__main__":
    fake_products = create_fake_products_list(5)
    for product in fake_products:
        print(product)
