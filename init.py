import os

def load_config(mode=os.environ.get('MODE')):
    """Load config."""
    try:
        if mode == 'PRODUCTION':
            from config import ProdConfig
            return ProdConfig
        elif mode == 'DEVELOPMENT':
            from config import DevConfig 
            return DevConfig
        elif mode == 'TESTING':
            from config import TestConfig 
            return TestConfig
        else:
            from config import DevConfig
            return  DevConfig

    except ImportError:
        print("Set default mode")
        from config import DevConfig
        return DevConfig
