from softie.p_space.PSpace import PSpace
from softie.p_object.PObject import PObject
from softie.p_system.PSystem import PSystem


my_particles = [
    PObject(
        (0, 0, 0), 
        5, 
        (2, 0, 0), 
    ),
    PObject(
        (1, 0, -1),
        5, 
        (0, 0, 0), 
    )
]

my_space = PSpace(
    (10,10,10),
    my_particles
)

my_system = PSystem(
    my_space,
    0.1,
    1
)

my_system.start()

