"""
When we try to iterate an object, Python will call the iter() function over it. One of the
first things this function checks for is the presence of the __iter__ method on that object,
which, if present, will be executed.
"""
from datetime import timedelta, date

class DateRangeIterable:
    """An iterable that contains its own iterator object."""
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today

for day in DateRangeIterable(date(2021, 6, 1), date(2021, 6, 18)):
    print(day)

"""
Here the for loop is starting a new iteration over our object.At this point, Python will call
the iter() function on it, which in turn will call the __iter__ magic method.On this method,
it is defined to return self, indicating that the object is an iterable itself, so at that 
point every step of the loop will call the next() function on that object, which delegates to
the __next__ method. In this method, we decide how to produce the elements and return one at time.
When there is nothing else to produce, we have to signal this to Python by raising the StopIteration
exception.
"""