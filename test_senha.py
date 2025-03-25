import string
from senha import gerar_senha

def test_tamanho_senha():
    senha = gerar_senha(20)
    assert len(senha) == 20 

def test_tipos_de_caracteres():
    senha = gerar_senha(15, usar_maiusculas=False, usar_numeros=False, usar_simbolos=False)
    assert all(c in string.ascii_lowercase for c in senha)  

def test_combinacao_caracteres():
    senha = gerar_senha(10, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True)
    assert any(c in string.ascii_uppercase for c in senha) 
    assert any(c in string.digits for c in senha)  
    assert any(c in string.punctuation for c in senha)  
