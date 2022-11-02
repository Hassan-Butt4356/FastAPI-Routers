from fastapi import FastAPI
from database import engine,Base

from api1 import main as api1_main
from api2 import main as api2_main
from api1 import models as api1_models
from api2 import models as api2_models

# api1_models.Base.metadata.create_all(bind=engine)
# api2_models.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(api1_main.router)
app.include_router(api2_main.router)