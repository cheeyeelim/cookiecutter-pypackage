"""Entrypoint for {{ cookiecutter.pkg_name }}."""
import logging
import time

import hydra
from omegaconf import DictConfig

from {{ cookiecutter.pkg_name }}.pipeline import pipeline_one

logger = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="../input/conf", config_name="config")
def main(cfg: DictConfig) -> None:
    """Main entrypoint.

    Parameters
    ----------
    cfg : DictConfig
        Configs read in via Hydra.

    Returns
    -------
    None
    """
    # Execute pipeline
    logger.info("Pipeline started - pipeline_one.")
    start_time = time.time()
    
    pipeline_one(cfg=cfg)

    end_time = time.time()
    logger.info(f"Pipeline ended - pipeline_one. Time elapsed : {end_time-start_time:.3f} secs.")


if __name__ == "__main__":
    main()  # pragma: no cover
