from src.DS_Project.config.configuration import ConfigurationManager
from src.DS_Project.components.model_evaluation import ModelEvaluation
from src.DS_Project import logger

STAGE_NAME="Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()