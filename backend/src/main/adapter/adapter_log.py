import logging
from collections import deque
from datetime import datetime



# buffer log -> quantidades de logs
log_buffer = deque(maxlen=200)



class BufferHandler(logging.Handler):
    def emit(self, record):
        try:
            current_time = datetime.now().strftime("%H:%M:%S")
            log_buffer.appendleft({
                "time": current_time,
                "level": record.levelname,
                "logger": record.name,
                "message": record.getMessage()
            })
        except Exception as exception:
            print(f"erro log : {exception}")

    def setup_logging():
        handler = BufferHandler()
        # conexxão geral com log
        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.INFO)
        return log_buffer

def setup_logging():
    handler = BufferHandler()
    
    # Pega o logger raiz do Python
    root_logger = logging.getLogger()
    
    # Adiciona o nosso handler customizado
    root_logger.addHandler(handler)
    
    # Define o nível para INFO (captura info, warn e error)
    root_logger.setLevel(logging.INFO)
    
    return log_buffer