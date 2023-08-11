"""Pipeline definitions."""
import logging
import time

from omegaconf import DictConfig


logger = logging.getLogger(__name__)


def pipeline_one(cfg: DictConfig) -> None:
    """Pipeline to create a linear regression model based on input data.

    Parameters
    ----------
    cfg : DictConfig
        Configs read in via Hydra.

    Returns
    -------
    None
    """
    logger.info("Component started - Data preparation.")
    start_time = time.time()
    # Data preparation component / function
    end_time = time.time()
    logger.info(f"Component ended - Data preparation. Time elapsed : {end_time-start_time:.3f} secs.")

    logger.info("Component started - Model training.")
    start_time = time.time()
    # Model training component / function
    end_time = time.time()
    logger.info(f"Component ended - Model training. Time elapsed : {end_time-start_time:.3f} secs.")

    logger.info("Component started - Model diagnosis.")
    start_time = time.time()
    # Model diagnosis component / function
    end_time = time.time()
    logger.info(f"Component ended - Model diagnosis. Time elapsed : {end_time-start_time:.3f} secs.")
