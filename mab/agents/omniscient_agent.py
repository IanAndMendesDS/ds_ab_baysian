import numpy as np


class OmniscientAgent(object):
    def __init__(self,prob_list):
        self.prob_list = prob_list

    def pull(self, bandit_machine):
        if np.random.random() < self.prob_list[bandit_machine]:
            reward = 1
        else:
            reward = 0
        return reward

# probabilidade de ter resultado positivo da pagina
prob_list = [0.25, 0.30]

# parametros do experimento
trials = 1000
episodes = 200
# agente
bandit = OmniscientAgent(prob_list)

prob_reward_array = np.zeros(len(prob_list))
accumulated_reward_array = []
avg_accumulated_reward_array = []

for episode in range(episodes):

    reward_array = np.zeros(len(prob_list))
    bandit_array = np.full(len(prob_list), 1.0e-5)
    accumulated_reward = 0

    for trial in range(trials):
        # agent - escolha
        bandit_machine = np.argmax(prob_list)

        # agent - recompensa
        reward = bandit.pull(bandit_machine)

        # agent - guarda recompensa
        reward_array[bandit_machine] += reward
        bandit_array[bandit_machine] += 1
        accumulated_reward += reward

    prob_reward_array += reward_array / bandit_array
    accumulated_reward_array.append(accumulated_reward)
    avg_accumulated_reward_array.append(np.mean(accumulated_reward_array))

prob01 = 100*np.round(prob_reward_array[0]/ episodes , 2)
prob02 = 100*np.round(prob_reward_array[1]/ episodes , 2)

print('\n Probabilidade da Maquina(Bandit 01): {}% - Probabilidade da Maquina(Bandit 02): {}%'.format(prob01, prob02))
print('\n Avg accumulated reward: {}'.format(np.mean(avg_accumulated_reward_array)))