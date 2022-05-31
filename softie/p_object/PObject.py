import uuid as uuid

class PObject:
    
    def __init__(
        self, 
        pos: tuple, 
        mass: float, 
        vels: tuple = None, 
        ):

        self.mass = mass

        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.pos_z = pos[2]

        self.vx = vels[0] if vels else 0
        self.vy = vels[1] if vels else 0
        self.vz = vels[2] if vels else 0

        self.id = uuid.uuid4()

    @property
    def pos(self):
        return (self.pos_x, self.pos_y, self.pos_z)

    def _apply_force(self, forces: tuple):
        self.fx = forces[0]
        self.fy = forces[1]
        self.fz = forces[2]

    def _update_velocities(self, dt: float):
        self.vx = self.vx + (self.fx/self.mass)*dt
        self.vy = self.vy + (self.fy/self.mass)*dt
        self.vz = self.vz + (self.fz/self.mass)*dt

    def _update_position(self, dt: float):
        self.pos_x = self.pos_x + self.vx*dt
        self.pos_y = self.pos_y + self.vy*dt
        self.pos_z = self.pos_z + self.vz*dt

    def step_object(self, dt: float, force:tuple):

        self._apply_force(force)

        self._update_velocities(dt)
        self._update_position(dt)
        return self.pos