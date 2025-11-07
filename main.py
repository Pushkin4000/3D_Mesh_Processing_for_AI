import trimesh
import numpy as np
import matplotlib.pyplot as plt
import os

def load_and_analyze(filepath):
    #Initial print
    print(f"\n{'='*50}")
    print(f"Analyzing: {os.path.basename(filepath)}")
    print('='*50)

    # Mesh loading
    mesh = trimesh.load(filepath)
    vertices = mesh.vertices
    
    # Basic statistics
    print(f"Number of vertices: {len(vertices)}")
    print(f"Number of faces: {len(mesh.faces)}")
    
    # Per-axis statistics
    for i, axis in enumerate(['X', 'Y', 'Z']):
        print(f"\n{axis}-axis:")
        print(f"  Min: {vertices[:, i].min():.4f}")
        print(f"  Max: {vertices[:, i].max():.4f}")
        print(f"  Mean: {vertices[:, i].mean():.4f}")
        print(f"  Std Dev: {vertices[:, i].std():.4f}")
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot_trisurf(mesh.vertices[:, 0], mesh.vertices[:, 1], mesh.vertices[:, 2],
                    triangles=mesh.faces, cmap='viridis', alpha=0.8, edgecolor='none')
    
    ax.set_title(f'{os.path.basename(filepath)}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    plt.tight_layout()
    plt.show()
    
    return mesh, vertices

meshes = "meshes/"
mesh_samples = [i for i in os.listdir(meshes) if i.endswith('.obj')]

print(f"Found {len(mesh_samples)} sample mesh files")

for sample_filename in mesh_samples:
    filepath = os.path.join(meshes, sample_filename)
    mesh, vertices = load_and_analyze(filepath)