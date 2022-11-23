from settings import base
import sys

SECRET_KEY = ""

DEBUG = False

ALLOWED_HOSTS = ['.us-east-1.elasticbeanstalk.com','172.31.40.213']

def main():
    SECRET_KEY = sys.argv[0]

if __name__ == '__main__':
    main()