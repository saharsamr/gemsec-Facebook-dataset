import matplotlib.pyplot as plt
import graph_tool.all as gt


class Plots:

    @staticmethod
    def degree_distribution(degrees, freq, title):

        p_degree = [f/sum(freq) for f in freq]

        fig, axs = plt.subplots(1, 2)
        fig.suptitle(title)

        axs[0].set_title("normal scale")
        axs[0].plot(degrees, p_degree, '.', markersize=2, c='c')

        axs[1].set_title("log scale")
        axs[1].set_yscale("log")
        axs[1].plot(degrees, p_degree, '.', markersize=2, c='c')

        for ax in axs.flat:
            ax.set(xlabel='degree', ylabel='P(degree)')

        fig.tight_layout()

    @staticmethod
    def degree_correlation_hist(hist, x_range=None, y_range=None):

        if x_range:
            plt.xlim(*x_range)
        if y_range:
            plt.ylim(*y_range)

        plt.xlabel('degree')
        plt.ylabel('degree')
        plt.imshow(hist.T, origin="lower")
        plt.colorbar()

    @staticmethod
    def plot_frequency(x, freq, x_label=None, y_label=None):

        plt.plot(x, freq, '.', markersize=2, c='c')
        plt.xlabel(x_label)
        plt.ylabel(y_label)

    @staticmethod
    def pie_plots(fracs, labels, colors=None, explode=None):

        plt.pie(fracs, labels=labels, autopct='%1.1f%%', colors=colors, explode=explode, pctdistance=0.82,
                textprops={'size': 'smaller'})
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.axis('equal')
        plt.tight_layout()
