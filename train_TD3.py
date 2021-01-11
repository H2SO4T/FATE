import pickle
import warnings
import os
import logging
warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
logging.getLogger('tensorflow').setLevel(logging.FATAL)
import Graph as graph
from stable_baselines import TD3
from stable_baselines.td3.policies import MlpPolicy
import os
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
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
    variant, train_freq = args[0], args[1]
    graphs = [dict(test)]
    name = [name_graph]
    ep_len = 300
    for j in range(len(graphs)):
        for i in range(N):
            print('train number: ' + str(i))
            discovered_activities = []
            clicked_buttons = []
            env = graph.Graph(graphs[j], ep_len, discovered_activities, clicked_buttons, strings=strings)
            # Here you can pass the parameters that you want to test
            model = TD3(MlpPolicy, env, train_freq=train_freq, learning_starts=0)
            model.learn(total_timesteps=timesteps)
            pickle.dump(discovered_activities, open(
                f'pickle_files{os.sep}TD3_{name[j]}_var{variant}_activities_{i}.pkl', 'wb'))
            pickle.dump(clicked_buttons, open(
                f'pickle_files{os.sep}TD3_{name[j]}_var{variant}_buttons_{i}.pkl', 'wb'))


if __name__ == '__main__':
    pool = multiprocessing.Pool(4)
    # Define the parameters that you want to test here
    pool.map(train, [
        (0, 5), (1, 10), (2, 20), (3, 100)
    ])
