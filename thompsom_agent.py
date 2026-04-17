import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import beta

def reward_plot(success_array, failure_array):
    linestyle = ['-', '--']
    x = np.linspace(0, 1, 1002)[1:-1]

    plt.clf()
    plt.xlim(0, 1)
    plt.ylim(0, 30)

    for a, b, ls in zip(success_array, failure_array, linestyle):
        dist = beta(a,b)
        
        plt.plot(x, dist.pdf(x), ls=ls, c='black', label='Alpha:{}, Beta{}'.format(a,b))

        plt.draw()
        plt.pause(0.01)




class ThompsonAgent(object):
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

eps_init = 1
decay = 0.005
threshold = 0.15

# decay values of eps
eps_array = [(eps_init*(1-decay))**i for i in range (trials)]

# agente
bandit = ThompsonAgent(prob_list)

prob_reward_array = np.zeros(len(prob_list))
accumulated_reward_array = []
avg_accumulated_reward_array = []

for episode in range(episodes):

    success_array = np.ones(len(prob_list))
    failure_array = np.full(len(prob_list), 1.0e-5)

    reward_array = np.zeros(len(prob_list))
    bandit_array = np.full(len(prob_list), 1.0e-5)
    accumulated_reward = 0

    for trial in range(trials):
        # agent - escolha
        prob_reward = np.random.beta(success_array, failure_array)
        bandit_machine = np.argmax(prob_reward)

        # agent - recompensa
        reward = bandit.pull(bandit_machine)

        if reward == 1:
            success_array[bandit_machine] += 1
        else:
            failure_array[bandit_machine] += 1


        #plot
        reward_plot(success_array, failure_array)

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