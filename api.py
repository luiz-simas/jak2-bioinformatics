from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from modules.hematology_rules import HematologyAnalyzer
from modules.admet import LipinskiFilter

app = FastAPI(title="JAK2 Bioinformatic & HTVS API")

class PatientData(BaseModel):
    status_jak2: str
    hemoglobina: float
    hematocrito: float
    plaquetas: int
    leucocitos: int

class MoleculeData(BaseModel):
    mw: float
    logp: float
    hbd: int
    hba: int

@app.post("/analyze/patient")
def analyze_patient(data: PatientData):
    hemogram = {
        "hemoglobina": data.hemoglobina,
        "hematocrito": data.hematocrito,
        "plaquetas": data.plaquetas,
        "leucocitos": data.leucocitos
    }
    return HematologyAnalyzer.evaluate_jak2(data.status_jak2, hemogram)

@app.post("/analyze/admet")
def analyze_admet(data: MoleculeData):
    return LipinskiFilter.check_lipinski(data.mw, data.logp, data.hbd, data.hba)
