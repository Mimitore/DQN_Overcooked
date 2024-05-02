from OvercookedEnv import OvercookedEnv
from DQNAgent import DQNAgent
import torch
import matplotlib.pyplot as plt

def run_episode(env, agent, epsilon):
    state = env.reset()
    total_reward = 0
    done = False

    while not done:
        action = agent.select_action(state, epsilon)
        next_state, reward, done = env.step(action)
        agent.memory.push(state, action, reward, next_state, done)
        state = next_state
        total_reward += reward
        agent.train(64)
    
    return env.map.score.score,total_reward

def update_target_model(main_model, target_model):
    target_model.load_state_dict(main_model.state_dict())

env = OvercookedEnv()
state_dim = env.state_dim 
action_dim = env.action_space.n 
agent = DQNAgent(state_dim, action_dim)

num_episodes = 4000
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01

rewards = []
scores = []
actions = []
results = []
for episode in range(num_episodes):
    score,total_reward = run_episode(env, agent, epsilon)
    print(f"Episode {episode}: Total Reward: {total_reward} , Score : {score}, action : {env.actions_occ}, result : {env.results_occ}")
    rewards.append(total_reward)
    scores.append(score)
    actions.append(env.actions_occ.copy())
    results.append(env.results_occ.copy())
    epsilon = max(epsilon * epsilon_decay, epsilon_min)
    if episode % 10 == 0:
        update_target_model(agent.model, agent.target_model)

# Tracé des récompenses en fonction des épisodes
plt.figure(figsize=(10, 5))  # Taille de la figure
plt.plot(rewards, label='Rewards per Episode')
plt.title('Rewards Trend over Episodes')  # Titre du graphique
plt.xlabel('Episodes')  # Axe des x
plt.ylabel('Total Reward')  # Axe des y
plt.legend()  # Ajouter une légende
plt.grid(True)  # Afficher une grille pour mieux visualiser les lignes
plt.show()  # Afficher le graphique


# Nombre d'épisodes par groupe pour l'agrégation
interval = 100

# Initialiser un dictionnaire pour stocker les données agrégées
aggregated_data = {}

for action in actions[0].keys():
    aggregated_data[action] = []

# Agréger les données
for i in range(0, num_episodes, interval):
    temp_data = {action: 0 for action in actions[0].keys()}
    for j in range(i, min(i + interval, num_episodes)):
        for action in actions[j]:
            temp_data[action] += actions[j][action]
    
    for action in temp_data:
        aggregated_data[action].append(temp_data[action] / interval)  # Moyenne des occurrences par intervalle

# Tracer les données agrégées
plt.figure(figsize=(10, 5))
for action, data in aggregated_data.items():
    plt.plot(range(0, num_episodes, interval), data, label=action)

plt.xlabel('Episode')
plt.ylabel('Average Occurrences')
plt.title('Action Occurrences per Interval')
plt.legend()
plt.grid(True)
plt.show()



result_data = {}
important_result = ['cut', 'toplate', 'tocookware', 'serv']

for action in important_result:
    result_data[action] = [0] * ((num_episodes + interval - 1) // interval) 

for i, episode_dict in enumerate(results):
    index = i // interval 
    for result, count in episode_dict.items():
        if result in important_result:
            result_data[result][index] += count  

for result in important_result:
    for i in range(len(result_data[result])):
        result_data[result][i] /= interval  # Moyenner les occurrences sur l'intervalle

plt.figure(figsize=(12, 8))
x_values = list(range(0, num_episodes, interval))
for result, occurrences in result_data.items():
    plt.plot(x_values, occurrences, label=result)

# Ajouter des titres et des labels
plt.title('Result Occurrences Over Intervals of Episodes')
plt.xlabel('Episode')
plt.ylabel('Average Occurrences')
plt.legend(title='Results')
plt.grid(True)

# Afficher le graphique
plt.show()


torch.save(agent.model.state_dict(), 'dqn_model.pth')
