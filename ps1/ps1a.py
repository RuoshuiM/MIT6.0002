###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
from operator import itemgetter

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = {}
    inFile = open(filename, "r")
    
    for line in inFile:
        name, weight = line.split(',')
        cows[name] = int(weight)
    
    inFile.close()
    
    return cows

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    transport = []
    cowsL = sorted(list(cows.items()), key=itemgetter(1), reverse=True)
    
    while len(cowsL) > 0:
        ship = []
        totalWeight = 0
        for (cow, weight) in cowsL:
            if (totalWeight + weight) <= limit:
                ship.append((cow, weight))
                totalWeight += weight
        
        cowNames = []
        for cow in ship:
            cowsL.remove(cow)
            cowNames.append(cow[0])
            
        transport.append(cowNames)
    
    return transport
    
# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    optimal = []

    for comb in get_partitions(cows.items()):
        if any(sum(weight for _, weight in ship) > limit for ship in comb):
            # If a ship has a weight > 10, then this transport is invalid
            continue
        else:
            if not optimal:
                optimal = comb
            else:
                optimal = min(optimal, comb, key=len)
    
    # remove the weight int from optimal combination
    result = []
    for ship in optimal:
        result.append([name for name, _ in ship])
    return result
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data_2.txt")
    start = time.time()
    print(f"Greedy solution: {greedy_cow_transport(cows, 10)}", f"time: {time.time() - start}")
    start = time.time()
    print(f"Brute-force solution: {brute_force_cow_transport(cows, 10)}", f"time: {time.time() - start}")
    
compare_cow_transport_algorithms()
    
