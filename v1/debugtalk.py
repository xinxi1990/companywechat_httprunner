import json
import os
import random
import string
import time
import configparser
import csv

# from testcases.api_server import HTTPBIN_SERVER, SECRET_KEY, gen_md5, get_sign

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

auto_cfg_path = PATH("../v1/config/auto.cfg")
file_path = PATH("../v1/file.csv")


BASE_URL = "http://127.login.login.1:5000"
# UserName = os.environ['UserName']




demo_default_request = {
    "base_url": "$BASE_URL",
    "headers": {
        "content-type": "application/json"
    }
}

def sum_two(m, n):
    return m + n

def sum_status_code(status_code, expect_sum):
    """ sum status code digits
        e.g. 400 => 4, 201 => 3
    """
    sum_value = 0
    for digit in str(status_code):
        sum_value += int(digit)

    assert sum_value == expect_sum

def is_status_code_200(status_code):
    return status_code == 200

os.environ["TEST_ENV"] = "PRODUCTION"

def skip_test_in_production_env():
    """ skip this test in production environment
    """
    return os.environ["TEST_ENV"] == "PRODUCTION"

def gen_app_version():
    return [
        {"app_version": "2.8.5"},
        {"app_version": "2.8.6"}
    ]

def get_account():
    return [
        {"username": "user1", "password": "111111"},
        {"username": "user2", "password": "222222"}
    ]

def gen_random_string(str_len):
    random_char_list = []
    for _ in range(str_len):
        random_char = random.choice(string.ascii_letters + string.digits)
        random_char_list.append(random_char)

    random_string = ''.join(random_char_list)
    return random_string

def setup_hook_add_kwargs(request):
    request["key"] = "value"

def setup_hook_remove_kwargs(request):
    request.pop("key")

def teardown_hook_sleep_N_secs(response, n_secs):
    """ sleep n seconds after request
    """
    if response.status_code == 200:
        time.sleep(0.1)
    else:
        time.sleep(n_secs)

def hook_print(msg):
    print(msg)

def modify_headers_os_platform(request, os_platform):
    request["headers"]["os_platform"] = os_platform

def setup_hook_httpntlmauth(request):
    if "httpntlmauth" in request:
        from requests_ntlm import HttpNtlmAuth
        auth_account = request.pop("httpntlmauth")
        request["auth"] = HttpNtlmAuth(
            auth_account["username"], auth_account["password"])

def alter_response(response):
    response.status_code = 500
    response.headers["Content-Type"] = "html/text"
    response.json["headers"]["Host"] = "127.login.login.1:8888"
    response.new_attribute = "new_attribute_value"
    response.new_attribute_dict = {
        "key": 123
    }

def alter_response_error(response):
    # NameError
    not_defined_variable


def read_config(cfg_file):
    cfg = configparser.ConfigParser()
    cfg.read(cfg_file)
    return cfg

l_c = read_config(auto_cfg_path)


def get_token_url():
    return l_c.get('corp_para', 'token_url')

def get_cord_id():
    return l_c.get('corp_para', 'corp_id')

def get_secure():
    return l_c.get('contact_para', 'secure')

def get_name_id():
    print(get_name_id)
    '''
    get name and id parameters
    :return:
    '''
    return [
        {"name": "p_1","id": "111"},
        {"name": "p_2", "id": "222"},
        {"name": "p_3", "id": "333"},
    ]


def teardown_hook_write_file(response):
    """ write some str after request
    """
    print("teardown_hook_write_file")
    if response.status_code == 200:
        department_id_list = []
        for index in response.json['department']:
            department_id_list.append([(index)['id']])
        with open(file_path, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["department_id"])
            writer.writerows(department_id_list)













