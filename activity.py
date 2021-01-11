from widget import Widget

class Activity:
    def __init__(self, node_name, widget_list):
        # State Definition
        self.number_visits = 0
        self.node_name = node_name
        self.map = {}
        for widget in widget_list:
            self.map.update({widget['transition_id']: Widget(father=self.node_name, transition=widget)})
        self.num_widgets = len(self.map.keys())

    def return_widget(self, widget_name):
        return self.map[widget_name]

    def return_widget_len(self):
        return self.num_widgets
