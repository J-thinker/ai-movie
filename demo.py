# -*- coding: UTF-8 -*-
import requests
import re
import time
import base64
import json
data = resp_data['data']
atob_data_1 = base64.urlsafe_b64decode(data.encode())
atob_data_2 = base64.urlsafe_b64decode(atob_data_1)
atob_data_3 = base64.urlsafe_b64decode(atob_data_2)

print(atob_data_3)