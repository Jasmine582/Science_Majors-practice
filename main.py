import matplotlib.pyplot as plt

scores = [80, 45, 34, 55]

slice_labels = ["Biology", "Chemistry", "Geology", "Physics"]

colors = ["brown", "blue", "grey", "green"]

plt.pie(scores, labels=slice_labels, colors=colors)

plt.title("Science Majors")

plt.savefig("Science_Majors.png")