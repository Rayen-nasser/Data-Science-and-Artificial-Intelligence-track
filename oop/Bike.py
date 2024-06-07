class Bike:
    def __init__(self, description, cost, sale_price, condition):
        """
        Initializes a new bike instance.

        :param description: Description of the bike.
        :param cost: Cost price of the bike.
        :param sale_price: Sale price of the bike.
        :param condition: Condition of the bike as a float between 0 and 1.
        """
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition
        self.sold = False

    def update_sale_price(self, sale_price):
        """
        Updates the sale price of the bike if it has not been sold.

        :param sale_price: The new sale price of the bike.
        """
        if self.sold:
            print('Action not allowed, Bike has already been sold')
        else:
            self.sale_price = sale_price

    def sell(self):
        """Marks the bike as sold."""
        self.sold = True

    def __str__(self):
        """Returns a string representation of the bike."""
        return f"{self.description}, Cost: {self.cost}, Sale Price: {self.sale_price}, Condition: {self.condition}, Sold: {self.sold}"

# Example usage
bike1 = Bike('Mountain Bike', 100, 500, 0.5)
bike2 = Bike('Road Bike', 200, 450, 0.8)
bike3 = Bike('Hybrid Bike', 300, 650, 0.4)

bike1.update_sale_price(600)
bike1.sell()
bike1.update_sale_price(900)
bike2.update_sale_price(800)

print(bike1)
print(bike2)

# # Output the details of the bikes
# bikes = [bike1, bike2, bike3]
# for bike in bikes:
#     print(bike)
