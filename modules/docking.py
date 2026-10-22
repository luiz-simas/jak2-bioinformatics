import os
import subprocess

class AutoDockVinaRunner:
    def __init__(self, vina_executable="vina"):
        self.vina_executable = vina_executable

    def run_docking(self, receptor_pdbqt: str, ligand_pdbqt: str, center: tuple, size: tuple, output_pdbqt: str) -> dict:
        cx, cy, cz = center
        sx, sy, sz = size
        cmd = [
            self.vina_executable,
            "--receptor", receptor_pdbqt,
            "--ligand", ligand_pdbqt,
            "--center_x", str(cx), "--center_y", str(cy), "--center_z", str(cz),
            "--size_x", str(sx), "--size_y", str(sy), "--size_z", str(sz),
            "--out", output_pdbqt
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return {"status": "sucesso", "stdout": result.stdout}
        except Exception as e:
            return {"status": "erro", "detalhes": str(e)}
