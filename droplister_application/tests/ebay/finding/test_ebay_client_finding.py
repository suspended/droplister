from ebaysdk.shopping import Connection as Shoping

from droplister_application.tests.ebay.utils import response_detail, write_response_to_file


def connection():
    api = Shoping(#domain='api.sandbox.ebay.com',
                  config_file=None,
                  proxy_host="127.0.0.1", proxy_port=3128, debug=True,
                  appid="CarlosFr-droplist-SBX-fab9522e2-c159ef37",
                  devid="2a01f362-e81a-43b7-874c-5991127d9c80",
                  certid="SBX-ab9522e2a0f1-cd79-41b9-a955-fda2",
                  token="AgAAAA**AQAAAA**aAAAAA**DFVDVw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDZaKogWdj6x9nY+seQ**zdEDAA**AAMAAA**ngXV46TF7Es/oMef4vA5L73xrHZd8F4PYknX2BudjF9dxX+YILaoi0ipWHURtoRj2P8mOBNlxi5pupEqjKyKkBxE72VfgZuTDUBpbj03p0BM4UQ5+SfNytfR5FThkvtGEPD6vHmhP2MfMfcrDrsfpIRpdCpvEohphzcRB+hlr4bzlx4JV1p/umV963wj/RifUrnpOAuo2WopRsSVO7l+Z2R1sbK5SLUrQ44L3tctCxqce7SNan0wdhPiej5vzO612IQUEVO9gq34UPCMr4p9GWshNiixyk6NU/6IzB84vq+M5C91wrNwoQ1pNhme4qbShEOsNnAMeub7m4cz1BweC1Vkv8mEIIxCV1sEEUZPCGtSf7urtoZnGnhPkbiXXpFEoNFW6koN/x1EuZPxYcTf3Za7UvUd2U6sNVgLcS4eSq2S7wJLBH8jBbGBS54FVzq9dz9KcAtUmvPGKBVw7sbFgeCtQ8JRBNWHsbLBQQTdUL6296cGgmsDmQl2zL3hBsmEEBJdhin9+upcUyv47hVF+JUtxlzF8U5XmpXPBgkKr/5k468Jvyo5BLeriHdmjWL4GS6/cP/qNM7bC1jIsUntyj5V+mRtLomM98u4zo5HdfvUKSB3HaZx2tO4sGk+y5/kgrwNJRxxrqksAV0FaZ0ct/0SEmTwEQNR240npStebg6wjNiYoZXNVyYiOEsmklKeEfbud5G6eUK+OO/HZb2V479hLDsJA48fzz3wcvlXINQnLqIx2ehnovOKt7THxFv/")
    return api


def find_items(query):
    action = 'getVersion'
    api = connection()
    api_request = {
        # 'keywords': u'ni',
        'keywords': u'book',
        # 'itemFilter': [
        #     {'name': 'Condition',
        #      'value': 'Used'},
        #     {'name': 'LocatedIn',
        #      'value': 'GB'},
        # ],
        # 'affiliate': {'trackingId': 1},
        # 'sortOrder': 'CountryDescending',
    }
    response = api.execute(action)
    response_detail(response)


if __name__ == '__main__':
    find_items('book')
