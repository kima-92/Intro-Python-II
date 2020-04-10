
class Item:
    """ This will be the base class for specialized item types to be declared later """

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        
        description = f"""
    >>> {self.name}
    {self.description}
    """

        return description