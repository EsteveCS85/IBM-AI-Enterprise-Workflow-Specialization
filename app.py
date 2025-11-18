from __future__ import annotations

import time
from typing import Any, Dict

from flask import Flask, jsonify, request

from logger import PredictionLogger
from model import RevenueModel

app = Flask(__name__)
model = RevenueModel()
prediction_logger = PredictionLogger()


# Mensaje de bienvenida para la ruta principal
@app.get("/")
def root() -> Dict[str, str]:
    return {"message": "Capstone revenue API. Use POST /predict."}


# Endpoint para hacer predicciones
@app.post("/predict")
def predict() -> Any:
    payload = request.get_json(silent=True) or {}
    country = payload.get("country")

    start = time.perf_counter()
    prediction = model.predict(country=country)
    runtime_ms = (time.perf_counter() - start) * 1000

    # Guardar el log de la predicción
    prediction_logger.log(country=prediction["country"], runtime_ms=runtime_ms, prediction=prediction)

    return (
        jsonify(
            {
                "input_country": country or "ALL",
                "prediction": prediction,
                "runtime_ms": round(runtime_ms, 2),
            }
        ),
        200,
    )


# Ejecutar la aplicación en modo debug
if __name__ == "__main__":
    app.run(debug=True, port=5000)
