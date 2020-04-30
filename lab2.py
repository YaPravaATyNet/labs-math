import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt
import seaborn as sns
import random

mu = np.arange(0, 2.1, 0.1)
sigma = np.arange(0.5, 2.1, 0.1)
len_mu = len(mu)
len_sigma = len(sigma)
p_val_swap = np.zeros((len_mu, len_sigma))
power_swap = np.zeros((len_mu, len_sigma))
p_val_signs = np.zeros((len_mu, len_sigma))
power_signs = np.zeros((len_mu, len_sigma))
amount = 10000
n = 20


def signs(arr):
    cnt = 0
    for i in range(n):
        if arr[i] > 0:
            cnt += 1
    p = 0
    if abs(cnt / n - 0.5) > 0.05:
        p = 1
    return sp.binom(n, cnt) / (2 ** n), p

def swap(arr):
    sum = 0
    for i in range(n):
        sum += arr[i]
    cnt = 0
    power = 0
    for i in range(n):
        swap_sum = 0
        for j in range(n):
            if random.random() > 0.5:
                swap_sum += arr[i]
            else:
                swap_sum -= arr[i]
        if abs(swap_sum) >= abs(sum):
            cnt += 1 / n
        if abs(swap_sum - sum) > 0.05 * n:
            power += 1 / n
    return cnt, power


for i in range(len_mu):
    for j in range(len_sigma):
        for k in range(amount):
            normal = np.random.normal(mu[i], sigma[j], n)
            p_val, power = signs(normal)
            p_val_signs[i][j] += p_val
            power_signs[i][j] += power
            p_val1, power1 = swap(normal)
            p_val_swap[i][j] += p_val1
            power_swap[i][j] += power1

p_val_signs /= amount
power_signs /= amount
p_val_swap /= amount
power_swap /= amount

x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
y = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]

plt.figure(figsize=(20, 10))
ax = sns.heatmap(p_val_signs.transpose(), vmin=.0, vmax=1, annot=True, fmt='4.2f', linewidth=1, xticklabels=x, yticklabels=y, cmap='YlGn')
ax.set_title("Signs. P-value", fontsize=24)
ax.set_xlabel("Mu", fontsize=18)
ax.set_ylabel("Sigma", fontsize=18)
plt.show()
plt.figure(figsize=(20, 10))
ax = sns.heatmap(power_signs.transpose(), vmin=.0, vmax=1, annot=True, fmt='4.2f', linewidth=1, xticklabels=x, yticklabels=y, cmap='YlOrRd')
ax.set_title("Signs. Power", fontsize=24)
ax.set_xlabel("Mu", fontsize=18)
ax.set_ylabel("Sigma", fontsize=18)
plt.show()
plt.figure(figsize=(20, 10))
ax = sns.heatmap(p_val_swap.transpose(), vmin=.0, vmax=1, annot=True, fmt='4.2f', linewidth=1, xticklabels=x, yticklabels=y, cmap='YlGn')
ax.set_title("Swap. P-value", fontsize=24)
ax.set_xlabel("Mu", fontsize=18)
ax.set_ylabel("Sigma", fontsize=18)
plt.show()
plt.figure(figsize=(20, 10))
ax = sns.heatmap(power_swap.transpose(), vmin=.0, vmax=1, annot=True, fmt='4.2f', linewidth=1, xticklabels=x, yticklabels=y, cmap='YlOrRd')
ax.set_title("Swap. Power", fontsize=24)
ax.set_xlabel("Mu", fontsize=18)
ax.set_ylabel("Sigma", fontsize=18)
plt.show()