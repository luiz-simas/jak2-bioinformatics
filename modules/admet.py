class LipinskiFilter:
    @staticmethod
    def check_lipinski(mw: float, logp: float, hbd: int, hba: int) -> dict:
        violations = 0
        details = []

        if mw > 500:
            violations += 1
            details.append("Massa Molecular > 500 Da")
        if logp > 5:
            violations += 1
            details.append("LogP > 5")
        if hbd > 5:
            violations += 1
            details.append("Doadores de H > 5")
        if hba > 10:
            violations += 1
            details.append("Aceitadores de H > 10")

        return {
            "pass_lipinski": violations <= 1,
            "violations_count": violations,
            "details": details
        }
