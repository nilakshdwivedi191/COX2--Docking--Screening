import pandas as pd

# 1. Input experimental data matching your PyCharm folder files
data = {
    "Compound": ["Celecoxib", "D-Glucose", "Quercetin", "Apigenin", "Resveratrol"],
    "Role": ["Positive Control Benchmark", "Negative Control Decoy", "Natural Lead", "Natural Candidate", "Natural Candidate"],
    "SDF_File": ["celecoxide.sdf", "glucose.sdf", "quercetine.sdf", "apegenin.sdf", "resrevatol.sdf"],
    "Pose_File": ["celecoix_pose1.pdb", "dglucose_pose1.pdb", "qurecetin_pose1.pdb", "apigenin_pose1.pdb", "resrevatol_pose1.pdb"],
    "Binding_Affinity_kcal_mol": [-11.0, -4.8, -9.4, -9.0, -8.1],
    "Target_PDB": ["6COX", "6COX", "6COX", "6COX", "6COX"]
}

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# 3. Compute affinity difference relative to benchmark NSAID (Celecoxib)
benchmark = -11.0
df["Delta_vs_Celecoxib"] = df["Binding_Affinity_kcal_mol"] - benchmark

# 4. Save to CSV spreadsheet
df.to_csv("docking_summary_results.csv", index=False)

print("Data exported successfully to docking_summary_results.csv:")
print(df[["Compound", "Role", "Binding_Affinity_kcal_mol", "Delta_vs_Celecoxib"]])