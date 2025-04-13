from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from uvicorn import run as app_run

from typing import Optional

# Importing constants and pipeline modules from the project
from src.constants import APP_HOST, APP_PORT
from src.pipline.prediction_pipeline import InsuranceData, InsuranceClaimClassifier
from src.pipline.training_pipeline import TrainPipeline

# Initialize FastAPI application
app = FastAPI()

# Mount the 'static' directory for serving static files (like CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 template engine for rendering HTML templates
templates = Jinja2Templates(directory='templates')

# Allow all origins for Cross-Origin Resource Sharing (CORS)
origins = ["*"]

# Configure middleware to handle CORS, allowing requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataForm:
    """
    DataForm class to handle and process incoming form data.
    This class defines the vehicle-related attributes expected from the form.
    """
    def __init__(self, request: Request):
        self.request: Request = request

        self.subscription_length: Optional[float] = None
        self.vehicle_age: Optional[float] = None
        self.customer_age: Optional[int] = None 
        self.region_code: Optional[float] = None
        self.region_density: Optional[int] = None 
        self.segment: Optional[float] = None
        self.model: Optional[ float] = None
        self.fuel_type: Optional[float] = None
        self.max_torque: Optional[float] = None
        self.max_power: Optional[float] = None
        self.engine_type: Optional[float] = None
        self.airbags: Optional[int ] = None 
        self.is_esc: Optional[float] = None
        self.is_adjustable_steering: Optional[float] = None
        self.is_tpms: Optional[float] = None
        self.is_parking_sensors: Optional[float] = None
        self.is_parking_camera: Optional[float] = None
        self.rear_brakes_type: Optional[float] = None
        self.displacement: Optional[int] = None  
        self.cylinder: Optional[int] = None  
        self.transmission_type: Optional[float] = None
        self.steering_type: Optional[float] = None
        self.turning_radius: Optional[float] = None
        self.length: Optional[int] = None  
        self.width: Optional[int] = None 
        self.gross_weight: Optional[int] = None  
        self.is_front_fog_lights: Optional[float] = None
        self.is_rear_window_wiper: Optional[float] = None
        self.is_rear_window_washer: Optional[float] = None
        self.is_rear_window_defogger: Optional[float] = None
        self.is_brake_assist : Optional[float] = None
        self.is_power_door_locks: Optional[float] = None
        self.is_central_locking: Optional[float] = None
        self.is_power_steering: Optional[float] = None
        self.is_driver_seat_height_adjustable: Optional[float] = None
        self.is_day_night_rear_view_mirror: Optional[float] = None
        self.is_ecw: Optional[float] = None
        self.is_speed_alert : Optional[float] = None
        self.ncap_rating: Optional[int] = None
                

    async def get_insurance_data(self):
        """
        Method to retrieve and assign form data to class attributes.
        This method is asynchronous to handle form data fetching without blocking.
        """
        form = await self.request.form()
        self.subscription_length= form.get("subscription_length")
        self.vehicle_age= form.get("vehicle_age")
        self.customer_age= form.get("customer_age")
        self.region_code= form.get("region_code")
        self.region_density= form.get("region_density")
        self.segment= form.get("segment")
        self.model= form.get("model")
        self.fuel_type= form.get("fuel_type")
        self.max_torque= form.get("max_torque")
        self.max_power= form.get("max_power")
        self.engine_type= form.get("engine_type")
        self.airbags= form.get("airbags")
        self.is_esc= form.get("is_esc")
        self.is_adjustable_steering= form.get("is_adjustable_steering")
        self.is_tpms= form.get("is_tpms")
        self.is_parking_sensors= form.get("is_parking_sensors")
        self.is_parking_camera= form.get("is_parking_camera")
        self.rear_brakes_type= form.get("rear_brakes_type")
        self.displacement= form.get("displacement")
        self.cylinder= form.get("cylinder")
        self.transmission_type= form.get("transmission_type")
        self.steering_type= form.get("steering_type")
        self.turning_radius= form.get("turning_radius")
        self.length= form.get("length")
        self.width= form.get("width")
        self.gross_weight= form.get("gross_weight")
        self.is_front_fog_lights= form.get("is_front_fog_lights")
        self.is_rear_window_wiper= form.get("is_rear_window_wiper")
        self.is_rear_window_washer= form.get("is_rear_window_washer")
        self.is_rear_window_defogger= form.get("is_rear_window_defogger")
        self.is_brake_assist = form.get("is_brake_assist")
        self.is_power_door_locks= form.get("is_power_door_locks")
        self.is_central_locking= form.get("is_central_locking")
        self.is_power_steering= form.get("is_power_steering")
        self.is_driver_seat_height_adjustable= form.get("is_driver_seat_height_adjustable")
        self.is_day_night_rear_view_mirror= form.get("is_day_night_rear_view_mirror")
        self.is_ecw= form.get("is_ecw")
        self.is_speed_alert= form.get("is_speed_alert")
        self.ncap_rating= form.get("ncap_rating")

