###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Ruoshui Mao
# Collaborators: Mr. K
# Time: 2
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # each index corresponds to the least eggs used for that weight
    eggs = [0, 1]
    
    for i in range(2, target_weight + 1):
        numEggs = []
        for w in egg_weights:
            if len(eggs) >= w:
                numEggs.append(eggs[i - w] + 1)
        eggs.append(min(numEggs))
    return eggs[target_weight]
    
##    if (egg_weights, target_weight) in memo:
##        result  = memo[(egg_weights, target_weight)]
##        
##    elif target_weight == 0:
##        result = 0
##    elif target_weight == 1:
##        result = 1        
##    elif len(egg_weights) == 1:
##        # when only weight 1 eggs are left
##        result = target_weight
##    else:
##        nextItem = egg_weights[len(egg_weights) - 1]
##        nextEggs = egg_weights[:-1]
##        
##        withVal = dp_make_weight(nextEggs, target_weight - nextItem, memo)
##        withVal += 1
##        
##        withoutVal = dp_make_weight(nextEggs, target_weight, memo)
##        
##        result = withVal if withVal < withoutVal else withoutVal
##        
##        memo[(egg_weights, target_weight)] = result
##        return result
##    pass

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
