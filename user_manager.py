from exceptions import UserNotFoundError, EmailAlreadyExistsError, UserIDAlreadyExistsError


class UserManager:
  # 유저 데이터 딕셔너리, 이메일 중복확인
  def __init__(self) :
    self.users = {}
    self.emails = set()
  
  # 새로운 유저 추가. ID나 이메일이 중복되면 예외 발생.
  def add_user(self, user_id, name, email) :
    if user_id in self.users:
      raise UserIDAlreadyExistsError("User Id {user_id} alread exists.")
    
    if email in self.emails:
      raise EmailAlreadyExistsError("Email {email} already exists.")
    
    self.users[user_id] = {"name" : name, "email" : email}
    self.emails.add(email)

  # 유저 ID로 유저 정보
  def get_user(self, user_id) :
      if user_id not in self.users:
        raise UserNotFoundError("User ID {user_id} not found. ")
      return self.users[user_id]
    
  # 유저 삭제
  def remove_user(self, user_id):
    if user_id not in self.users:
      raise UserNotFoundError("User ID {user_id} not found. ")
    
    user = self.users.pop(user_id)
    self.emails.remove(user["email"])

  # 유저 이메일 업데이트
  def update_email(self, user_id, new_email) :
    if user_id not in self.users:
      raise UserNotFoundError("User ID {user_id} not found. ")
    
    if new_email in self.emails:
      raise EmailAlreadyExistsError("Email {email} already exists.")
    
    user = self.users[user_id]
    self.emails.remove(user["email"])
    user["email"] = new_email
    self.emails.add(new_email)

  def get_all_users(self):
    return list(self.users.values())