"""
### Exercício 6: Decorador de Autenticação

Crie um decorador chamado `autenticar_usuario` que receba como parâmetro um usuário e senha corretos. 
O decorador deve verificar se as credenciais fornecidas ao chamar a função estão corretas. Se estiverem, a função é executada; 
caso contrário, exibe uma mensagem de "Acesso negado".

#### Exemplo:
```python
@autenticar_usuario(usuario="admin", senha="1234")
def acesso_restrito():
    print("Bem-vindo à área restrita!")

acesso_restrito("admin", "1234")  # Bem-vindo à área restrita!
acesso_restrito("user", "senha_errada")  # Acesso negado
```

"""
def autenticar_usuario(func):
    
    usuario = "admin"
    senha = "1234"
    
    def autenticador(user,password, *args,**kwargs):
        if usuario  == user and senha == password:
            return func(*args,**kwargs)
        else:
            print("acesso negado")
    
    return autenticador

        
    

@autenticar_usuario
def acesso_restrito():
    print("Bem-vindo à área restrita!")


acesso_restrito("admin", "1234")  # Bem-vindo à área restrita!
acesso_restrito("user", "senha_errada")  # Acesso negado
