# Extractor de información del correo electrónico
# Recopile una dirección de correo electrónico del usuario y luego averigüe si el usuario tiene un nombre de dominio personalizado
# o un nombre de dominio popular.


popular_domains = {
"gmail": "Google",
"hotmail":"Microsoft",
"yahoo":"Yahoo",
"outlook":"Microsoft"}

user_email = input("What is your email address? ")

user_name = user_email.split('@')[0]
user_domain = user_email.split('@')[-1]
user_domain = user_domain.split('.')[0]

if user_domain in popular_domains.keys():
    print(f"Hola {user_name} parece que tu email esta registrado con {popular_domains[user_domain]}. ¡Eso es genial!")
else:
    print(f"Hola {user_name} parece que estas usando un dominio personalizado de {user_domain}. ¡Impresionante!")