""" Utility functions to compute distances and related metrics """

def dist_squared(x0, y0, x1, y1):
	dx = x1 - x0
	dy = y1 - y0
	return dx ** 2 + dy ** 2