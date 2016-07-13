from ebaysdk.exception import ConnectionError
from ebaysdk.trading import Connection as Trading

from droplister_application.ebayws.utils import response_detail, write_response_to_file

appid = "CarlosFr-droplist-SBX-fab9522e2-c159ef37"

user_default_token = "AgAAAA**AQAAAA**aAAAAA**RUs/Vw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDZOLqQ6dj6x9nY+seQ**zdEDAA**AAMAAA**lsyM3SMUtQCFUvO0+Phkf8elVjgEz/wSdU6sXJQMrBiGlE13wjckf1ceZMHDRgreVOQeM87t5oMChVP5V24HtvJG2zKvmKeLWa60qAWiY427/7oE+QHHfzR6Mkea3WOWGHAQMUq7zhq5ec4UfHukAq86GGJzLF5MV+6tDjrpWp6IsRMJaQoWiff4ZBCyqyZHk+E1ZI8s+9eORSgaye4WyrPF+DB8k+RHV5B0RqNBKqGOMDfrB7Y5G3591DfTE/nPYn5FOg3RVwtrkUK7BiLdrchyfCi6CLxxe2SyXvT3VH5veDlcXbRxW5p+s0i5Hp1Uxj+5NPWGv22TBP12rjwUVY/fq447o/DyHNyPTIjYgtmxiorASYcZXFKzGpdJ41vAFiC6TXWx23/icS4ydq/Mzn0vWK8GvJh0RMqbUAYNJ73hfoK8W/z3psHTH/3cCnKfDvuYALiluwd9vB3DlJwZSysi6BOt/SjsMoNFwL4f/MGU8NtOrLprL5IwjgC7AEp+EbfSbyELyLvx2YSP9UiRpkZjuEGymRmJBqzmWGollAcLmaYfyc6fRoBPjVaI4HpITIc4f7D2L1+EuIQWb3AKqr5/A6zyk0OWq58iaDdrvFcMfMwO/xnTsmITGo7WcEf2hMQZ32grEqcP+P/2e+zVMdeD0IlrvOUEYwrLwRNtKIN6H4jGSM93/f5dgCzxdmH+N2kVPPpSXQjlBiiVYzBAOhq68LgYTsO5ll5bhYe+1xKhYUYJBmOJnLDoFvQECr9g"

testuser_lion_token = 'AgAAAA**AQAAAA**aAAAAA**GehMVw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDZOLqQ6dj6x9nY+seQ**zdEDAA**AAMAAA**lsyM3SMUtQCFUvO0+Phkf8elVjgEz/wSdU6sXJQMrBiGlE13wjckf1ceZMHDRgreVOQeM87t5oMChVP5V24HtvJG2zKvmKeLWa60qAWiY427/7oE+QHHfzR6Mkea3WOWGHAQMUq7zhq5ec4UfHukAq86GGJzLF5MV+6tDjrpWp6IsRMJaQoWiff4ZBCyqyZHk+E1ZI8s+9eORSgaye4WyrPF+DB8k+RHV5B0RqNBKqGOMDfrB7Y5G3591DfTE/nPYn5FOg3RVwtrkUK7BiLdrchyfCi6CLxxe2SyXvT3VH5veDlcXbRxW5p+s0i5Hp1Uxj+5NPWGv22TBP12rjwUVY/fq447o/DyHNyPTIjYgtmxiorASYcZXFKzGpdJ41vAFiC6TXWx23/icS4ydq/Mzn0vWK8GvJh0RMqbUAYNJ73hfoK8W/z3psHTH/3cCnKfDvuYALiluwd9vB3DlJwZSysi6BOt/SjsMoNFwL4f/MGU8NtOrLprL5IwjgC7AEp+EbfSbyELyLvx2YSP9UiRpkZjuEGymRmJBqzmWGollAcLmaYfyc6fRoBPjVaI4HpITIc4f7D2L1+EuIQWb3AKqr5/A6zyk0OWq58iaDdrvFcMfMwO/xnTsmITGo7WcEf2hMQZ32grEqcP+P/2e+zVMdeD0IlrvOUEYwrLwRNtKIN6H4jGSM93/f5dgCzxdmH+N2kVPPpSXQjlBiiVYzBAOhq68LgYTsO5ll5bhYe+1xKhYUYJBmOJnLDoFvQECr9g'


