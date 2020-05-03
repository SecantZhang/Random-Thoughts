from random import random, uniform
from math import sqrt
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt


def inside_circle(center_coord, curr_coord, radius):
    return sqrt((curr_coord[0]-center_coord[0])**2 + (curr_coord[1]-center_coord[1])**2) < radius


def semicircle(center_coord, curr_row):
    """
    @param center_coord:    The coordinate of pool's center, represented as a tuple.
    @param curr_row:        The coordinate of four simulated ducks (points), represented as a list of tuples.
    @returns:               True if four points are in the same semi-circle, false if not.
    """
    # Calculate the line function for each coord and center.
    # Ax + By + C = 0: A=y2-y1, B=x1-x2, C=x2*y1-x1*y2. 2: center, 1: current point
    for i in range(4):
        A = center_coord[1]-curr_row[i][1]
        B = curr_row[i][0]-center_coord[0]
        C = center_coord[0]*curr_row[i][1]-curr_row[i][0]*center_coord[1]
        semicircle_result = [A*curr_row[j][0]+B*curr_row[j][1]+C >= 0 for j in range(4) if j != i]
        if len(set(semicircle_result)) == 1:
            return True
    return False


def main(canvas_size, sim_size):
    canvas_radius = float(canvas_size / 2)
    center_coord = (canvas_radius, canvas_radius)

    curr_sim_size = 0
    curr_success_size = 0
    curr_sim_matx = np.empty((sim_size + 1, 5))
    total_sim_count = 0
    step_average = []
    pbar = tqdm(total=sim_size)

    while curr_sim_size <= sim_size:
        total_sim_count += 1

        temp_row = [(uniform(0, canvas_size), uniform(0, canvas_size)) for i in range(4)]
        temp_row_truth = [inside_circle(center_coord, temp_coord, canvas_radius) for temp_coord in temp_row]

        if temp_row_truth != [1, 1, 1, 1]:  # Make sure the sampled result is within the circle.
            continue
        else:
            result_semicircle = semicircle(center_coord, temp_row)
            if result_semicircle:
                curr_success_size += 1
            curr_sim_matx[curr_sim_size] = temp_row.append(result_semicircle)
            curr_sim_size += 1
            step_average.append(curr_success_size / curr_sim_size)
            pbar.update(1)

    pbar.close()
    return float(curr_success_size / sim_size), step_average


def step_avg_plot(step_avg_list, output_path=None):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(range(len(step_avg_list)), step_avg_list)
    ax.set(xlabel='# Iteration', ylabel='Probability',
           title='Monte Carlo Simulation for Approximating the Ducks in Pool Problem')
    ax.grid()

    if output_path is not None:
        fig.savefig(output_path)
    plt.show()


if __name__ == "__main__":
    estimated_prob, step_average = main(500, 8000)
    print(estimated_prob)
    step_avg_plot(step_average)
