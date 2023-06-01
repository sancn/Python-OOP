class Order:
    def __init__(self,order_id,customer):
        self.order_id=order_id
        self.customer=customer
    def calculate_total_price(self):
        # calculate the total price of the order
        pass
    def save_to_database(self):
        #saves the order to the databse 
        pass
    def send_confirmation_email(self):
        #sends a confirmation email to the customer
        pass
    
    """
    In the above code, the Order class has multiple responsibilities.
    It is responsible for calculating the total price of the order, saving the order to the database,
    and sending a confirmation email to the customer.
    This violates the SRP because the class has more than one reason to change.
    If any of these responsibilities need to be modified or added in the future,
    it will require changes to the Order class.

    """

class Order:
  def __init__(self, order_id, customer):
      self.order_id = order_id
      self.customer = customer


class OrderCalculator:
    def calculate_total_price(self, order):
        # Calculates the total price of the order
        pass


class OrderDatabaseManager:
    def save_to_database(self, order):
        # Saves the order to the database
        pass


class EmailSender:
    def send_confirmation_email(self, order):
        # Sends a confirmation email to the customer
        pass

