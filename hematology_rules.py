class HematologyAnalyzer:
    @staticmethod
    def evaluate_jak2(status_jak2: str, hemogram: dict) -> dict:
        status_jak2 = status_jak2.strip().upper()
        
        if status_jak2 != "POSITIVO":
            return {
                "flag_risco": "NORMAL",
                "hipoteses": ["Sem indício direto de Neoplasia Mieloproliferativa por JAK2."],
                "condutas": ["Acompanhamento clínico de rotina."]
            }

        hipoteses = []
        ht = hemogram.get("hematocrito", 0.0)
        hb = hemogram.get("hemoglobina", 0.0)
        plt = hemogram.get("plaquetas", 0)

        if ht > 49.0 or hb > 16.5:
            hipoteses.append("Suspeita Elevada: Policitemia Vera (PV)")
        if plt > 450000:
            hipoteses.append("Suspeita Elevada: Trombocitemia Essencial (TE)")
        if not hipoteses:
            hipoteses.append("Investigar Mielofibrose Primária (MF) ou NMP Inespecífica")

        condutas = [
            "Encaminhar para consulta especializada em Hematologia",
            "Solicitar dosagem de Eritropoetina Sérica (EPO)",
            "Avaliar indicação de Biópsia e Aspirado de Medula Óssea",
            "Avaliar escore de risco trombótico e profilaxia"
        ]

        return {
            "flag_risco": "ALTO",
            "mutacao": "JAK2 V617F DETETADA",
            "hipoteses": hipoteses,
            "condutas": condutas
        }
