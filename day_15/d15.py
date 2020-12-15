from tqdm import tqdm
import matplotlib.pyplot as plt

def get_last_two_indices(spoken, current):
    indces = []
    for i, j in enumerate(spoken[::-1]):
        if j == current:
            indces.append(len(spoken) - i)
            if len(indces) == 2:
                return indces
    return "Fuck"

if __name__ == '__main__':
    spoken = [5,1,9,18,13,8,0]

    n = 2020

    for i in tqdm(range((len(spoken)), n)):
        if spoken[i-1] not in spoken[:-1]:
            spoken.append(0)
        else:
            indices = get_last_two_indices(spoken, spoken[i-1])
            spoken.append(indices[0] - indices[1])

    print(spoken)
    print(spoken[-1])
    plt.plot(spoken)
    plt.show()

