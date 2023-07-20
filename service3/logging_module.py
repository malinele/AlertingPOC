from datetime import datetime
from elasticsearch import Elasticsearch
import json


# Elasticsearch connection error
class ElasticsearchConnectionError(Exception):
    pass


try:
    with open('config.json') as f:
        config = json.load(f)

    es = Elasticsearch(hosts=[config['elasticsearch_url']])

    if not es.ping():
        raise ElasticsearchConnectionError("Can't connect to Elasticsearch!")

except FileNotFoundError:
    print("Config file not found.")
except json.JSONDecodeError:
    print("Error parsing config file.")
except ElasticsearchConnectionError as e:
    print(str(e))
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")


def log_to_elasticsearch(service_name, method_name, decision, data):
    doc = {
        'timestamp': datetime.utcnow(),
        'service': service_name,
        'method': method_name,
        'decision': decision,
        'data': data,
        'environment': config.get('environment', None)
        # Get the environment from the config file, if it's not available, set it to None
    }
    try:
        es.index(index="my-index", doc_type='_doc', body=doc)
    except Exception as e:
        print(f"An error occurred while trying to index the document: {str(e)}")
