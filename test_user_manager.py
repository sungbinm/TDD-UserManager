import unittest
from exceptions import UserNotFoundError, EmailAlreadyExistsError, UserIDAlreadyExistsError
from user_manager import UserManager

class TestUserManager(unittest.TestCase):

  def setUp(self) :
    self.manager = UserManager()
  
  # 유저추가 정상적으로 동작하는지 테스트
  def test_add_user_success(self):
    self.manager.add_user(1, "sungbinm", "sungbinm@naver.com")
    user = self.manager.get_user(1)
    self.assertEqual(user["name"], "sungbinm")
    self.assertEqual(user["email"], "sungbinm@naver.com")
  
  # 중복된 ID로 유저 추가 시 예외 발생 여부 테스트
  def test_add_user_duplicate_id(self):
     self.manager.add_user(1, "sungbinm", "sungbinm@naver.com")
     with self.assertRaises(UserIDAlreadyExistsError):
       self.manager.add_user(1, "suhyeon", "suhyeon@naver.com")
  
  # 중복된 email로 유저 추가 시 예외 발생 여부 테스트
  def test_add_user_duplicate_email(self):
    self.manager.add_user(1, "sungbinm", "sungbinm@naver.com")
    with self.assertRaises(EmailAlreadyExistsError) :
      self.manager.add_user(2, "suhyeon", "sungbinm@naver.com")
    
  # 유저삭제 정상적으로 동작하는지 테스트  
  def test_remove_user_success(self) :
    self.manager.add_user(1, "sungbinm", "sungbinm@naver.com")
    self.manager.remove_user(1)
    with self.assertRaises(UserNotFoundError) :
      self.manager.get_user(1)

  # 유저 이메일 업데이트 정상적으로 동작하는지 테스트
  def test_update_email_success(self):
    self.manager.add_user(1, "sungbinm", "sungbinm@naver.com")
    self.manager.update_email(1, "suhyeon@naver.com")
    user = self.manager.get_user(1)
    self.assertEqual(user["email"], "suhyeon@naver.com")

  # 다른 유저의 이메일로 업데이트시 예외 발생 여부 테스트
  def test_update_email_duplicate(self) :
    self.manager.add_user(1, "sungbinm", "sungbinm@naver.com")
    self.manager.add_user(2, "suhyeon", "suhyeon@naver.com")
    with self.assertRaises(EmailAlreadyExistsError) :
      self.manager.update_email(1, "suhyeon@naver.com")
  
  # 모든 유저를 가져오는 메서드 테스트
  def test_get_all_users(self) :
    self.manager.add_user(1, "sungbinm", "sungbinm@naver.com")
    self.manager.add_user(2, "suhyeon", "suhyeon@naver.com")
    users = self.manager.get_all_users()
    self.assertEqual(len(users), 2)
    self.assertEqual(users[0]["name"], "sungbinm")
    self.assertEqual(users[1]["name"], "suhyeon")
  
if __name__ == "__main__":
  unittest.main()
