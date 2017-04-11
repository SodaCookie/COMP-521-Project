"""Defines operations used to visualize states of the board."""
from model.board.modifiers.resource import Resource

import matplotlib.pyplot as plot
from matplotlib.mlab import griddata
from mpl_toolkits.mplot3d import Axes3D
from numpy import meshgrid, linspace, zeros

def visualize_board_height(board, wireframe=False):
    X, Y = meshgrid(range(board.width), range(board.height))
    fx = X.flatten()
    fy = Y.flatten()
    z = [board[pos].elevation for pos in zip(X.flatten(), Y.flatten())]
    Z = griddata(fx, fy, z, range(board.width), range(board.height), interp="linear")

    fig = plot.figure()
    ax = fig.add_subplot(111, projection='3d')
    if wireframe:
        # Plot a basic wireframe.
        ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)
    else:
        # Plot surface
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1)
    plot.show()

def visualize_board_pathing(board):
    pathing = zeros((board.width, board.height))
    for i in range(board.width):
        for j in range(board.height):
            pathing[i, j] = int(board[i, j].pathable)

    fig = plot.figure()
    plot.imshow(pathing, cmap='Greys',  interpolation='nearest')
    plot.show()

def visualize_board_resources(board):
    resources = zeros((board.width, board.height))
    max_val = 1
    for i in range(board.width):
        for j in range(board.height):
            if board[i, j].has_modifier(Resource):
                resources[i, j] = int(board[i, j].get_modifier(Resource).amount)
                if resources[i, j] > max_val:
                    max_val = resources[i, j]

    fig = plot.figure()
    resources = resources / max_val
    plot.imshow(resources, cmap='Greys',  interpolation='nearest')
    plot.show()
