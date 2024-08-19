import os


def get_admin_id():
  admin_id = os.getenv("ADMIN_CHAT_ID")
  return admin_id

def is_admin(client_id):
  admin_id = get_admin_id()
  
  if not admin_id:
    print(f"Add ADMIN_CHAT_ID={client_id} to .env file")
    return False

  print(f"{client_id} == {admin_id}")
  return str(client_id) == str(admin_id)