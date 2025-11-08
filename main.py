import trimesh
import numpy as np
import matplotlib.pyplot as plt
import os

def load_and_analyze(filepath):
    #Initial print
    print(f"\n{'='*30}")
    print(f"Analyzing: {os.path.basename(filepath)}")
    print('='*30)

    # Mesh loading
    mesh = trimesh.load(filepath)
    vertices = np.array(mesh.vertices)  
    faces = np.array(mesh.faces)
    
    
    num_vertices = vertices.shape[0]
    num_faces = faces.shape[0]
    
    print(f"Number of vertices: {num_vertices}")
    print(f"Number of faces: {num_faces}")
    
    #per-axis statistics
    axis_names = np.array(['X', 'Y', 'Z'])
    mins = np.min(vertices, axis=0)
    maxs = np.max(vertices, axis=0)
    means = np.mean(vertices, axis=0)
    stds = np.std(vertices, axis=0)
    
    
    for i, axis in enumerate(axis_names):
        print(f"\n{axis}-axis:")
        print(f"  Min: {mins[i]:.4f}")
        print(f"  Max: {maxs[i]:.4f}")
        print(f"  Mean: {means[i]:.4f}")
        print(f"  Std Dev: {stds[i]:.4f}")
    
    # Additional numpy-based analysis
    print(f"\nBounding box dimensions:")
    bbox_dims = maxs - mins
    print(f"  Width (X): {bbox_dims[0]:.4f}")
    print(f"  Depth (Y): {bbox_dims[1]:.4f}")
    print(f"  Height (Z): {bbox_dims[2]:.4f}")
    
    print(f"\nMesh centroid: ({means[0]:.4f}, {means[1]:.4f}, {means[2]:.4f})")
    
    # Visualization                                
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=faces, cmap='viridis', alpha=0.8, edgecolor='none')
    
    ax.set_title(f'{os.path.basename(filepath)}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    plt.tight_layout()
    plt.show()
    
    return mesh, vertices

meshes = "meshes/"
mesh_samples = np.array([i for i in os.listdir(meshes) if i.endswith('.obj')])

print(f"Found {len(mesh_samples)} sample mesh files")

for sample_filename in mesh_samples:
    filepath = os.path.join(meshes, sample_filename)
    mesh, vertices = load_and_analyze(filepath)