import os
from src.constant.confidential import API_KEY,API_SECRET_KEY,BOOTSTRAP_SERVER,SCHEMA_REGISTRY_API_KEY,SCHEMA_REGISTRY_API_SECRET,ENDPOINT_SCHEMA_URL

SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"

"""API_KEY = os.getenv('API_KEY',None)
ENDPOINT_SCHEMA_URL  = os.getenv('ENDPOINT_SCHEMA_URL',None)
API_SECRET_KEY = os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER',None)
SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET',None)"""

# Kafka Cluster Configration
def sasl_conf():
    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }

    return sasl_conf

# Kafka Schema Configration
def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"
    }

if __name__ == '__main__':
    sasl_conf()