def connection(user_token=user_default_token):
    api = Trading(domain='api.sandbox.ebay.com',
                  config_file=None,
                  proxy_host="127.0.0.1", proxy_port=3128,
                  appid=appid,
                  devid="2a01f362-e81a-43b7-874c-5991127d9c80",
                  certid="SBX-ab9522e2a0f1-cd79-41b9-a955-fda2",
                  token=user_default_token)
    # token="AgAAAA**AQAAAA**aAAAAA**DFVDVw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDZaKogWdj6x9nY+seQ**zdEDAA**AAMAAA**ngXV46TF7Es/oMef4vA5L73xrHZd8F4PYknX2BudjF9dxX+YILaoi0ipWHURtoRj2P8mOBNlxi5pupEqjKyKkBxE72VfgZuTDUBpbj03p0BM4UQ5+SfNytfR5FThkvtGEPD6vHmhP2MfMfcrDrsfpIRpdCpvEohphzcRB+hlr4bzlx4JV1p/umV963wj/RifUrnpOAuo2WopRsSVO7l+Z2R1sbK5SLUrQ44L3tctCxqce7SNan0wdhPiej5vzO612IQUEVO9gq34UPCMr4p9GWshNiixyk6NU/6IzB84vq+M5C91wrNwoQ1pNhme4qbShEOsNnAMeub7m4cz1BweC1Vkv8mEIIxCV1sEEUZPCGtSf7urtoZnGnhPkbiXXpFEoNFW6koN/x1EuZPxYcTf3Za7UvUd2U6sNVgLcS4eSq2S7wJLBH8jBbGBS54FVzq9dz9KcAtUmvPGKBVw7sbFgeCtQ8JRBNWHsbLBQQTdUL6296cGgmsDmQl2zL3hBsmEEBJdhin9+upcUyv47hVF+JUtxlzF8U5XmpXPBgkKr/5k468Jvyo5BLeriHdmjWL4GS6/cP/qNM7bC1jIsUntyj5V+mRtLomM98u4zo5HdfvUKSB3HaZx2tO4sGk+y5/kgrwNJRxxrqksAV0FaZ0ct/0SEmTwEQNR240npStebg6wjNiYoZXNVyYiOEsmklKeEfbud5G6eUK+OO/HZb2V479hLDsJA48fzz3wcvlXINQnLqIx2ehnovOKt7THxFv/")
    return api


def get_user_detail(token):
    try:
        api = connection(user_token=token)
        action = 'GetUser'
        response = api.execute(action, {})
        response_detail(response)
        write_response_to_file(response, action)


    except ConnectionError as e:
        print(e)
        print(e.response.dict())


def getcategories():
    action = 'GetCategories'
    api = connection()
    response = api.execute(action, {'CategorySiteID': 186, 'DetailLevel': 'ReturnAll'})
    response_detail(response)
    write_response_to_file(response, action)


def getsuggestedcategories():
    action = 'GetSuggestedCategories'
    api = connection()
    response = api.execute(action, {'query': 'book'})
    response_detail(response)
    write_response_to_file(response, action)


def getitem():
    action = 'GetItem'
    itemid = '110178441866'
    api = connection()
    response = api.execute(action, {'itemID': itemid})
    response_detail(response)
    write_response_to_file(response, action)


"""
        <Title>Harry Potter and the Philosopher's Stone</Title>
        <Description>
            This is the first book in the Harry Potter series. In excellent condition!
        </Description>
        <PrimaryCategory>
            <CategoryID>377</CategoryID>
        </PrimaryCategory>
        <StartPrice>1.0</StartPrice>
        <CategoryMappingAllowed>true</CategoryMappingAllowed>
        <ConditionID>4000</ConditionID>
        <Country>US</Country>
        <Currency>USD</Currency>
        <DispatchTimeMax>3</DispatchTimeMax>
        <ListingDuration>Days_7</ListingDuration>
        <ListingType>Chinese</ListingType>
        <PaymentMethods>PayPal</PaymentMethods>
        <PayPalEmailAddress>magicalbookseller@yahoo.com</PayPalEmailAddress>
        <PictureDetails>
            <PictureURL>http://pics.ebay.com/aw/pics/dot_clear.gif</PictureURL>
        </PictureDetails>
        <PostalCode>95125</PostalCode>
        <Quantity>1</Quantity>
        <ReturnPolicy>
            <ReturnsAcceptedOption>ReturnsAccepted</ReturnsAcceptedOption>
            <RefundOption>MoneyBack</RefundOption>
            <ReturnsWithinOption>Days_30</ReturnsWithinOption>
            <Description>If you are not satisfied, return the book for refund.</Description>
            <ShippingCostPaidByOption>Buyer</ShippingCostPaidByOption>
        </ReturnPolicy>
        <ShippingDetails>
            <ShippingType>Flat</ShippingType>
            <ShippingServiceOptions>
                <ShippingServicePriority>1</ShippingServicePriority>
                <ShippingService>USPSMedia</ShippingService>
                <ShippingServiceCost>2.50</ShippingServiceCost>
            </ShippingServiceOptions>
        </ShippingDetails>
        <Site>US</Site>
"""


