# Create class
class MaxSizeList(object):

    # Initialize with data to pass as the maximum list size and set a starting empty list
    def __init__(self, max):
        self.max_size = max  # Pass through maximum size of list with max_size
        self.initial_list = []  # Make intial list empty

    # Create a method for adding to the list called push and remove anything longer than max list size passed through
    def push(self, obj):
        self.initial_list.append(obj)
        # Set loop to iterate through list until conditions are met
        if len(self.initial_list) > self.max_size:  # If the list is greater than max list do next step
            self.initial_list.pop(0)  # Delete first item off list

    # Create a method to get the instance list
    def get_list(self):
        return self.initial_list
