import matplotlib.pyplot as plt


class UHistory:
    def __init__(self, owner):
        self.owner = owner

    def SaveHistory(self):
        pass

    @staticmethod
    def BuildGraphFromVariable(draw_var, name = "Y"):
        t = range(len(draw_var))
        plt.plot(t, draw_var, marker='o', linestyle='-')
        plt.xlabel("Days")
        plt.ylabel(name)
        plt.show()
