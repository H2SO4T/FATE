import gym
import numpy as np
from activity import Activity

def preprocess_graph(graph):
    global_vars = {}
    for var in graph['global_vars']:
        global_vars.update({var['name']: var['value']})
    new_graph = {}
    for node in graph['nodes']:
        new_graph.update({node['node_id']: Activity(node['node_id'], node['transitions'])})
    return global_vars, new_graph


class Graph(gym.Env):

    def __init__(self, graph, max_timesteps, discovered_activities, clicked_buttons, strings):

        self.global_vars, self.explorable_graph = preprocess_graph(graph)
        self.backup_graph = dict(self.explorable_graph)
        self.backup_vars = dict(self.global_vars)
        ######
        self.init_activity = list(self.explorable_graph.keys())[0]
        self.set_activities_episode = {self.init_activity}
        self.max_timesteps = max_timesteps
        self.timesteps = 0
        ######
        assert type(discovered_activities) == list
        self.discovered_activities_set = {self.init_activity}
        self.discovered_activities_list = discovered_activities
        assert type(clicked_buttons) == list
        self.clicked_buttons_set = set()
        self.clicked_buttons_list = clicked_buttons
        ######
        self.ACTION_SPACE = 0
        self.activity_space = 0
        self.widget_space = 0
        self.STRINGS = strings
        for key in self.explorable_graph.keys():
            self.activity_space += 1
            dim = self.explorable_graph[key].return_widget_len()
            self.widget_space += dim
            if dim > self.ACTION_SPACE:
                self.ACTION_SPACE = dim

        self.observation = np.array([0] * (self.activity_space + self.widget_space))
        self.current_activity = self.past_activity = self.init_activity
        self.action_space = gym.spaces.Box(low=np.array([0, 0]),
                                           high=np.array([self.ACTION_SPACE, self.STRINGS]),
                                           dtype=np.int64)
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(self.activity_space + self.widget_space,),
                                                dtype=np.int32)
        self.update_action_space()

    def reset(self):
        self.timesteps = 0
        self.current_activity = self.past_activity = self.init_activity
        self.set_activities_episode = {self.init_activity}
        self.explorable_graph = dict(self.backup_graph)
        self.global_vars = self.backup_vars
        self.update_action_space()
        observation = self.compute_observation()
        return observation

    def step(self, action):
        action = action.astype(int)
        if action[0] >= self.get_action_space()[0]:
            self.update_tracker()
            return self.observation, np.array([-30.0]), np.array(False), {}
        else:
            new_activity = self.perform_action(action)
            if new_activity != self.current_activity:
                self.past_activity = self.current_activity
                self.current_activity = new_activity
            self.update_action_space()
            self.update_tracker(action)
            observation = self.compute_observation()
            reward = self.compute_reward()
            self.timesteps += 1
            done = self._termination()
            return self.observation, np.array([reward]), np.array(done), {}

    def perform_action(self, action):
        # I have the corresponding button
        transition = self.explorable_graph[self.current_activity].map[action[0]]
        if self.evaluate_guard(transition):
            self.evaluate_set(transition, action)
            return transition.destination
        else:
            return self.current_activity

    def compute_observation(self):
        observation = [0] * (self.activity_space + self.widget_space)
        observation[list(self.explorable_graph.keys()).index(self.current_activity)] = 1
        position = self.activity_space
        for key in self.explorable_graph.keys():
            if key == self.current_activity:
                dim = self.explorable_graph[key].return_widget_len()
                observation[position:position + dim] = [1] * dim
            else:
                position += self.explorable_graph[key].return_widget_len()
        self.observation = np.array(observation)
        return self.observation

    def compute_reward(self):
        if self.past_activity != self.current_activity:
            if self.current_activity not in self.set_activities_episode:
                self.set_activities_episode.add(self.current_activity)
                return 1000.0
            else:
                return 0.0
        # self.past_activity == self.current_activity
        else:
            return -1.0

    def update_action_space(self):
        self.action_space.high[0] = self.explorable_graph[self.current_activity].return_widget_len()

    def _termination(self):
        if self.timesteps == self.max_timesteps:
            return True
        else:
            return False

    def update_tracker(self, action=None):
        if action is not None:
            self.discovered_activities_set.add(self.current_activity)
            self.clicked_buttons_set.add(self.past_activity + str(action[0]))
            self.discovered_activities_list.append(len(self.discovered_activities_set))
            self.clicked_buttons_list.append(len(self.clicked_buttons_set))
        else:
            self.discovered_activities_list.append(len(self.discovered_activities_set))
            self.clicked_buttons_list.append(len(self.clicked_buttons_set))

    def get_action_space(self):
        return self.action_space.high

    def evaluate_guard(self, transition):
        if transition.guard is not None:
            return eval(transition.guard, {'__builtins__': None}, self.global_vars)
        else:
            return True

    def evaluate_set(self, transition, action):
        if transition.set is not None:
            if 'input_text' in transition.set:
                input_text = transition.strings[action[1]]
                exec(transition.set, {'input_text': input_text}, self.global_vars)
            else:
                exec(transition.set, {'__builtins__': None}, self.global_vars)
