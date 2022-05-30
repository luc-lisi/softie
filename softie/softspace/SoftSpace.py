from ..softobject.SoftObject import SoftObject
from typing import List

class SoftSpace:

    def __init__(
        self, 
        dimensions: tuple, 
        children: List[SoftObject] = None):

        self.children = children if children else []

        self.x = dimensions[0]
        self.y = dimensions[1]
        self.z = dimensions[2]

    def add_child(self, child: SoftObject):
        self.children.append(child)
