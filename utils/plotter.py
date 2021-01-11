import os
import pickle
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.colors as color
import statistics
from operator import sub, add, truediv
from sklearn import metrics
import csv

class Plotter:

    @staticmethod
    def variance(data):
        return [statistics.variance(i) for i in zip(*data)]

    @staticmethod
    def std_dev(data):
        return [statistics.stdev(i) for i in zip(*data)]

    @staticmethod
    def semean(data):
        return stats.sem(data, axis=0)

    @staticmethod
    def plot_data(algo_list, name_list, N, steps, title, path, stdev_flag, p, sem_flag, name_app, csv_flag):
        assert len(algo_list) == len(name_list)
        y_activities = []
        y_buttons = []
        for name in algo_list:
            for i in range(N):
                y_activities.append(Plotter.load_pickle(path + '/' + name + '_activities_'
                                                        + str(i) + '.pkl')[0:steps])
                # y_buttons.append(Plotter.load_pickle(path + '/' + name + '_buttons_'
                #                                     + str(i) + '.pkl')[0:steps])
        y_a = []
        y_b = []
        std_dev_a = []
        std_dev_b = []
        sem_a = []
        sem_b = []
        i = 0
        for j in range(len(algo_list)):
            y_a.append([sum(x) / N for x in zip(*y_activities[i:i + N])])
            # y_b.append([sum(x) / N for x in zip(*y_buttons[i:i + N])])
            if stdev_flag:
                std_dev_a.append(Plotter.std_dev(y_activities[i:i + N]))
                # std_dev_b.append(Plotter.std_dev(y_buttons[i:i + N]))
            if sem_flag:
                sem_a.append(Plotter.semean(y_activities[i:i + N]))
                # sem_b.append(Plotter.semean(y_buttons[i:i + N]))
            i += N

        if csv_flag:
            x = [i for i in range(4000)]
            check = os.path.isfile(f'csv/summary_{name_app}.csv')
            f = open(f'csv/summary_{name_app}.csv', 'a')
            if not check:
                # f.write('Algo, 1000, 2000, 3000, 4000, AUC 1000, AUC 2000, AUC 3000, AUC 4000 N\n')
                f.write('Algo, AUC 4000 N\n')
            for k in range(len(name_list)):
                f.write(f'{name_list[k]}, ' #{round(y_a[k][999], 2)}, {round(y_a[k][1999], 2)}, {round(y_a[k][2999], 2)},'
                        # f' {round(y_a[k][3999], 2)},'
                        # f'{round(metrics.auc(x[:999],y_a[k][:999]), 0)}, {round(metrics.auc(x[:1999],y_a[k][:1999]), 0)}, '
                        # f' {round(metrics.auc(x[:2999],y_a[k][:2999]), 0)}, {round(metrics.auc(x[:3999],y_a[k][:3999]), 0)}, '
                        f' {round(metrics.auc(x[:3999],y_a[k][:3999]), 0)}, '
                        f'{N}\n')

        Plotter.matplot(y_a, name_list, stdev=std_dev_a, sem=sem_a, title=f'Activities Coverage {title}', stdev_flag=stdev_flag,
                        p=p, sem_flag=sem_flag)
        # Plotter.matplot(y_b, name_list, stdev=std_dev_b, sem=sem_b, title=f'Buttons Coverage {title}', stdev_flag=stdev_flag,
        # p=p, sem_flag=sem_flag)


    @staticmethod
    def matplot(y, y_labels, stdev, sem, title, stdev_flag, p, sem_flag):
        colors = list(color.BASE_COLORS.keys())
        colors[7] = 'orange'
        fig, ax = plt.subplots()
        for i in range(len(y)):
            ax.plot(y[i], colors[i], label=y_labels[i])
            if stdev_flag:
                e_sup = list(map(add, y[i], stdev[i]))
                e_inf = list(map(sub, y[i], stdev[i]))
                for j in range(4000):
                    if e_inf[j] < 0:
                        e_inf[j] = 0
                ax.fill_between(x=[i for i in range(0, 4000)], y1=e_sup, y2=e_inf, alpha=0.3, edgecolor='grey',
                                facecolor=colors[i], linewidth=1, linestyle='dotted')
            if sem_flag:
                sem_sup = list(map(add, y[i], sem[i]))
                sem_inf = list(map(sub, y[i], sem[i]))
                for j in range(4000):
                    if sem_inf[j] < 0:
                        sem_inf[j] = 0
                ax.fill_between(x=[i for i in range(0, 4000)], y1=sem_sup, y2=sem_inf, alpha=0.3, edgecolor='grey',
                                facecolor=colors[i], linewidth=1, linestyle='dotted')
        ax.set(xlabel='simulation Steps', title=title)

        if p == 'ul':
            ax.legend(loc='upper left')
        elif p == 'ur':
            ax.legend(loc='upper right')
        elif p == 'bl':
            ax.legend(loc='lower left')
        elif p == 'br':
            ax.legend(loc='lower right')
        ax.grid()
        fig.savefig('figs/' + title + '.png', format='png', dpi=120)

    @staticmethod
    def load_pickle(path):
        return pickle.load(open(path, 'rb'))
