from sqlalchemy.orm import Session
from ..models.orders import Order as OrderModel
from ..models.order_details import OrderDetail as OrderDetailModel
from ..models.guest_order import GuestOrder as GuestOrderModel
from ..models.menu import MenuItem as MenuItemModel
from ..models.feedback import Feedback as FeedbackModel
from ..models.promotion import Promotion as PromotionModel
from ..models.customers import Customer as CustomerModel
from ..models.payments import Payment as PaymentModel
from ..models.resources import Resource as ResourceModel
from ..dependencies.database import engine

def populate_data():
    session = Session(bind=engine)

    # Clear existing data
    session.query(OrderModel).delete()
    session.query(OrderDetailModel).delete()
    session.query(GuestOrderModel).delete()
    session.query(MenuItemModel).delete()
    session.query(FeedbackModel).delete()
    session.query(PromotionModel).delete()
    session.query(CustomerModel).delete()
    session.query(PaymentModel).delete()
    session.query(ResourceModel).delete()

    # Sample data
    orders = [
        OrderModel(customer_name="John Doe", description="First order"),
        OrderModel(customer_name="Jane Smith", description="Second order"),
        OrderModel(customer_name="Alice Johnson", description="Third order")
    ]

    order_details = [
        OrderDetailModel(order_id=1, sandwich_id=1, amount=2),
        OrderDetailModel(order_id=2, sandwich_id=2, amount=1),
        OrderDetailModel(order_id=3, sandwich_id=3, amount=3)
    ]

    guest_orders = [
        GuestOrderModel(customer_name="Michael Brown", phone="123-456-7890", address="123 Main St", order_description="Guest order 1"),
        GuestOrderModel(customer_name="Laura White", phone="987-654-3210", address="456 Elm St", order_description="Guest order 2")
    ]

    menu_items = [
        MenuItemModel(name="Ham Sandwich", ingredients="Ham, Bread, Lettuce", price=5.99, calories=250, category="Sandwich"),
        MenuItemModel(name="Cheese Sandwich", ingredients="Cheese, Bread, Tomato", price=4.99, calories=200, category="Sandwich")
    ]

    feedbacks = [
        FeedbackModel(customer_name="John Doe", rating=5, comments="Great service!"),
        FeedbackModel(customer_name="Jane Smith", rating=4, comments="Good food!")
    ]

    promotions = [
        PromotionModel(code="HOLIDAY20", discount_percentage=20.0, description="Holiday Discount", is_active=1),
        PromotionModel(code="LOYALTY10", discount_percentage=10.0, description="Loyalty Program", is_active=1)
    ]

    customers = [
        CustomerModel(name="John Doe", email="john.doe@example.com", phone="123-456-7890", address="123 Main St"),
        CustomerModel(name="Jane Smith", email="jane.smith@example.com", phone="987-654-3210", address="456 Elm St")
    ]

    payments = [
        PaymentModel(card_info="4111 1111 1111 1111", transaction_status="Success", payment_type="Credit"),
        PaymentModel(card_info="4222 2222 2222 2222", transaction_status="Pending", payment_type="Debit")
    ]

    resources = [
        ResourceModel(name="Bread", amount=100.0, unit="kg"),
        ResourceModel(name="Cheese", amount=50.0, unit="kg")
    ]

    # Insert data
    session.add_all(orders)
    session.add_all(order_details)
    session.add_all(guest_orders)
    session.add_all(menu_items)
    session.add_all(feedbacks)
    session.add_all(promotions)
    session.add_all(customers)
    session.add_all(payments)
    session.add_all(resources)

    session.commit()
    session.close()
    print("Data population complete")

if __name__ == "__main__":
    populate_data()
