# __init__.py
from .analytics_engine import AnalyticsEngine
from .data_processor import DataProcessor
from .report_generator import ReportGenerator
from .visualization_tools import VisualizationTools

__all__ = [
    'AnalyticsEngine',
    'DataProcessor',
    'ReportGenerator',
    'VisualizationTools',
]

# Initialize the analytics module with necessary configurations
def init_analytics_module(config):
    """
    Initialize the analytics module with the provided configuration.
    
    :param config: A dictionary containing configuration for the analytics module.
    """
    analytics_engine = AnalyticsEngine(config)
    data_processor = DataProcessor(config)
    report_generator = ReportGenerator(config)
    visualization_tools = VisualizationTools(config)

    return {
        'engine': analytics_engine,
        'processor': data_processor,
        'reporter': report_generator,
        'visualizer': visualization_tools,
    }