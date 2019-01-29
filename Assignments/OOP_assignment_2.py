class Shirt:
    # The parent class Shirt represents a shirt sold in a store
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
    # Method for initializing Shirt object

    def change_price(self, new_price):
        # This method changes the price of the shirt
        self.price = new_price

    def discount(self, discount):
        # This method applys a discount from the entered float number
        return self.price * (1 - discount)


class Pants:
    # This parent class of Pants represents Pants in a store
    def __init__(self, pants_color, waist_size, pants_length, pants_price):
        self.color = str(pants_color)
        self.size = int(waist_size)
        self.length = int(pants_length)
        self.price = float(pants_price)
    # This method initialzes the object Pants with arguments pants_color,
    # waist_size, pants_length, pants_price

    def change_price(self, new_price):
        # This method changes the price of the attribute of a pants object
        # Args:
        # new_price (float): The new price of the pants object
        self.price = new_price

    def discount(self, percentage):
        # This method applys a discount to the attribute price of a pants object
        # Args:
        # percentage (float): decimal representing the amount to discount
        return self.price * (1 - percentage)


class SalesPerson:
    # This class represents a sales employee of a store

    def __init__(self, first_name, last_name, employee_id, salary):
        # This is a method for initializing a SalesPerson object
        # Args/attributes:
        # below
        self.first_name = str(first_name)  # First name of employee in string form
        self.last_name = str(last_name)  # Last name of employee in string form
        self.employee_id = int(employee_id)  # ID number of employee in integer form
        self.salary = float(salary)  # Salary of the employee in float form
        self.pants_sold = []  # List of pants objects the employee sold
        self.total_sales = 0  # Total(sum) price of all pants objects sold

    def sell_pants(self, new_pants_sold):
        # sell_pants method appends a pants object to pants_sold attribute
        # Args:
        # new_pants_sold (object): a pants sold object created
        self.pants_sold.append(new_pants_sold)
        # appends the list with object passed through

    def display_sales(self):
        # Method to print out all pants that have been pants_sold
        # Args: None   Return: None

        for pants in self.pants_sold:
            print("Color: {}, size: {}, length: {}, price: {}".format(
                pants.color, pants.size, pants.length, pants.price))

    def calculate_sales(self):
        # Method to create a sum of the total price of all pants objects sold
        total = 0
        for pants in self.pants_sold:
            total += pants.price
        self.total_sales = total
        return total

    def calculate_commission(self, percentage):
        # Method to calculate comission of a sales person based on a percentage off
        # percentage of sales total
        # Args:
        # percentage (float): the comission to be paid in decimal form
        sales_total = self.calculate_sales()
        return sales_total * percentage


# Check results with this code
pants_one = Pants('red', 35, 36, 15.12)
pants_two = Pants('blue', 40, 38, 24.12)
pants_three = Pants('tan', 28, 30, 8.12)

salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
salesperson.sell_pants(pants_one)
salesperson.sell_pants(pants_two)
salesperson.sell_pants(pants_three)

salesperson.display_sales()
print(salesperson.calculate_commission(.15))
