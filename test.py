import random
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


def preprocess_file(file_path):
    """
    Preprocess the raw text file to extract valid names.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Extract names (assuming names are in a specific column, e.g., first column)
    names = [line.split()[0] for line in lines if line.strip()]  # Adjust if column positions vary
    return names

def f(xi):
    """
    Returns the index of the character in the alphabet (A=1, Z=26).
    """
    return ord(xi) - ord('A') + 1

def h1(x, ell):
    """
    Hash function h1(x) as defined.
    """
    return sum(f(xi) for xi in x) % ell

def h2(x, ell):
    """
    Hash function h2(x) as defined.
    """
    a = [random.randint(0, ell - 1) for _ in x]  # Random coefficients
    return sum(f(xi) * ai for xi, ai in zip(x, a)) % ell

def hash_names(names, ell):
    """
    Hash the given names using h1 and h2.
    """
    h1_hashes = [h1(name, ell) for name in names]
    h2_hashes = [h2(name, ell) for name in names]
    return h1_hashes, h2_hashes


def plot_histogram(hash_values, ell, title, xlabel, ylabel):
    """
    Plot a histogram of hash values.
    """
    # Count frequencies of hash values
    frequency = Counter(hash_values)
    buckets = list(range(ell))
    counts = [frequency[b] if b in frequency else 0 for b in buckets]

    # Create the histogram
    plt.figure(figsize=(10, 6))
    plt.bar(buckets, counts, width=1.0, edgecolor="black", align="center")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()
    
    
def compute_longest_chain(hash_values):
    """
    Compute the length of the longest chain for chaining collision resolution.
    """
    frequency = Counter(hash_values)
    return max(frequency.values())

# def compute_collisions(hash_values):
#     """
#     Compute the number of collisions (buckets with more than one item).
#     """
#     frequency = Counter(hash_values)
#     return sum(1 for count in frequency.values() if count > 1)

def plot_longest_chain_vs_n(hash_values, step=100):
    """
    Plot the length of the longest chain as a function of the number of hash values.
    """
    n_values = list(range(step, len(hash_values) + 1, step))
    longest_chains = []

    for n in n_values:
        sampled_hashes = hash_values[:n]
        longest_chains.append(compute_longest_chain(sampled_hashes))

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, longest_chains, marker='o')
    plt.title("Longest Chain Length vs. Number of Strings (n)")
    plt.xlabel("Number of Strings (n)")
    plt.ylabel("Longest Chain Length")
    plt.grid()
    plt.show()

def plot_collisions_vs_buckets(hash_values, ell_values):
    """
    Plot the number of collisions as a function of the number of buckets (ℓ).
    """
    collisions = []

    for ell in ell_values:
        # Re-hash values to new bucket size
        rehashed = [h % ell for h in hash_values]
        collisions.append(compute_collisions(rehashed))

    plt.figure(figsize=(10, 6))
    plt.plot(ell_values, collisions, marker='o')
    plt.title("Number of Collisions vs. Number of Buckets (ℓ)")
    plt.xlabel("Number of Buckets (ℓ)")
    plt.ylabel("Number of Collisions")
    plt.grid()
    plt.show()

# Parameters
file_path = "dist.all.last.txt"  # Replace with the actual path
ell = 5701  # Number of buckets

# Steps
names = preprocess_file(file_path)  # Step 1: Preprocess file to extract names
sampled_names = random.sample(names, len(names) // 2)  # Step 2: Randomly select 50% of names
h1_hashes, h2_hashes = hash_names(sampled_names, ell)  # Step 3: Compute hash values


# Generate histograms
# plot_histogram(h1_hashes, ell, title="Histogram of h1(x)", xlabel="Bucket Index", ylabel="Frequency")
# plot_histogram(h2_hashes, ell, title="Histogram of h2(x)", xlabel="Bucket Index", ylabel="Frequency")


# Prime numbers for bucket sizes
ell_values = [1000, 3000, 5000, 7000]

# Plot for h1(x)
print("Plots for h1(x):")
plot_longest_chain_vs_n(h1_hashes)
# plot_collisions_vs_buckets(h1_hashes, ell_values)

# Plot for h2(x)
print("Plots for h2(x):")
plot_longest_chain_vs_n(h2_hashes)
# plot_collisions_vs_buckets(h2_hashes, ell_values)

def compute_collisions(hash_values, ell):
    """
    Compute the number of collisions for a specific bucket size (ℓ).
    """
    rehashed = [h % ell for h in hash_values]
    frequency = Counter(rehashed)
    return sum(1 for count in frequency.values() if count > 1)

def plot_collisions_vs_buckets(names, ell_values, hash_function):
    """
    Plot the number of collisions as a function of the number of buckets (ℓ).
    """
    collisions = []

    for ell in ell_values:
        # Recompute hash values for the new bucket size
        hash_values = [hash_function(name, ell) for name in names]
        collisions.append(compute_collisions(hash_values, ell))

    plt.figure(figsize=(10, 6))
    plt.plot(ell_values, collisions, marker='o')
    plt.title("Number of Collisions vs. Number of Buckets (ℓ)")
    plt.xlabel("Number of Buckets (ℓ)")
    plt.ylabel("Number of Collisions")
    plt.grid()
    plt.show()


def h2_rehash(names, ell):
    """
    Rehash names using h2(x) for a given number of buckets (ℓ), with random coefficients a_i.
    """
    rehashed = []
    for name in names:
        a = [random.randint(0, ell - 1) for _ in name]  # Generate random coefficients for each character
        rehashed_value = sum(f(xi) * ai for xi, ai in zip(name, a)) % ell
        rehashed.append(rehashed_value)
    return rehashed


def plot_collisions_vs_buckets_h2(names, ell_values):
    """
    Plot the number of collisions for h2(x) as a function of the number of buckets (ℓ).
    """
    collisions = []

    for ell in ell_values:
        # Recompute h2 hash values for the new bucket size
        hash_values = h2_rehash(names, ell)
        collisions.append(compute_collisions(hash_values, ell))

    plt.figure(figsize=(10, 6))
    plt.plot(ell_values, collisions, marker='o')
    plt.title("Number of Collisions for h2(x) vs. Number of Buckets (ℓ)")
    plt.xlabel("Number of Buckets (ℓ)")
    plt.ylabel("Number of Collisions")
    plt.grid()
    plt.show()

# Run the corrected plotting function
plot_collisions_vs_buckets_h2(sampled_names, ell_values)


# Plot for h1(x)
print("Collisions for h1(x):")
plot_collisions_vs_buckets(sampled_names, ell_values, h1)

# Plot for h2(x)
print("Collisions for h2(x):")
plot_collisions_vs_buckets(sampled_names, ell_values, h2)


