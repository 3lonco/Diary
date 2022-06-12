import matplotlib.pyplot as plt
import matplotlib.animation as anm


class World:
    def __init__(self, time_span, time_interval, debug=True):
        self.objects = []
        self.debug = debug
        self.time_span = time_span
        self.time_interval = time_interval

    def append(self, obj):
        self.objects.append(obj)

    def draw(self):
        fig = plt.figure(figsize=(4, 4))
        ax = fig.add_subplot(111)
        ax.set_aspect("equal")
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_xlabel("X", fontsize=20)
        ax.set_ylabel("Y", fontsize=20)

        elems = []
        if self.debug:
            for i in range(1000):
                self.one_step(i, elems, ax)
        else:
            self.ani = anm.FuncAnimation(
                fig,
                self.one_step,
                fargs=(elems, ax),
                frames=int(self.time_span / self.time_interval) + 1,
                interval=int(self.time_interval * 1000),
                repeat=False,
            )
            plt.show()

    def one_step(self, i, elems, ax):
        while elems:
            elems.pop().remove()
        time_str = "t=%.2f[s]" % (self.time_interval * i)
        elems.append(ax.text(-4.4, 4.5, time_str, fontsize=10))
        for obj in self.objects:
            obj.draw(ax, elems)
            if hasattr(obj, "one_step"):
                obj.one_step(1.0)
