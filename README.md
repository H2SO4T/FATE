# FATE# FATE
Deep RL algorithms require fine tuning, which is expensive on real apps. Therefore, we developed FATE, 
a simulation environment for fast Android testing. FATE models only the navigation constraints of Android apps, 
so it can be used to efficiently compare alternative testing algorithms and to quickly tune their corresponding 
hyperparameters.

# Requirements

* Ptolemy: https://ptolemy.berkeley.edu
* python 3.5 to 3.7 (tensorflow limitation)

# Modelling an Android App

In the folder `ptolemy` you can find an example of app. Following the pattern of  bank.xml you can define your own app.
Once finished you can launch the script : ``python3 ptolemy_to_fate.py -n 'path_to_xml'``.
As output, you will have a python file named as your original xml file. Please check the `global_vars` inside the 
python file.
Once done use you modelled application in ``train_TD3.py, train_SAC.py, train_DDPG.py``.