def addItem():
    myitem = {
        "Item": {
            "Title": "Harry Potter and the Philosopher's Stone",
            "Description": "This is the first book in the Harry Potter series. In excellent condition!",
            "PrimaryCategory": {"CategoryID": "377"},
            "StartPrice": "1.0",
            "CategoryMappingAllowed": "true",
            "Country": "US",
            "ConditionID": "3000",
            "Currency": "USD",
            "DispatchTimeMax": "3",
            "ListingDuration": "Days_7",
            "ListingType": "Chinese",
            "PaymentMethods": "PayPal",
            # "PayPalEmailAddress": "allforyouint@hotmail.com",
            "PayPalEmailAddress": "andrydiaz@hotmail.com",
            "PictureDetails": {"PictureURL": "http://i1.sandbox.ebayimg.com/03/i/00/30/07/20_1.JPG?set_id=8800005007"},
            "PostalCode": "95125",
            "Quantity": "1",
            "ReturnPolicy": {
                "ReturnsAcceptedOption": "ReturnsAccepted",
                "RefundOption": "MoneyBack",
                "ReturnsWithinOption": "Days_30",
                "Description": "If you are not satisfied, return the book for refund.",
                "ShippingCostPaidByOption": "Buyer"
            },
            "ShippingDetails": {
                "ShippingType": "Flat",
                "ShippingServiceOptions": {
                    "ShippingServicePriority": "1",
                    "ShippingService": "USPSMedia",
                    "ShippingServiceCost": "2.50"
                }
            },
            "Site": "US"
        }
    }
    api = connection()

    api.execute('VerifyAddItem', myitem)

    print("%s" % api.response.content)

    # response = api.execute(action, itemDict)
    # response_detail(response)


runame = "Carlos_Franciso-CarlosFr-dropli-hcoxi"


def getSesionID():
    api = connection()
    response = api.execute('GetSessionID', {"RuName": runame})
    response_detail(response)
    session_id = response.reply.SessionID
    print("%s - %s" % (api.response.content, session_id))
    print "Visit: https://signin.sandbox.ebay.com/ws/eBayISAPI.dll?SignIn&RuName=%s&SessID=%s" % (runame, session_id)
    return session_id


def getTokenXSessionID(sessionID):
    print "Fetching token with Session ID %s" % sessionId
    api = connection()
    response = api.execute('FetchToken', {"SessionID": sessionID})
    response_detail(response)
    return response.reply.eBayAuthToken, response.reply.HardExpirationTime
    # return response.reply.SessionID


def test_user_interactivity():
    global sessionId
    sessionId = getSesionID()
    raw_input("Proceed?")
    getTokenXSessionID(sessionId)


def GetMyeBaySelling(token):
    api = connection(user_token=token)
    response = api.execute('GetMyeBaySelling', {"ActiveList": {'Include': "true"}})
    response_detail(response)
    write_response_to_file(response, 'GetMyeBaySelling')


def GetOrders(token):
    api = connection(user_token=token)
    response = api.execute('GetOrders', {'NumberOfDays': 30})
    response_detail(response)
    write_response_to_file(response, 'GetOrders')


def GetStore(token):
    api = connection(user_token=token)
    response = api.execute('GetStore', {'CategoryStructureOnly': 'True'})
    response_detail(response)
    write_response_to_file(response, 'GetStore')


if __name__ == '__main__':
    print "Running...."
    # getcategories()
    # get_user_detail(testuser_lion_token)
    # getsuggestedcategories()
    # getitem()
    # add_item()
    # test_user_interactivity()
    # GetMyeBaySelling(testuser_lion_token)
    # GetOrders(testuser_lion_token)
    GetStore(testuser_lion_token)