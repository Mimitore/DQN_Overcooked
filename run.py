from OvercookedEnv import OvercookedEnv
from DQNAgent import DQNAgent

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

    return total_reward

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

for episode in range(num_episodes):
    total_reward = run_episode(env, agent, epsilon)
    print(f"Episode {episode}: Total Reward: {total_reward}")
    epsilon = max(epsilon * epsilon_decay, epsilon_min)
    if episode % 10 == 0:
        update_target_model(agent.model, agent.target_model)


