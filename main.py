"""
Factory function to raise a number to the power of n.
"""

def power(n):
    def power_n(num):
        return num ** n
    return power_n

if __name__ == "__main__":

    squarer = power(2)
    print(squarer(3))

    cuber = power(3)
    print(cuber(3))
