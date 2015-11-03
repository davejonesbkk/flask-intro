import os

#default config

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '!\xb5@G|\xe8\x81\xe7\x861\x8fV\xce\x1e\xee\x00\x912\xc3\xc5\x14\x9f\xe9;'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False