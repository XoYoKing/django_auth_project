from .models import User

class EmailBackend(object):
	def authenticate(self,request,**credentials):
		#要种族一表中中用户输入的用户名或者邮箱的field名均为username
		email = credentials.get('email',credentials.get('username'))
		try:
			user = User.objects.get(email=email)
		except User.DoesNotExist:
			pass
		else:
			if user.check_password(credentials["password"]):
				return user
	def get_user(self,user_id):
		# 这个方法是必须的
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None