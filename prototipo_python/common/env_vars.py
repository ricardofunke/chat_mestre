from environs import Env

env = Env()
env.read_env()

OPENAI_KEY = env.str('OPENAI_KEY', '<redacted>')
