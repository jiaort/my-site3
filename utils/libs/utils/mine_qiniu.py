# -*- coding: utf-8 -*-

from uuid import uuid4
from qiniu import Auth, put_data


# 需要填写你的 Access Key 和 Secret Key
access_key = 'r5O7ETO-aXn6EejQSKb3j_j-WeImHLFcjZZ9i0Bj'
secret_key = 'nTCQFVtjHAG5cDW-k2M_twnYrx0u_--ZrF55_S7B'
domain_prefix = 'http://img.sndz.top/'


def upload_data(filestream, bucket_name):
    # 生成上传凭证
    q = Auth(access_key, secret_key)
    suffix = filestream.name.split('.')[-1]  # 后缀(jpg, png, gif)

    filename = uuid4().get_hex() + '.' + suffix.lower()
    token = q.upload_token(bucket_name, filename)
    # 上传文件
    retData, respInfo = put_data(token, filename, filestream)

    return filename, domain_prefix + filename
