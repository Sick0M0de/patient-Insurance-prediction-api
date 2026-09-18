from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models.predict import Model_verson, model, predict_output
from schemas.pydantic_model import user_input

app = FastAPI()


@app.get("/")
def homepage():
    return {"message": "Patient Insurace premiuim API"}


@app.get("health")
def health_check():
    return {"status": "OK", "version": Model_verson, "model_loaded": model is not None}


@app.post("/predict")
def premimum_prediction(data: user_input):

    user_input = {
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation,
    }

    try:
        prediction = predict_output(user_input)
        return JSONResponse(
            status_code=200, content={"predicted premium is ": prediction}
        )

    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))
