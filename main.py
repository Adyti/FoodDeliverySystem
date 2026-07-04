from app import App
from database.sqlite_database import SQLiteDatabase
from repositories.customer_repository import SQLiteCustomerRepository
from repositories.restaurant_repository import SQLiteRestaurantRepository
from repositories.order_repository import SQLiteOrderRepository
from services.customer_service import CustomerService
from services.restaurant_service import RestaurantService
from services.order_service import OrderService
from controllers.customer_controller import CustomerController
from controllers.restaurant_controller import RestaurantController
from controllers.order_controller import OrderController
from cli.cli import CLI


database = SQLiteDatabase()

customer_repository = SQLiteCustomerRepository(database)
restaurant_repository = SQLiteRestaurantRepository(database)
order_repository = SQLiteOrderRepository(database)

customer_service = CustomerService(customer_repository)
restaurant_service = RestaurantService(restaurant_repository)
order_service = OrderService(order_repository, customer_service, restaurant_service)

customer_controller = CustomerController(customer_service)
restaurant_controller = RestaurantController(restaurant_service)
order_controller = OrderController(order_service, customer_controller, restaurant_controller)

cli = CLI(customer_controller, restaurant_controller, order_controller)

app = App(cli)
app.run()