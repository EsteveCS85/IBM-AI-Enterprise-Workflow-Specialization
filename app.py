from __future__ import annotations

import time
from typing import Any, Dict

from flask import Flask, jsonify, request

from logger import PredictionLogger
from model import RevenueModel

# Crear la app Flask
app = Flask(__name__)
model = RevenueModel()
logger = PredictionLogger()


# Ruta principal
@app.get("/")
def home() -> Dict[str, str]:
    return {"message": "Bienvenido a la API. Usa POST /predict para predicciones."}


# Ruta para predicciones
@app.post("/predict")
def hacer_prediccion() -> Any:
    datos = request.get_json(silent=True) or {}
    pais = datos.get("country")

    inicio = time.perf_counter()
    resultado = model.predict(country=pais)
    tiempo = (time.perf_counter() - inicio) * 1000

    # Guardar log
    logger.log(country=str(resultado.get("country", "Unknown")), runtime_ms=tiempo, prediction=resultado)

    return (
        jsonify(
            {
                "prediction": {
                    "country": pais or "ALL",
                    "average_revenue": resultado.get("average_revenue", 0.0),
                    "observations": resultado.get("observations", 0),
                    "model_version": resultado.get("model_version", "unknown"),
                },
                "runtime_ms": round(tiempo, 2),
            }
        ),
        200,
    )


# Iniciar servidor
if __name__ == "__main__":
    app.run(debug=True, port=5000)
