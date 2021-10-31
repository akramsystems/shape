import matplotlib.pyplot as plt

class ScatterPlot:
    def __init__(self):
        self.fig = plt.figure(figsize=(8,8))
        self.ax = self.fig.add_subplot(111, title="Misquito Distance Travelled")
    def addPoint(self, x:int, y:int):
        self.ax.scatter([x],[y], s=10000, alpha=0.1)
    def display(self):
        plt.show()
