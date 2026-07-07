import logging
from pathlib import Path


def setup_logger():
    """
    Configures the application logger.
    """

    # Ruta de la carpeta logs
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Configuración del logger
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_dir / "automation.log"),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(__name__)