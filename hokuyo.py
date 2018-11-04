import numpy as np
import matplotlib.pyplot as plt
from hokuyolx import HokuyoLX


def cleanLidar(readings, mask):
    arange = np.arange(len(readings))
    x = arange[mask]
    xp = arange[~mask]
    fp = readings[~mask]
    readings[mask] = np.interp(x, xp, fp)
    return readings


class Hokuyo(object):

    def __init__(self):
        self.laser = HokuyoLX()
        angles = self.laser.get_angles()
        self.cos = np.cos(angles)
        self.sin = np.sin(-angles)

    def xy(self, filter=False, interpolate=False):
        if not filter:
            scan = self.laser.get_dist()[1]
            scan = scan * .001
            x = self.sin * scan
            y = self.cos * scan
            return x, y

        if interpolate:
            scan = self.scene * .001
            x = self.sin * scan
            y = self.cos * scan
            return x, y

        else:
            scan = self.laser.get_dist()[1]
            valid = np.logical_and(21 <= scan, scan <= 30000)
            scan = scan * .001
            x = self.sin * scan
            y = self.cos * scan
            return x[valid], y[valid]

    @property
    def scene(self):
        scan = self.laser.get_dist()[1]
        invalid = np.logical_or(21 > scan, scan > 30000)
        return cleanLidar(scan, invalid)

    def live_plot(self, interpolate=False):
        import matplotlib.animation as anim
        fig = plt.figure()
        ax = fig.add_subplot(111)
        x, y = self.xy(interpolate)
        graph = ax.plot(x, y, linestyle="", marker=".")[0]
        plt.gca().set_aspect('equal', adjustable='box')

        def update_graph(*args):
            x, y = self.xy(interpolate)
            graph.set_data(x, y)

        do_not_remove = anim.FuncAnimation(fig, update_graph, None,
                                           interval=100, blit=False)
        plt.show()


if __name__ == "__main__":
    laser = Hokuyo()
    laser.live_plot(True, True)
