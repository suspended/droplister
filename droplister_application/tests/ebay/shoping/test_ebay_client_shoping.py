from ebaysdk.shopping import Connection as Shoping


def connection():
    api = Shoping(domain='api.sandbox.ebay.com', config_file=None,
                  proxy_host="127.0.0.1", proxy_port=3128, debug=True,
                  appid="CarlosFr-droplist-SBX-fab9522e2-c159ef37",
                  devid="2a01f362-e81a-43b7-874c-5991127d9c80",
                  certid="SBX-ab9522e2a0f1-cd79-41b9-a955-fda2",
                  token="AgAAAA**AQAAAA**aAAAAA**RUs/Vw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDZOLqQ6dj6x9nY+seQ**zdEDAA**AAMAAA**lsyM3SMUtQCFUvO0+Phkf8elVjgEz/wSdU6sXJQMrBiGlE13wjckf1ceZMHDRgreVOQeM87t5oMChVP5V24HtvJG2zKvmKeLWa60qAWiY427/7oE+QHHfzR6Mkea3WOWGHAQMUq7zhq5ec4UfHukAq86GGJzLF5MV+6tDjrpWp6IsRMJaQoWiff4ZBCyqyZHk+E1ZI8s+9eORSgaye4WyrPF+DB8k+RHV5B0RqNBKqGOMDfrB7Y5G3591DfTE/nPYn5FOg3RVwtrkUK7BiLdrchyfCi6CLxxe2SyXvT3VH5veDlcXbRxW5p+s0i5Hp1Uxj+5NPWGv22TBP12rjwUVY/fq447o/DyHNyPTIjYgtmxiorASYcZXFKzGpdJ41vAFiC6TXWx23/icS4ydq/Mzn0vWK8GvJh0RMqbUAYNJ73hfoK8W/z3psHTH/3cCnKfDvuYALiluwd9vB3DlJwZSysi6BOt/SjsMoNFwL4f/MGU8NtOrLprL5IwjgC7AEp+EbfSbyELyLvx2YSP9UiRpkZjuEGymRmJBqzmWGollAcLmaYfyc6fRoBPjVaI4HpITIc4f7D2L1+EuIQWb3AKqr5/A6zyk0OWq58iaDdrvFcMfMwO/xnTsmITGo7WcEf2hMQZ32grEqcP+P/2e+zVMdeD0IlrvOUEYwrLwRNtKIN6H4jGSM93/f5dgCzxdmH+N2kVPPpSXQjlBiiVYzBAOhq68LgYTsO5ll5bhYe+1xKhYUYJBmOJnLDoFvQECr9g")
    return api



if __name__ == '__main__':
    pass
