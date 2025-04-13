from dataclasses import dataclass

"""we are expecting below mentioned output as Data Ingestion Artifact"""
@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str

"""we are expecting below mentioned output as Data validation Artifact"""
@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    validation_report_file_path: str

"""we are expecting below mentioned output as Data Transformation Artifact"""
@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str

"""we are expecting below mentioned output as Classifiaction Metric Artifact"""
@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float
"""we are expecting below mentioned output as Model Trainer Artifact"""
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str 
    metric_artifact:ClassificationMetricArtifact


@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    changed_accuracy:float
    s3_model_path:str 
    trained_model_path:str

@dataclass
class ModelPusherArtifact:
    bucket_name:str
    s3_model_path:str