#!/usr/bin/python3
"""
Prime Game Solution

This module implements the solution to the "Prime Game" task. 
Maria and Ben play a game involving consecutive integers and prime numbers.
This module provides functions to simulate the game and determine the winner.

Functions:
- findMultiples(num, targets): Removes multiples of a given number from a list.
- isPrime(i): Checks if a number is a prime.
- findPrimes(n): Counts and removes prime numbers and their multiples from a set.
- isWinner(x, nums): Determines the overall winner after multiple rounds of the game.
"""

from typing import Literal, Any


def findMultiples(num, targets) -> Any:
    """
    Removes multiples of a given number from a list.

    Args:
        num (int): The number whose multiples are to be removed.
        targets (list[int]): The list of numbers to filter.

    Returns:
        list[int]: The updated list with multiples of num removed.
    """
    for i in targets:
        if i % num == 0:
            targets.remove(i)
    return targets


def isPrime(i) -> bool:
    """
    Checks if a number is a prime.

    Args:
        i (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if i == 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


def findPrimes(n) -> int:
    """
    Counts and removes prime numbers and their multiples from a set.

    Args:
        n (set[int]): A set of integers.

    Returns:
        int: The count of prime numbers removed from the set.
    """
    counter = 0
    target = list(n)
    for i in range(1, len(target) + 1):
        if isPrime(i):
            counter += 1
            target.remove(i)
            target = findMultiples(i, target)
    return counter


def isWinner(x, nums) -> None | Literal['Maria'] | Literal['Ben']:
    """
    Determines the winner of the game after multiple rounds.

    Args:
        x (int): The number of rounds played.
        nums (list[int]): A list containing the upper limits for each round.

    Returns:
        Literal['Maria', 'Ben', None]: 
            - 'Maria' if Maria wins more rounds.
            - 'Ben' if Ben wins more rounds.
            - None if there is a tie.
    """
    players = {'Maria': 0, 'Ben': 0}
    cluster = set()
    for elem in range(x):
        nums.sort()
        num = nums[elem]
        for i in range(1, num + 1):
            cluster.add(i)
            if i == num + 1:
                break
        temp = findPrimes(cluster)

        if temp % 2 == 0:
            players['Ben'] += 1
        elif temp % 2 != 0:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
