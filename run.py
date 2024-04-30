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

num_episodes = 1000
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



# Initialiser un dictionnaire pour stocker les listes des occurrences de chaque action
action_data = {}

# Parcourir chaque dictionnaire d'occurrences dans la liste
for episode_dict in actions:
    for action, count in episode_dict.items():
        if action in action_data:
            action_data[action].append(count)
        else:
            action_data[action] = [count]

plt.figure(figsize=(12, 8))

# Tracer une courbe pour chaque action
for action, occurrences in action_data.items():
    plt.plot(list(range(1, num_episodes + 1)), occurrences, label=action) 

# Ajouter des titres et des labels
plt.title('Action Occurrences Over Episodes')
plt.xlabel('Episode')
plt.ylabel('Occurrences')
plt.legend(title='Actions')
# Afficher une grille
plt.grid(True)
# Afficher le graphique
plt.show()



# Initialiser un dictionnaire pour stocker les listes des occurrences de chaque action
result_data = {}

# Parcourir chaque dictionnaire d'occurrences dans la liste
for episode_dict in results:
    for result, count in episode_dict.items():
        if result in result_data:
            result_data[result].append(count)
        else:
            result_data[result] = [count]

plt.figure(figsize=(12, 8))

print(result_data)
# Tracer une courbe pour chaque action
for result, occurrences in result_data.items():
    plt.plot(list(range(1, num_episodes + 1)), occurrences, label=result) 

# Ajouter des titres et des labels
plt.title('Result Occurrences Over Episodes')
plt.xlabel('Episode')
plt.ylabel('Occurrences')
plt.legend(title='Results')
# Afficher une grille
plt.grid(True)
# Afficher le graphique
plt.show()


torch.save(agent.model.state_dict(), 'dqn_model.pth')
