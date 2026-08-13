#!/usr/bin/python3
"""Square module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes."""
        attrs = ["id", "size", "x", "y"]
        if args:
            for i, v in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Return dictionary representation."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
