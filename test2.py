import random
import string
import matplotlib.pyplot as plt

def read_names(filename):
    """
    Reads names from the given file and returns a list of names.
    Assumes that the name is the first word in each line.
    """
    names = []
    with open(filename, 'r') as f:
        for line in f:
            # Split the line into parts and take the first part as the name
            parts = line.strip().split()
            if parts:
                name = parts[0]
                names.append(name)
    return names

def select_random_names(names, percentage=50):
    """
    Randomly selects a given percentage of names from the list.
    """
    n = len(names)
    k = n * percentage // 100
    selected_names = random.sample(names, k)
    return selected_names

def letter_to_index(letter):
    """
    Converts a letter to its corresponding index (A=1, B=2, ..., Z=26).
    """
    letter = letter.upper()
    return ord(letter) - ord('A') + 1

def h1(x, l):
    """
    Hash function h1(x) = (sum of character indices) mod l.
    """
    total = 0
    for c in x:
        if c.isalpha():  # Ensure the character is a letter
            total += letter_to_index(c)
    return total % l

def h2(x, l, a_i):
    """
    Universal hash function h2(x) = (sum of f2(x_i, a_i)) mod l,
    where f2(x_i, a_i) = f(x_i) * a_i.
    """
    total = 0
    for idx, c in enumerate(x):
        if c.isalpha():
            total += letter_to_index(c) * a_i[idx]
    return total % l

def max_name_length(names):
    """
    Returns the length of the longest name in the list.
    """
    return max(len(name) for name in names)

def generate_ai(l, m_max):
    """
    Generates a list of random integers a_i for use in h2(x).
    Each a_i is a uniform random integer in [0, l-1].
    """
    a_i = [random.randint(0, l - 1) for _ in range(m_max)]
    return a_i

def plot_histograms(counts_h1, counts_h2, l):
    """
    Plots histograms of hash locations for h1(x) and h2(x).
    """
    plt.figure(figsize=(12, 6))

    # Histogram for h1(x)
    plt.subplot(1, 2, 1)
    plt.bar(range(l), counts_h1, width=1.0, edgecolor='none')
    plt.title('Histogram of Hash Locations for h1(x)')
    plt.xlabel('Hash Location')
    plt.ylabel('Frequency')

    # Histogram for h2(x)
    plt.subplot(1, 2, 2)
    plt.bar(range(l), counts_h2, width=1.0, edgecolor='none')
    plt.title('Histogram of Hash Locations for h2(x)')
    plt.xlabel('Hash Location')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

def plot_longest_chain(selected_names, l):
    """
    Plots the length of the longest chain as a function of the number of strings hashed.
    """
    n_values = range(1000, len(selected_names) + 1, 1000)
    longest_chains = []
    maxi = max_name_length(selected_names)
    for n in n_values:
        counts = [0] * l
        for name in selected_names[:n]:
            idx = h2(name, l, generate_ai(l, maxi)) 
            counts[idx] += 1
        longest_chain = max(counts)
        longest_chains.append(longest_chain)

    plt.figure()
    plt.plot(n_values, longest_chains, marker='o')
    plt.title('Length of the Longest Chain vs. Number of Strings Hashed')
    plt.xlabel('Number of Strings Hashed (n)')
    plt.ylabel('Length of the Longest Chain')
    plt.grid(True)
    plt.show()

def plot_collisions_vs_l(selected_names):
    """
    Plots the number of collisions as a function of table size l.
    Uses prime numbers for l and shows how collisions decrease as l increases.
    """
    # List of prime numbers for l
    l_values = [101, 503, 1009, 2017, 4093, 5701, 8011, 10007, 12011, 14009, 16001]
    n = len(selected_names)
    collision_counts = []
    maxi = max_name_length(selected_names)
    for l in l_values:
        counts = [0] * l
        for name in selected_names:
            idx = h2(name, l, generate_ai(l, maxi)) 
            counts[idx] += 1
        num_non_empty_buckets = sum(1 for count in counts if count > 0)
        num_collisions = n - num_non_empty_buckets
        collision_counts.append(num_collisions)

    plt.figure()
    plt.plot(l_values, collision_counts, marker='o')
    plt.title('Number of Collisions vs. Table Size l')
    plt.xlabel('Table Size (l)')
    plt.ylabel('Number of Collisions')
    plt.grid(True)
    plt.show()

def main():
    # Read names from file
    filename = 'dist.all.last.txt'  # Replace with the path to your file
    names = read_names(filename)

    # Randomly select 50% of the names
    selected_names = select_random_names(names, percentage=50)

    # Define the number of buckets
    l = 5701  # Given value for l

    # Find the maximum name length
    m_max = max_name_length(selected_names)

    # Generate random integers a_i for h2(x)
    a_i = generate_ai(l, m_max)

    # Initialize counts for hash locations
    counts_h1 = [0] * l
    counts_h2 = [0] * l

    # Hash the names using h1(x) and h2(x)
    for name in selected_names:
        idx_h1 = h1(name, l)
        counts_h1[idx_h1] += 1

        idx_h2 = h2(name, l, a_i)
        counts_h2[idx_h2] += 1

    # Produce histograms for both hash functions
    plot_histograms(counts_h1, counts_h2, l)

    # Part (d): Plot longest chain length vs. number of strings hashed
    plot_longest_chain(selected_names, l)

    # Part (d): Plot number of collisions vs. table size l
    plot_collisions_vs_l(selected_names)

if __name__ == '__main__':
    main()
