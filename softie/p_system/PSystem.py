from ..p_space.PSpace import PSpace
import csv 

class PSystem:
    def __init__(self, space: PSpace, dt: float, sim_duration: float):
        
        self.dt = dt
        self.space = space

        self.sim_duration = sim_duration

        self.time_elapsed = 0

    def start(self):

        logging_status = True

        if logging_status:
            with open('sim_log.csv', 'w', newline='') as csvfile:
                wr = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                wr.writerow(['id', 'pos_x', 'pos_y', 'pos_z', 'time_elapsed'])

        while self.time_elapsed < self.sim_duration:
            self.space.step_children(self.dt)
            self.space.write_positions(self.time_elapsed)
            self.time_elapsed += self.dt

        self.stop()

    def pause(self):
        pass

    def stop(self):
        print(f"Simulation copmelte after {self.time_elapsed}s. \n Exiting Siimulation. :)")
        exit(1)

    @classmethod
    def plot_simulation():
        pass