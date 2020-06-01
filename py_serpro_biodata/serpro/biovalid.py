import os
import base64
import json
import logging
import requests
from jose import jwt
from .constants import SERPRO_API_GATEWAY, AUTHENTICATE_ENDPOINT, \
    BIODATA_TOKEN_ENDPOINT, SERPRO_PUBLIC_JWKS, JWT_AUDIENCE


class SERPROBioValid:
    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.common_headers = {
            "Content-Type": "application/x-www-form-urlencoded"}
        self.base_url = f"{SERPRO_API_GATEWAY}"

    def authenticate(self):
        request_payload = {"grant_type": "client_credentials"}
        concat_keys = f"{self.consumer_key}:{self.consumer_secret}"
        b64_encoded_token = base64.b64encode(concat_keys.encode("utf-8"))
        headers = self.common_headers
        auth_token = f'{"Basic"} {b64_encoded_token.decode("utf-8")}'
        headers["Authorization"] = auth_token
        url = f"{self.base_url}{AUTHENTICATE_ENDPOINT}"
        response = requests.post(url, headers=headers, data=request_payload)
        return response

    def get_token(self):
        token = self.authenticate().json()
        return token["access_token"]

    def get_biodata_token(self, cpf):
        """
            https://biodata.estaleiro.serpro.gov.br/doc/4consultaapi/
        """
        url = f"{self.base_url}{BIODATA_TOKEN_ENDPOINT}?cpf={cpf}"
        logging.info(f"Getting token for CPF: {cpf}")
        access_token = self.get_token()
        headers = self.common_headers
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.post(url, headers=headers)
        logging.info(f"Biovalid token for CPF: {cpf} token: {response.text}")
        return response

    def get_jwks_public_key(self):
        url = SERPRO_PUBLIC_JWKS
        response = requests.get(url)
        jwks_key = response.json()
        return jwks_key

    def get_biovalid_return(self, key, token):
        alg = key['keys'][0]['alg']
        bio_key = key['keys'][0]
        audience = JWT_AUDIENCE
        payload = jwt.decode(token, bio_key,
                             algorithms=alg, audience=audience)

        return payload

    def validate_biodata_token(self, cpf, token):
        """
            https://biodata.estaleiro.serpro.gov.br/doc/4consultaapi/
        """
        url = f"{self.base_url}{BIODATA_TOKEN_ENDPOINT}?cpf={cpf}&token={token}"
        logging.info(f"Token validation for CPF: {cpf}")
        access_token = self.get_token()
        headers = self.common_headers
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        logging.info(
            f"Biovalid token validation for CPF: {cpf} and token: {response.text}"
        )
        return response
