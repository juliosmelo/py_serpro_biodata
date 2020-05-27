![Python package](https://github.com/juliosmelo/py_serpro_biodata/workflows/Python%20package/badge.svg?branch=master)

## Instalando

```bash
pip install py_serpro_biodata
```

## Como usar

Solicitando o token de autenticação

```python
session = SERPROBioValid(SERPRO_CONSUMER_KEY, SERPRO_CONSUMER_SECRET)
session = session.authenticate()
session.get_token()
```

Solicitando token para realiazar o processo da prova de vida

```python
cpf = 11111111111
session = SERPROBioValid(SERPRO_CONSUMER_KEY, SERPRO_CONSUMER_SECRET)
session = session.authenticate()
session.get_biodata_token(cpf)
```

Com esse token você pode baixar o aplicativo BIOValid do SERPRO. Informar o token a na tela inicial e fazer o processo de prova de vida.

Após realizar o processo no aplicativo BIOValid do SERPRO. Você precisa verificar o resultada da prova de vida.

```python
token = <TOKEN_QUE_FOI_USADO_PARA_FAZER_A_PROVA_DE_VIDA>
cpf = 11111111111
session = SERPROBioValid(SERPRO_CONSUMER_KEY, SERPRO_CONSUMER_SECRET)
session = session.authenticate()
session.validate_biodata_token(cpf, token)
```
