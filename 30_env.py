import os
from dotenv import load_dotenv

# pip install python-dotenv

load_dotenv()
test_api_key = os.getenv('TEST_API_KEY')
# test_api_key = os.environ.get('TEST_API_KEY')
print(test_api_key)

# os.environ['TEST_API_KEY'] = '5432fdref354yt544r32'

