import json
from os import environ
from typing import Dict, Optional

import boto3
from dotenv import load_dotenv
from injector import inject, singleton

load_dotenv()


@singleton
class Environment:
    @inject
    def __init__(self) -> None:
        self.__secret_environment: Dict[str, str] = {}
        if secret_arn := environ.get('SECRET_ARN'):
            response = boto3.client('secretsmanager').get_secret_value(SecretId=secret_arn)
            self.__secret_environment.update(json.loads(response['SecretString']))

    def get(self, name: str) -> Optional[str]:
        return self.__secret_environment.get(name, environ.get(name))
