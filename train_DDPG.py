import pickle
import warnings
import os
import logging



warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
logging.getLogger('tensorflow').setLevel(logging.FATAL)
import Graph as graph
from stable_baselines import DDPG
from stable_baselines.ddpg.policies import MlpPolicy
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
    variant, random_exploration, nb_train_steps = args[0], args[1], args[2]
    graphs = [dict(test)]
    name = [name_graph]
    ep_len = 300
    for j in range(len(graphs)):
        for i in range(N):
            print('train number: ' + str(i))
            discovered_activities = []
            clicked_buttons = []
            env = graph.Graph(graphs[j], ep_len, discovered_activities, clicked_buttons, strings=strings)
            model = DDPG(MlpPolicy, env, random_exploration=0.8, nb_train_steps=25)
            model.learn(total_timesteps=timesteps)
            pickle.dump(discovered_activities, open(
                'pickle_files{}'.format(os.sep) + 'DDPG_' + name[j] + '_var' + str(variant) + '_activities_' + str(i)
                + '.pkl', 'wb'))
            pickle.dump(clicked_buttons, open(
                'pickle_files{}'.format(os.sep) + 'DDPG_' + name[j] + '_var' + str(variant) + '_buttons_' + str(i)
                + '.pkl', 'wb'))


if __name__ == '__main__':
    pool = multiprocessing.Pool(5)
    pool.map(train, [
        # Define the parameters that you want to test here
        (0, 0.5, 5), (1, 0.5, 25), (2, 0.6, 25), (3, 0.6, 100), (4, 0.7, 25), (5, 0.7, 10), (6, 0.8, 10), (7, 0.8, 25)
    ])
