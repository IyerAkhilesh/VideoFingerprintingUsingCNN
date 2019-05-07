import matplotlib.pyplot as plotter

# training_accuracies_1 = [None, None, None, None, None, 94.62, 93.77, 94.9, 90, 90]

training_accuracies_1 = [0, 0, 0, 0, 0, 94.62, 0, 94.9, 0, 0]
training_accuracies_2 = [94.52, 94.67, 95.53, 94.73, 94.60, 93.86, 93.64, 95.02, 94.28, 95.36]
training_accuracies_3 = [95.82, 94.67, 94.75, 95.45, 95.15, 94.57, 95.04, 94.49, 95.49, 94.54]
train_ratios = [95, 90, 85, 80, 75, 70, 65, 60, 55, 50]
train_ratios.reverse()
subtractor = [0.2]
# validatn_accuracies = [23.31, 20.30, 40.60, 36.84, 40.60, 34.59, 33.83, 45.86, 61.65, 64.66, 67.67, 68.42, 61.65, 68.42, 65.41, 69.17]
# testing_accuracies  = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 69.12]
epochs_1 = [0, 0, 0, 0, 0, 17, 0, 11, 0, 0]
epochs_2 = [8, 9, 10, 10, 10, 8, 7, 9, 9, 13]
epochs_3 = [7, 8, 8, 8, 11, 8, 8, 8, 8, 7]

# training_box_1 = plotter.bar(x=train_ratios, height=training_accuracies_1, width=1.0, color="#882222cc", label="For 10 videos, 95 instances/video, lr=0.0001")
# training_box_2 = plotter.bar(x=train_ratios, height=training_accuracies_2, width=1.0, color="#228822cc", label="For 1 videos, 95 instances/video, lr=0.0001")
# training_box_3 = plotter.bar(x=train_ratios, height=training_accuracies_3, width=1.0, color="#222288cc", label="For 10 videos, 95 instances/video, lr=0.0005")

training_line_1 = plotter.plot(train_ratios, epochs_1, '#dd2222dd', linewidth=3.0, label="Convergence speed for 10 videos, lr=0.0001")
training_line_2 = plotter.plot(train_ratios, epochs_2, '#22dd22dd', linewidth=3.0, label="Convergence speed for 16 videos, lr=0.0001")
training_line_3 = plotter.plot(train_ratios, epochs_3, '#2222dddd', linewidth=3.0, label="Convergence speed for 16 videos, lr=0.0005")

legend = plotter.legend(loc='upper left', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#dddddd')
plotter.xlabel("Train proportion")
plotter.ylabel("Number of epochs")
plotter.show()


