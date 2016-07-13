# from ebaysdk.trading import Connection as Trading
#
# appid = "CarlosFr-droplist-SBX-fab9522e2-c159ef37"
#
# def connection():
#     api = Trading(domain='api.sandbox.ebay.com',
#                   config_file=None,
#                   proxy_host="127.0.0.1", proxy_port=3128,
#                   appid=appid,
#                   devid="2a01f362-e81a-43b7-874c-5991127d9c80",
#                   certid="SBX-ab9522e2a0f1-cd79-41b9-a955-fda2",
#                   token="AgAAAA**AQAAAA**aAAAAA**RUs/Vw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDZOLqQ6dj6x9nY+seQ**zdEDAA**AAMAAA**lsyM3SMUtQCFUvO0+Phkf8elVjgEz/wSdU6sXJQMrBiGlE13wjckf1ceZMHDRgreVOQeM87t5oMChVP5V24HtvJG2zKvmKeLWa60qAWiY427/7oE+QHHfzR6Mkea3WOWGHAQMUq7zhq5ec4UfHukAq86GGJzLF5MV+6tDjrpWp6IsRMJaQoWiff4ZBCyqyZHk+E1ZI8s+9eORSgaye4WyrPF+DB8k+RHV5B0RqNBKqGOMDfrB7Y5G3591DfTE/nPYn5FOg3RVwtrkUK7BiLdrchyfCi6CLxxe2SyXvT3VH5veDlcXbRxW5p+s0i5Hp1Uxj+5NPWGv22TBP12rjwUVY/fq447o/DyHNyPTIjYgtmxiorASYcZXFKzGpdJ41vAFiC6TXWx23/icS4ydq/Mzn0vWK8GvJh0RMqbUAYNJ73hfoK8W/z3psHTH/3cCnKfDvuYALiluwd9vB3DlJwZSysi6BOt/SjsMoNFwL4f/MGU8NtOrLprL5IwjgC7AEp+EbfSbyELyLvx2YSP9UiRpkZjuEGymRmJBqzmWGollAcLmaYfyc6fRoBPjVaI4HpITIc4f7D2L1+EuIQWb3AKqr5/A6zyk0OWq58iaDdrvFcMfMwO/xnTsmITGo7WcEf2hMQZ32grEqcP+P/2e+zVMdeD0IlrvOUEYwrLwRNtKIN6H4jGSM93/f5dgCzxdmH+N2kVPPpSXQjlBiiVYzBAOhq68LgYTsO5ll5bhYe+1xKhYUYJBmOJnLDoFvQECr9g")
#     # token="AgAAAA**AQAAAA**aAAAAA**DFVDVw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDZaKogWdj6x9nY+seQ**zdEDAA**AAMAAA**ngXV46TF7Es/oMef4vA5L73xrHZd8F4PYknX2BudjF9dxX+YILaoi0ipWHURtoRj2P8mOBNlxi5pupEqjKyKkBxE72VfgZuTDUBpbj03p0BM4UQ5+SfNytfR5FThkvtGEPD6vHmhP2MfMfcrDrsfpIRpdCpvEohphzcRB+hlr4bzlx4JV1p/umV963wj/RifUrnpOAuo2WopRsSVO7l+Z2R1sbK5SLUrQ44L3tctCxqce7SNan0wdhPiej5vzO612IQUEVO9gq34UPCMr4p9GWshNiixyk6NU/6IzB84vq+M5C91wrNwoQ1pNhme4qbShEOsNnAMeub7m4cz1BweC1Vkv8mEIIxCV1sEEUZPCGtSf7urtoZnGnhPkbiXXpFEoNFW6koN/x1EuZPxYcTf3Za7UvUd2U6sNVgLcS4eSq2S7wJLBH8jBbGBS54FVzq9dz9KcAtUmvPGKBVw7sbFgeCtQ8JRBNWHsbLBQQTdUL6296cGgmsDmQl2zL3hBsmEEBJdhin9+upcUyv47hVF+JUtxlzF8U5XmpXPBgkKr/5k468Jvyo5BLeriHdmjWL4GS6/cP/qNM7bC1jIsUntyj5V+mRtLomM98u4zo5HdfvUKSB3HaZx2tO4sGk+y5/kgrwNJRxxrqksAV0FaZ0ct/0SEmTwEQNR240npStebg6wjNiYoZXNVyYiOEsmklKeEfbud5G6eUK+OO/HZb2V479hLDsJA48fzz3wcvlXINQnLqIx2ehnovOKt7THxFv/")
#     return api
#
#
# def getRuname():
#     return "Carlos_Franciso-CarlosFr-dropli-hcoxi"
#
#
# def getSesionID():
#     api = connection()
#     response = api.execute('GetSessionID', {"RuName": getRuname()})
#     return response.reply.SessionID


def response_detail(response, echo=True):
    attrs = vars(response)
    details = '\n'.join("%s: %s" % item for item in attrs.items())
    if echo:
        print details
    return details


def write_response_to_file(response, filename, ext=".text"):
    file = open(filename + ext, 'w')
    file.write(response_detail(response, echo=False))
    file.flush()
    file.close()