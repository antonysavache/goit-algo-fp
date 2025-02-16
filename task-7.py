import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def simulate_dice_rolls(num_simulations):
    """Simulate rolling two dice multiple times"""
    results = []
    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        results.append(total)
    return results

def calculate_probabilities(results):
    """Calculate probability for each possible sum"""
    counter = Counter(results)
    total_rolls = len(results)
    probabilities = {sum_value: count/total_rolls
                     for sum_value, count in counter.items()}
    return dict(sorted(probabilities.items()))

def get_theoretical_probabilities():
    """Calculate theoretical probabilities for sum of two dice"""
    theoretical = {
        2: 1/36,   # (1,1)
        3: 2/36,   # (1,2), (2,1)
        4: 3/36,   # (1,3), (2,2), (3,1)
        5: 4/36,   # (1,4), (2,3), (3,2), (4,1)
        6: 5/36,   # (1,5), (2,4), (3,3), (4,2), (5,1)
        7: 6/36,   # (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)
        8: 5/36,   # (2,6), (3,5), (4,4), (5,3), (6,2)
        9: 4/36,   # (3,6), (4,5), (5,4), (6,3)
        10: 3/36,  # (4,6), (5,5), (6,4)
        11: 2/36,  # (5,6), (6,5)
        12: 1/36   # (6,6)
    }
    return theoretical

def create_probability_table(simulated_probs, theoretical_probs):
    """Create a formatted table comparing probabilities"""
    print("\nProbability Comparison Table:")
    print("-" * 60)
    print(f"{'Sum':<8} {'Theoretical':<15} {'Simulated':<15} {'Difference':<15}")
    print("-" * 60)

    for sum_value in range(2, 13):
        theo_prob = theoretical_probs[sum_value]
        sim_prob = simulated_probs.get(sum_value, 0)
        diff = abs(theo_prob - sim_prob)

        print(f"{sum_value:<8} {theo_prob:,.4f}        {sim_prob:,.4f}        {diff:,.4f}")
    print("-" * 60)

def plot_comparison(simulated_probs, theoretical_probs, num_simulations):
    """Plot comparison between simulated and theoretical probabilities"""
    plt.figure(figsize=(12, 6))

    x = list(theoretical_probs.keys())
    theoretical_values = list(theoretical_probs.values())
    simulated_values = [simulated_probs.get(k, 0) for k in x]

    width = 0.35
    x_pos = np.arange(len(x))

    # Create bars
    plt.bar(x_pos - width/2, theoretical_values, width,
            label='Theoretical', color='blue', alpha=0.6)
    plt.bar(x_pos + width/2, simulated_values, width,
            label='Simulated', color='red', alpha=0.6)

    # Customize plot
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability')
    plt.title(f'Dice Roll Probabilities\nMonte Carlo Simulation ({num_simulations:,} rolls)')
    plt.xticks(x_pos, x)
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Add value labels on bars
    for i, v in enumerate(theoretical_values):
        plt.text(i - width/2, v, f'{v:.3f}', ha='center', va='bottom', fontsize=8)
    for i, v in enumerate(simulated_values):
        plt.text(i + width/2, v, f'{v:.3f}', ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    plt.show()

def plot_convergence(max_rolls=100000, checkpoints=20):
    """Plot how the simulated probabilities converge to theoretical values"""
    theoretical_probs = get_theoretical_probabilities()
    rolls_per_checkpoint = max_rolls // checkpoints

    # Track error at each checkpoint
    errors = []
    num_rolls = []

    results = []
    for i in range(checkpoints):
        # Simulate more rolls
        new_rolls = simulate_dice_rolls(rolls_per_checkpoint)
        results.extend(new_rolls)

        # Calculate current probabilities and error
        current_probs = calculate_probabilities(results)
        avg_error = sum(abs(theoretical_probs[k] - current_probs.get(k, 0))
                        for k in theoretical_probs.keys()) / len(theoretical_probs)

        errors.append(avg_error)
        num_rolls.append(len(results))

    # Plot convergence
    plt.figure(figsize=(10, 5))
    plt.plot(num_rolls, errors, '-o')
    plt.xlabel('Number of Rolls')
    plt.ylabel('Average Absolute Error')
    plt.title('Convergence of Monte Carlo Simulation')
    plt.grid(True)
    plt.show()

def run_simulation(num_simulations=100000):
    """Run the complete simulation and analysis"""
    print(f"Running Monte Carlo simulation with {num_simulations:,} dice rolls...")

    # Run simulation
    results = simulate_dice_rolls(num_simulations)
    simulated_probs = calculate_probabilities(results)
    theoretical_probs = get_theoretical_probabilities()

    # Create probability comparison table
    create_probability_table(simulated_probs, theoretical_probs)

    # Plot probability comparison
    plot_comparison(simulated_probs, theoretical_probs, num_simulations)

    # Plot convergence
    print("\nGenerating convergence plot...")
    plot_convergence()

    # Calculate overall error
    avg_error = sum(abs(theoretical_probs[k] - simulated_probs.get(k, 0))
                    for k in theoretical_probs.keys()) / len(theoretical_probs)
    print(f"\nAverage absolute error: {avg_error:.6f}")

if __name__ == "__main__":
    # Run simulation with 100,000 rolls
    run_simulation(100000)