"""
# Labs: Write an Algorithm that splits a dataset by a computed midpoint, the algorithm should be able to search from the upper and
lower of the dataset
All right reserved lotus code studios Apr 2021
"""

dataset = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search(dataset, datum):
    mid = len(dataset) // 2
    high = dataset[: mid]
    low = dataset[mid:]

    # debugger
    print(f"High: {high}\nLow: {low}")
    count = 0

    if datum in high:
        # print(f"Datum {datum} found {high[datum]}")
        print("datum found at upper")
    elif datum in low:
        # print(f"Datum {datum} found at {low[datum]}")
        print("datum found at lower")
    else:
        print("Datum does not exists in the Dataset")


"""
# Labs: Write an Algorithm that splits a dataset by a computed midpoint, the algorithm should be able to search 
from the upper and lower of the dataset, if the datum is being found in upper re-split the dataset using a computed
midpoint and indicate which of the halfs the datum belong to in the upper


      
All right reserved lotus code studios Apr 2021
"""

dataset2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_searchV2(dataset, datum):
    mid = len(dataset) // 2
    high = dataset[: mid]
    low = dataset[mid:]

    # debugger
    print(f"High: {high}\nLow: {low}")
    count = 0

    if datum in high:

        high_mid = len(high) // 2
        higher = high[: high_mid]
        # print(f"Datum {datum} found {high[datum]}")

        if datum in higher:
            print(f"Datum {datum} found in higher {higher}")

        print("datum found at upper")
    elif datum in low:
        # print(f"Datum {datum} found at {low[datum]}")
        print("datum found at lower")
    else:
        print("Datum does not exists in the Dataset")


print(binary_searchV2(dataset2, 0))


def blastoff(counter):
    if counter != 0:
        print(counter)
        blastoff(counter - 1)


    else:
        print("Launched Successfully")

# blastoff(10)
