import pickle
import logging
import time
import warnings
import os

warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
logging.getLogger('tensorflow').setLevel(logging.FATAL)
import Graph as graph
from stable_baselines.sac.policies import MlpPolicy
from stable_baselines import SAC
import os
import multiprocessing

# Here you need to define the graph of your app
from graphs.bank import bank as test

# Define the name
name_graph = 'bank'
# Define the testing time steps
timesteps = 4000
# Define the number of runs
N = 10
# Define the number of strings to use
strings = 20


def train(args):
    variant, target_update_interval, train_freq = args[0], args[1], args[2]
    graphs = [dict(test)]
    name = [name_graph]
    ep_len = 300
    for j in range(len(graphs)):
        for i in range(N):
            discovered_activities = []
            clicked_buttons = []
            env = graph.Graph(graphs[j], ep_len, discovered_activities, clicked_buttons, strings=strings)
            model = SAC(MlpPolicy, env, verbose=1, train_freq=train_freq, target_update_interval=target_update_interval,
                        learning_rate=0.001)
            model.learn(total_timesteps=timesteps)
            pickle.dump(discovered_activities, open('pickle_files{}'.format(os.sep) + 'SAC_' + name[j] + '_var'
                                                    + str(variant) + '_activities_' + str(i) + '.pkl', 'wb'))
            pickle.dump(clicked_buttons, open('pickle_files{}'.format(os.sep) + 'SAC_' + name[j] + '_var'
                                              + str(variant) + '_buttons_' + str(i) + '.pkl', 'wb'))


def main():
    pool = multiprocessing.Pool(6)
    # Define the parameters that you want to test here
    pool.map(train, [(0, 1, 1), (1, 1, 5), (2, 2, 1), (3, 2, 5), (4, 5, 1), (5, 5, 5), (6, 10, 1),
                     (7, 10, 5)])


if __name__ == '__main__':
    main()
