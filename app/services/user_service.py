users = []

next_id = 1

def get_all_users():
    return users

def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user

def create_user(data):
    global next_id
    nome = data.get("nome")
    email = data.get("email")

    if not nome or not email:
        return None, {"erro": "O nome e email são obrigatórios"}
    
    user = {
        "id": next_id,
        "nome": nome,
        "email": email
    }

    users.append(user)

    next_id += 1

    return user, None

def update_user(user_id, data):
    user = get_user_by_id(user_id)

    if not user:
        return None, {"erro": "O usuário não foi encontrado"}
    
    nome = data.get("nome", None)
    email = data.get("email", None)

    if nome is None and email is None:
        return None, {"erro": "Não há dados para atualizar"}
    
    if nome is not None:
        user["nome"] = nome

    if email is not None:
        user["email"] = email

    return user, None

def delete_user(user_id):
    global users
    user = get_user_by_id(user_id)
    if not user:
        return None, {"erro":"O usuário não foi encontrado"}
    
    users = [user for user in users if user["id"] != user_id]
    return {"mensagem": "O usuário foi deletado"}, None