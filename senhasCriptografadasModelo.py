Primeiro dê um pip install passlib no terminal.
pip install passlib

Configura um contexto. OBS: quanto maior o número de rounds mais seguro, porém mais demorado também. Esse rounds é quantas vezes ele vai embaralhar a mesma string.
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["pdkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000
)

Definindo funções de hashing e verificação de string:
def hash_password(password):
    return pwd_context.hash(password)

def check_hashed_password(password, hashed):
    return pwd_context.verify(password, hashed)

Testando:
password = 'abc123'
hashed = hash_password(password)

Conferindo:
check_hashed_password('9y879', hashed) #retorna falso
check_hashed_password('abc123', hashed) #retorna verdadeiro

