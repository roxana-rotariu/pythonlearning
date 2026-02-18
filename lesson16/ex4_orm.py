from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Define base class for ORM models
Base = declarative_base()

# Define Product model
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"

def main():
    # Replace with your actual DB credentials
    DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/lesson16_db"

    # Create SQLAlchemy engine
    engine = create_engine(DATABASE_URL, echo=True)

    # Create all tables in DB (creates products table)
    Base.metadata.create_all(engine)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Open a session
    with Session() as session:
        # Insert 2 products
        product1 = Product(name="Laptop", price=999.99)
        product2 = Product(name="Smartphone", price=499.99)
        session.add_all([product1, product2])
        session.commit()

        # Query all products
        products = session.query(Product).all()

        # Print products
        for product in products:
            print(product)

if __name__ == "__main__":
    main()
