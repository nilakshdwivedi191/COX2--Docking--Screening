import py3Dmol

# 1. Initialize 3D view
view = py3Dmol.view(width=800, height=600)

# 2. Load clean protein backbone
with open("clean_protien.pbd.pdb", "r") as f:
    protein_pdb = f.read()
view.addModel(protein_pdb, "pdb")
view.setStyle({'cartoon': {'color': 'cyan'}})

# 3. Load docked Quercetin pose
with open("qurecetin_pose1.pdb", "r") as f:
    ligand_pdb = f.read()
view.addModel(ligand_pdb, "pdb")
view.setStyle({'model': -1}, {'stick': {'colorscheme': 'yellowCarbon'}})

# 4. Zoom in and render HTML interactive viewer
view.zoomTo()
# 5. Save view as HTML file you can open in browser
with open("quercetin_3d_view.html", "w") as out:
    out.write(view._make_html())

print("3D view generated successfully! Open quercetin_3d_view.html in your browser.")