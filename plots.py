import matplotlib.pyplot as plt


class Plots:

    @staticmethod
    def degree_distribution(x, y, title):

        fig, axs = plt.subplots(1, 2)
        fig.suptitle(title)

        axs[0].set_title("normal scale")
        axs[0].plot(x, y, '.', markersize=2)

        axs[1].set_title("log scale")
        axs[1].set_xscale("log")
        axs[1].set_yscale("log")
        axs[1].plot(x, y, '.', markersize=2)

        for ax in axs.flat:
            ax.set(xlabel='degree', ylabel='node count')
