import matplotlib.pyplot as plt

# 1. Experimental Binding Scores (kcal/mol)
compounds = ['Celecoxib\n(Benchmark)', 'Glucose\n(Decoy)', 'Quercetin', 'Apigenin', 'Resveratrol']
vina_scores = [-11.0, -4.8, -9.4, -9.0, -8.1]

# 2. Color Palette (Blue=Benchmark, Red=Decoy, Green=Natural Candidates)
colors = ['#2b5c8f', '#d9534f', '#2ca02c', '#2ca02c', '#2ca02c']

# 3. Build Plot
plt.figure(figsize=(9, 5))
bars = plt.bar(compounds, vina_scores, color=colors, edgecolor='black', width=0.55)

# 4. Styling & Labels
plt.ylabel('Binding Free Energy ΔG (kcal/mol)', fontsize=12, fontweight='bold')
plt.title('Molecular Docking Binding Affinity Against COX-2 (PDB: 6COX)', fontsize=13, fontweight='bold')
plt.axhline(0, color='black', linewidth=0.8)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Add score labels on bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval - 0.45, f'{yval} kcal/mol',
             ha='center', va='bottom', fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig('docking_results_chart.png', dpi=300)
plt.show()
print("Chart generated successfully as docking_results_chart.png!")