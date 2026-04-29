    # This class is an iterator that generates powers of three.
class PowerOfThree:
    # The __iter__ method is called when an iterator is initialized. 
    # For eg. when we use a for loop to iterate over an instance of PowerOfThree, 
    # the __iter__ method is called to set up the iterator.
    # It sets the initial value to 1 and returns the iterator object itself.
    # The __iter__ method initializes the value to 1 and returns the iterator object itself.
    # This allows the object to be used in a for loop or any other context that requires an iterator.
    def __iter__(self):
        self._value = 1
        return self
    
    # The __next__ method is called to get the next item in the iteration.
    # The __next__ method returns the current value and then updates it to the next power of three.
    # If the value exceeds a certain limit (e.g., 500), it raises a StopIteration exception to signal that there are no more items to iterate over.
    def __next__(self):
        if self._value > 500:
            raise StopIteration
        current_value = self._value
        self._value *= 3
        return current_value
    
for i in PowerOfThree():
    print(i)