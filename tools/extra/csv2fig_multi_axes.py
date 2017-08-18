import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys

def draw(argv):
	if len(argv)<2:
		print 'need *.log.train/test filename as parameter'
		exit()
	save_name = argv[1].split('.')[0] + '.png'
	with open(argv[1],'rb') as csvfile:
		csv_reader = csv.reader(csvfile, delimiter=',')
		header = next(csv_reader)
		loss_n = len(header) - 3
		loss_names = header[3:]
		iters = []
		loss = [[] for name in loss_names]
		for row in csv_reader:
			iters.append(float(row[0]))
			for loss_id in xrange(loss_n):
				loss[loss_id].append(float(row[loss_id+3]))
	skip_iter = 1000
	
	iters = np.array(iters)
	offset = 60
	loss = np.array(loss)
	start_id = np.where(iters > skip_iter)[0][0]
	iters = iters[start_id:]
	loss = loss[:,start_id:]
	#assert(loss_n==2)	
	print loss
	#fig = plt.figure()
	fig,axes = plt.subplots(nrows=loss_n)
	all_colors=('k','r','b','g','c')
	colors = all_colors[:loss_n]
	for ax, color, loss_vec,loss_name in zip(axes, colors, loss, loss_names):
		ax.plot(iters,loss_vec,color=color)
		ax.set_ylabel(loss_name,color=color)
	plt.title(save_name[:-4])
	#plt.legend(loss_names)
	plt.grid(True)
	plt.show()
	plt.savefig(save_name)

if __name__ == '__main__':
	draw(sys.argv)