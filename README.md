# 3D Mesh Normalization & Quantization Pipeline

A reproducible pipeline for preprocessing 3D meshes for AI workflows: normalization, quantization, reconstruction and evaluation (including transformation-invariance analysis and adaptive quantization).


## Features
- Normalize meshes (min–max, unit sphere)
- Quantize and dequantize vertex coordinates (uniform & adaptive)
- Reconstruct and measure reconstruction error
- Test transformation invariance and produce detailed Task 4 summaries
- Save per-mesh outputs, plots and JSON logs for reproducibility

## Repository structure

- LICENSE
- main_2.ipynb                # Primary notebook to run the full pipeline
- requirements.txt            # Python dependencies
- meshes/                     # Put your input .obj mesh files here
- Outputs/                    # Outputs for Tasks 2/3 per mesh
- Outputs_Task4/              # Outputs and logs for Task 4 analyses

## Requirements
- Python 3.9+
- Create and use a virtual environment (recommended)
- See `requirements.txt` for the exact Python packages used

## Quick start (Windows)

1. Create a virtual environment

```powershell
python -m venv venv
```

2. Activate the environment

```powershell
./venv/Scripts/Activate.ps1
```

3. Install dependencies

```powershell
pip install -r requirements.txt
```

4. Run the notebook

Open `main_2.ipynb` in Jupyter or VS Code and run cells sequentially. The notebook executes the pipeline tasks (normalization, quantization, reconstruction, Task 4 analyses).

## Usage notes
- Place input meshes (OBJ files) into the `meshes/` directory before running.
- The notebook creates the `Outputs/` and `Outputs_Task4/` directories automatically when writing results.

## Outputs (what to expect)

- `Outputs/<mesh_name>/`
    - `normalized/` – normalized mesh files and arrays
    - `quantized/` – quantized representations and helper files
    - `plots/` – visualization PNGs for reconstruction/error
    - `normalization_params.json` – parameters used to normalize the mesh

- `Outputs_Task4/<mesh_name>/`
    - `transformations/` – transformed meshes used for invariance tests
    - `normalized/` – normalized files for Task 4
    - `quantized_uniform/` and `quantized_adaptive/` – quantization results
    - `reconstructions/` – reconstructed meshes from quantized data
    - `plots/` – figures for Task 4 analyses
    - `invariance_consistency_log.json` – per-mesh invariance logs

- Global Task 4 summaries:
    - `Outputs_Task4/task4_error_summary.csv`
    - `Outputs_Task4/task4_detailed_results.csv`
    - `Outputs_Task4/task4_conclusion.txt`

## Tips & troubleshooting
- Module errors: ensure the venv is activated before running.
- Performance: large meshes increase runtime and memory usage. Downsample meshes if necessary for quick tests.
- Invalid mesh: verify OBJ file integrity and that `trimesh` can load it.

## Reproducibility
All normalization parameters and logs are stored alongside outputs so that quantization and reconstruction steps can be repeated deterministically.

## License & author
This project is released under the MIT License.

Author: Pushkin Ranjan

---