# Route to render the main page with the form
@app.get("/", tags=["authentication"])
async def index(request: Request):
    """
    Renders the main HTML form page for vehicle data input.
    """
    return templates.TemplateResponse(
            "index.html",{"request": request, "context": "Rendering"})

# Route to trigger the model training process
@app.get("/train")
async def trainRouteClient():
    """
    Endpoint to initiate the model training pipeline.
    """
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return Response("Training successful!!!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")

# Route to handle form submission and make predictions
@app.post("/")
async def predictRouteClient(request: Request):
    """
    Endpoint to receive form data, process it, and make a prediction.
    """
    try:
        form = DataForm(request)
        await form.get_insurance_data()
        Insurance_Data = InsuranceData(
                                    subscription_length= form.subscription_length,
                                    vehicle_age= form.vehicle_age,
                                    customer_age= form.customer_age,
                                    region_code= form.region_code,
                                    region_density= form.region_density,
                                    segment= form.segment,
                                    model= form.model,
                                    fuel_type= form.fuel_type,
                                    max_torque= form.max_torque,
                                    max_power= form.max_power,
                                    engine_type= form.engine_type,
                                    airbags= form.airbags,
                                    is_esc= form.is_esc,
                                    is_adjustable_steering= form.is_adjustable_steering,
                                    is_tpms= form.is_tpms,
                                    is_parking_sensors= form.is_parking_sensors,
                                    is_parking_camera= form.is_parking_camera,
                                    rear_brakes_type= form.rear_brakes_type,
                                    displacement= form.displacement,
                                    cylinder= form.cylinder,
                                    transmission_type= form.transmission_type,
                                    steering_type= form.steering_type,
                                    turning_radius= form.turning_radius,
                                    length= form.length,
                                    width= form.width,
                                    gross_weight= form.gross_weight,
                                    is_front_fog_lights= form.is_front_fog_lights,
                                    is_rear_window_wiper= form.is_rear_window_wiper,
                                    is_rear_window_washer= form.is_rear_window_washer,
                                    is_rear_window_defogger= form.is_rear_window_defogger,
                                    is_brake_assist = form.is_brake_assist,
                                    is_power_door_locks= form.is_power_door_locks,
                                    is_central_locking= form.is_central_locking,
                                    is_power_steering= form.is_power_steering,
                                    is_driver_seat_height_adjustable= form.is_driver_seat_height_adjustable,
                                    is_day_night_rear_view_mirror= form.is_day_night_rear_view_mirror,
                                    is_ecw= form.is_ecw,
                                    is_speed_alert= form.is_speed_alert,
                                    ncap_rating= form.ncap_rating
                                )
        # Convert form data into a DataFrame for the model
        Insurance_df = Insurance_Data.get_insurance_input_data_frame()

        # Initialize the prediction pipeline
        model_predictor = InsuranceClaimClassifier()

        # Make a prediction and retrieve the result
        value = model_predictor.predict(dataframe=Insurance_df)[0]

        # Interpret the prediction result as 'Response-Yes' or 'Response-No'
        status = "Response-Yes" if value == 1 else "Response-No"

        # Render the same HTML page with the prediction result
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "context": status},
        )
        
    except Exception as e:
        return {"status": False, "error": f"{e}"}

# Main entry point to start the FastAPI server
if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)