import numpy as np
from scipy import stats

# 1. Experimental groups (scores in kcal/mol)
glucose_score = -4.8  # Negative control decoy baseline
natural_scores = [-9.4, -9.0, -8.1]  # Quercetin, Apigenin, Resveratrol

# 2. Descriptive statistics
mean_natural = np.mean(natural_scores)
std_natural = np.std(natural_scores, ddof=1)

print("=== STATISTICAL SUMMARY ===")
print(f"Decoy Control Score (Glucose): {glucose_score} kcal/mol")
print(f"Natural Compounds Mean Score:  {mean_natural:.2f} kcal/mol (SD: {std_natural:.2f})")

# 3. One-sample t-test comparing natural compounds against decoy baseline
t_stat, p_value = stats.ttest_1samp(natural_scores, glucose_score)

print("\n=== HYPOTHESIS TESTING ===")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value:     {p_value:.4f}")

if p_value < 0.05:
    print("Conclusion: STATISTICALLY SIGNIFICANT (p < 0.05). Natural compounds demonstrate true binding affinity over decoy.")
else:
    print("Conclusion: NOT STATISTICALLY SIGNIFICANT (p >= 0.05).")