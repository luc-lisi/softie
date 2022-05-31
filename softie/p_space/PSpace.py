from ..p_object.PObject import PObject
from typing import List

import csv

class PSpace:

    def __init__(
        self, 
        dimensions: tuple, 
        children: List[PObject] = None,
        force_list: list = None):

        self.children = children if children else []

        self.size_x = dimensions[0]
        self.size_y = dimensions[1]
        self.size_z = dimensions[2]

        self.force_list = force_list if force_list else []

        self.child_positions = { child.id: child.pos for child in children}

    def add_child(self, child: PObject):
        self.children.append(child)

    def _update_child_positions(self, child):
        self.child_positions[child.id] = child.pos

    def _calculate_child_forces(self, child: PObject):
        
        current_force = (0, 0, 0)

        this_id = child.id
        this_pos = child.pos

        for other_child in self.children:
            if other_child.id == this_id:
                continue
            
            else:
                other_pos = self.child_positions[other_child.id]
                distance = (
                    this_pos[0]-other_pos[0],
                    this_pos[1]-other_pos[1],
                    this_pos[2]-other_pos[2],
                    )
                
                for force in self.force_list:
                    current_force = (
                        current_force[0] + force(distance[0]), 
                        current_force[1] + force(distance[1]), 
                        current_force[2] + force(distance[2])
                    )

        return current_force

    def write_positions(self, time_elapsed):
        with open('sim_log.csv', 'a', newline='') as csvfile:
            wr = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for child in self.children:
                wr.writerow([child.id, child.pos_x, child.pos_y, child.pos_z, time_elapsed])

    def step_children(self, dt: float):

        for child in self.children:
            child_force = self._calculate_child_forces(child)
            child.step_object(dt, child_force)
            self._update_child_positions(child)
            print(f"Object {child.id} at: {child.pos}")
