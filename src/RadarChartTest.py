import matplotlib.pyplot as plt
import numpy as np

labels = ['SKill 1', 'Skill 2', 'Skill 3','Skill 4', 'Skill5']

markers = [0, 1, 2, 3, 4, 5]


def make_radar_chart(name, points, attribute_labels):
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    stats = np.concatenate((points, [points[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    attribute_labels.append(attribute_labels[0])

    fig = plt.figure()
    ax = fig.add_subplot(polar=True)

    ax.plot(angles, stats, 'o--', linewidth=2, label='Level')
    ax.fill(angles, stats, alpha=0.25)
    ax.set_thetagrids(angles * 180 / np.pi, attribute_labels)

    ax.set_title(name)
    plt.yticks(markers)
    ax.grid(True)
    plt.legend()
    plt.tight_layout()
    
    return plt.show()


make_radar_chart("Bob", [1, 4, 2, 3, 5], labels)
