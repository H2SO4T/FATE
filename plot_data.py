from utils.plotter import Plotter


def plot_all(names, csv_flag, sem_flag, stdev_flag, N, my_numbers, path, steps, type):
    for name in names:
        title = f'TD3 {name}'
        name_app = f'{name}_{type}'
        algo_list = [f'TD3_{name}_var{i}' for i in my_numbers]
        name_list = algo_list
        Plotter.plot_data(algo_list=algo_list, name_list=name_list, N=N, steps=steps, title=title, path=path,
                          stdev_flag=stdev_flag, p='br', sem_flag=sem_flag, csv_flag=csv_flag, name_app=name_app)
        title = f'SAC {name}'
        name_app = f'{name}_{type}'
        algo_list = [f'SAC_{name}_var{i}' for i in my_numbers]
        name_list = algo_list
        Plotter.plot_data(algo_list=algo_list, name_list=name_list, N=N, steps=steps, title=title, path=path,
                          stdev_flag=stdev_flag, p='br', sem_flag=sem_flag, csv_flag=csv_flag, name_app=name_app)
        title = f'DDPG {name}'
        name_app = f'{name}_{type}'
        algo_list = [f'DDPG_{name}_var{i}' for i in my_numbers]
        name_list = algo_list
        Plotter.plot_data(algo_list=algo_list, name_list=name_list, N=N, steps=steps, title=title, path=path,
                          stdev_flag=stdev_flag, p='br', sem_flag=sem_flag, csv_flag=csv_flag, name_app=name_app)


if __name__ == '__main__':
    # specify the names used before
    names = ['market_40', 'social_40', 'bank_40']
    csv_flag = True
    sem_flag = True
    stdev_flag = False
    # Define the number of runs to plot
    N = 20
    # How many variants of the algorithm to plot
    my_numbers = [k for k in range(8)]
    path = f'pickle_files'
    steps = 4000
    type = '40'
    plot_all(names, csv_flag, sem_flag, stdev_flag, N, my_numbers, path, steps, type)
