import sys
from src.entity.config_entity import ClaimPredictorConfig
from src.entity.s3_estimator import Proj1Estimator
from src.exception import MyException
from src.logger import logging
from pandas import DataFrame


class InsuranceData:
    def __init__(self,
                subscription_length,
                vehicle_age,
                customer_age,
                region_code,
                region_density,
                segment,
                model,
                fuel_type,
                max_torque,
                max_power,
                engine_type,
                airbags,
                is_esc,
                is_adjustable_steering,
                is_tpms,
                is_parking_sensors,
                is_parking_camera,
                rear_brakes_type,
                displacement,
                cylinder,
                transmission_type,
                steering_type,
                turning_radius,
                length,
                width,
                gross_weight,
                is_front_fog_lights,
                is_rear_window_wiper,
                is_rear_window_washer,
                is_rear_window_defogger,
                is_brake_assist,
                is_power_door_locks,
                is_central_locking,
                is_power_steering,
                is_driver_seat_height_adjustable,
                is_day_night_rear_view_mirror,
                is_ecw,
                is_speed_alert,
                ncap_rating
                ):
        """
        Insurance Data constructor
        Input: all features of the trained model for prediction
        """
        try:
            self.subscription_length= subscription_length
            self.vehicle_age= vehicle_age
            self.customer_age= customer_age
            self.region_code= region_code
            self.region_density= region_density
            self.segment= segment
            self.model= model
            self.fuel_type= fuel_type
            self.max_torque= max_torque
            self.max_power= max_power
            self.engine_type= engine_type
            self.airbags= airbags
            self.is_esc= is_esc
            self.is_adjustable_steering= is_adjustable_steering
            self.is_tpms= is_tpms
            self.is_parking_sensors= is_parking_sensors
            self.is_parking_camera= is_parking_camera
            self.rear_brakes_type= rear_brakes_type
            self.displacement= displacement
            self.cylinder= cylinder
            self.transmission_type= transmission_type
            self.steering_type= steering_type
            self.turning_radius= turning_radius
            self.length= length
            self.width= width
            self.gross_weight= gross_weight
            self.is_front_fog_lights= is_front_fog_lights
            self.is_rear_window_wiper= is_rear_window_wiper
            self.is_rear_window_washer= is_rear_window_washer
            self.is_rear_window_defogger= is_rear_window_defogger
            self.is_brake_assist = is_brake_assist
            self.is_power_door_locks= is_power_door_locks
            self.is_central_locking= is_central_locking
            self.is_power_steering= is_power_steering
            self.is_driver_seat_height_adjustable= is_driver_seat_height_adjustable
            self.is_day_night_rear_view_mirror= is_day_night_rear_view_mirror
            self.is_ecw= is_ecw 
            self.is_speed_alert = is_speed_alert
            self.ncap_rating= ncap_rating

        except Exception as e:
            raise MyException(e, sys) from e

    def get_insurance_input_data_frame(self)-> DataFrame:
        """
        This function returns a DataFrame from USvisaData class input
        """
        try:
            
            vehicle_input_dict = self.get_insurance_data_as_dict()
            return DataFrame(vehicle_input_dict)
        
        except Exception as e:
            raise MyException(e, sys) from e


    def get_insurance_data_as_dict(self):
        """
        This function returns a dictionary from InsuranceData class input
        """
        logging.info("Entered get_usvisa_data_as_dict method as Insurance class")

        try:
            input_data = {
                "subscription_length":[self.subscription_length],
                "vehicle_age":[self.vehicle_age],
                "customer_age":[self.customer_age],
                "region_code":[self.region_code],
                "region_density":[self.region_density],
                "segment":[self.segment],
                "model":[self.model],
                "fuel_type":[self.fuel_type],
                "max_torque":[self.max_torque],
                "max_power":[self.max_power],
                "engine_type":[self.engine_type],
                "airbags":[self.airbags],
                "is_esc":[self.is_esc],
                "is_adjustable_steering":[self.is_adjustable_steering],
                "is_tpms":[self.is_tpms],
                "is_parking_sensors":[self.is_parking_sensors],
                "is_parking_camera":[self.is_parking_camera],
                "rear_brakes_type":[self.rear_brakes_type],
                "displacement":[self.displacement],
                "cylinder":[self.cylinder],
                "transmission_type":[self.transmission_type],
                "steering_type":[self.steering_type],
                "turning_radius":[self.turning_radius],
                "length":[self.length],
                "width":[self.width],
                "gross_weight":[self.gross_weight],
                "is_front_fog_lights":[self.is_front_fog_lights],
                "is_rear_window_wiper":[self.is_rear_window_wiper],
                "is_rear_window_washer":[self.is_rear_window_washer],
                "is_rear_window_defogger":[self.is_rear_window_defogger],
                "is_brake_assist":[self.is_brake_assist],
                "is_power_door_locks":[self.is_power_door_locks],
                "is_central_locking":[self.is_central_locking],
                "is_power_steering":[self.is_power_steering],
                "is_driver_seat_height_adjustable":[self.is_driver_seat_height_adjustable],
                "is_day_night_rear_view_mirror":[self.is_day_night_rear_view_mirror],
                "is_ecw":[self.is_ecw],
                "is_speed_alert":[self.is_speed_alert],
                "ncap_rating":[self.ncap_rating]
            }

            logging.info("Created Insurance data dict")
            logging.info("Exited get_Insurance_data_as_dict method as Insurance class")
            return input_data

        except Exception as e:
            raise MyException(e, sys) from e

class InsuranceClaimClassifier:
    def __init__(self,prediction_pipeline_config: ClaimPredictorConfig = ClaimPredictorConfig(),) -> None:
        """
        :param prediction_pipeline_config: Configuration for prediction the value
        """
        try:
            self.prediction_pipeline_config = prediction_pipeline_config
        except Exception as e:
            raise MyException(e, sys)

    def predict(self, dataframe) -> str:
        """
        This is the method of InsuranceClaimDataClassifier
        Returns: Prediction in string format
        """
        try:
            logging.info("Entered predict method of InsuranceClaimDataClassifier class")
            model = Proj1Estimator(
                bucket_name=self.prediction_pipeline_config.model_bucket_name,
                model_path=self.prediction_pipeline_config.model_file_path,
            )
            result =  model.predict(dataframe)
            
            return result
        
        except Exception as e:
            raise MyException(e, sys)