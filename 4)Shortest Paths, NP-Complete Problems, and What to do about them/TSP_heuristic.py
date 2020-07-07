import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def dist(A,B):
	return np.sqrt((A['x']-B['x'])**2 + (A['y']-B['y'])**2)

def dist_from(idx, visited, Graph):
	ans = pd.Series([np.inf]*len(Graph.index), index=Graph.index)
	for i in Graph.index:
		if i == idx or i in visited:
			continue
		else:
			ans[i] = dist(Graph.loc[idx], Graph.loc[i])
	return ans


if __name__ == '__main__':
	Graph = pd.read_table('nn.txt', sep=' ', index_col=0, names=['idx', 'x', 'y'], header=0)

	current_point_idx = 1
	visited = [1]
	cum_distance = 0

	while len(visited) < len(Graph.index):
		available_distances = dist_from(current_point_idx, visited, Graph)
		next_point_idx = np.argmin(available_distances) +1

		visited.append(next_point_idx)
		cum_distance += available_distances[next_point_idx]
		current_point_idx = next_point_idx

		print(len(visited))

	cum_distance += dist(Graph.loc[1], Graph.loc[current_point_idx])
	print(np.floor(cum_distance))