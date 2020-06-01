import os
from serpro.biovalid import SERPROBioValid

SERPRO_CONSUMER_KEY = os.getenv("SERPRO_CONSUMER_KEY")
SERPRO_CONSUMER_SECRET = os.getenv("SERPRO_CONSUMER_SECRET")
TEST_CPF = os.getenv("SERPRO_TEST_CPF")


class TestSERPROBioValid:
    def test_authentication(self):
        session = SERPROBioValid(SERPRO_CONSUMER_KEY, SERPRO_CONSUMER_SECRET)
        response = session.authenticate()
        assert response.status_code == 200

    def test_get_token(self):
        session = SERPROBioValid(SERPRO_CONSUMER_KEY, SERPRO_CONSUMER_SECRET)
        access_token = session.get_token()
        assert access_token is not None

    def test_get_biodata_token(self):
        session = SERPROBioValid(SERPRO_CONSUMER_KEY, SERPRO_CONSUMER_SECRET)
        biodata_token = session.get_biodata_token(str(TEST_CPF))
        assert biodata_token.status_code == 200
        assert biodata_token.text is not None

    def test_get_jwks_key(self):
        session = SERPROBioValid(SERPRO_CONSUMER_KEY, SERPRO_CONSUMER_SECRET)
        serpro_jwks_key = session.get_jwks_public_key()
        assert serpro_jwks_key is not None
