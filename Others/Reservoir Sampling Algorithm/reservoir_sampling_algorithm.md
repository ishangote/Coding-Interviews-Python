# Reservoir Sampling Algorithm

Reservoir sampling is an efficient algorithm for selecting a random item from a stream of data of unknown or very large size, ensuring that each item has an equal probability of being chosen. Let’s go over how it works and why it maintains uniform probability.

## Problem Statement

Given a stream of numbers of unknown size, select one number uniformly at random, such that every number in the stream has the same probability of being selected.

## Reservoir Sampling

Reservoir sampling, specifically the simplest version (k = 1), allows us to select a single item from a stream with equal probability.

1. Initialize the "reservoir":

   - Start with an empty "reservoir," which will hold our single, randomly selected item.

2. Process each item in the stream one by one:

   - For the first item, store it in the reservoir.
   - For every subsequent item (starting from the second one), generate a random number j between 0 and the item’s position index (inclusive).
   - If j is 0, replace the current item in the reservoir with the new item; otherwise, keep the current item in the reservoir.

3. Return the item in the reservoir after processing the entire stream.

## Why Reservoir Sampling Works

To understand why every item in the stream has an equal probability of being in the reservoir, let's break down the probability that each item remains in the reservoir.

1. Probability of First Item (Index 1):

   - When the first item is added, it is stored in the reservoir with a 100% probability.
   - For it to stay in the reservoir, each subsequent item must fail to replace it.

2. Probability of a Given Item Being Selected (Index n):

   - When processing the n-th item, the probability of choosing it to replace the reservoir item is 1/n.
   - The probability of the n-th item remaining in the reservoir until the end of the stream must consider that it was chosen and that all subsequent items failed to replace it. This ensures that, at any point in the stream, every item has a probability of 1/n​ of being in the reservoir.

3. Uniform Probability Across All Items:
   - Due to the random replacement at each step, each item in the stream has an equal 1/n chance of being the reservoir item after processing n items, ensuring uniform probability.
