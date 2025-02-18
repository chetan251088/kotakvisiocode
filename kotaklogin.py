import requests
import json

class kotaklogin:

    def main(self):
        accesstoken = self.zgentokenthread()
        id,token,hsid,tokensam = self.login()
        # id,token,hsid = self.login()
        with open("cred.json", "w") as f:
            # json.dump({"token": token, "id": id, "hsid": hsid, "accesstoken": accesstoken,"tokensam":"0b694ce2a836ca324b49f5ad69cdf68c"}, f)    
            json.dump({"token": token, "id": id, "hsid": hsid, "accesstoken": accesstoken,"tokensam":tokensam}, f)   

    def zgentokenthread(self):
            global sub, tok, sid,accesstoken

            # consumer_key = "CDmsSH32py2cbf30vcRNLCad_owa"
            # consumer_secret = "r8hB5TtSjrpHXfYIcdfdPXgBTGoa"
            urlAT = "https://napi.kotaksecurities.com/oauth2/token"
            data = {"grant_type":"password","username": "client350", "password": "MWPhe9Ar"}
            form_data = {
                    "grant_type": "password",
                    "username": "client350",
                    "password": "MWPhe9Ar"
                    }
            #usrPass = consumer_key+':'+consumer_secret
            #encoded_u = base64.b64encode(usrPass.encode()).decode()
            headers = {"Content-Type": "application/x-www-form-urlencoded","Authorization" : "Basic Q0Rtc1NIMzJweTJjYmYzMHZjUk5MQ2FkX293YTpyOGhCNVR0U2pycEhYZllJY2RmZFBYZ0JUR29h"} #Base64 encoded string entered here manually generated
            #b64Val = base64.b64encode(usrPass)
            r=requests.post(urlAT, headers=headers,data=form_data)
            #r = requests.post(urlAT, headers=HTTPBasicAuth('CDmsSH32py2cbf30vcRNLCad_owa', 'r8hB5TtSjrpHXfYIcdfdPXgBTGoa'), data=json.dumps(data))
            Acc_token = r.json()
            #eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQzNTAiLCJhdXQiOiJBUFBMSUNBVElPTl9VU0VSIiwiYXVkIjoiQ0Rtc1NIMzJweTJjYmYzMHZjUk5MQ2FkX293YSIsIm5iZiI6MTcwNDYxNzgzMiwiYXpwIjoiQ0Rtc1NIMzJweTJjYmYzMHZjUk5MQ2FkX293YSIsInNjb3BlIjoiZGVmYXVsdCIsImlzcyI6Imh0dHBzOlwvXC9uYXBpLmtvdGFrc2VjdXJpdGllcy5jb206NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjozNjE3MDQ2MTc4MzIsImlhdCI6MTcwNDYxNzgzMiwianRpIjoiZGM3YmI3ZGYtNDhiOS00MGI1LTllNmYtZmUwN2VhNDJkZTA4In0.H6RbjYBLG-l5vv3JZORNQIde3LdTzMgwQNz887GMg-YEAEhtTvtnh2RjEgwpG8e3Kv1ixZLu4MC5JFE7saUA5vbfxU_dp5F9i0-zGc3lqGgCRlUuVCQnRrxl6KfDz_bfh_HlHqsx7s47EDfhSeKMr3cz158DQBk9dFcgBFesENeClXSLWC_02aRoY48gKAQr4RHR8JhHqBpu1epiGqmDQbjOXFzTxl7EyWamLEDAgnmFa7qbdfLRlHd2JIgMkHmJZbsMnZA97nxSEuj5nHpz_Q9LHmTdPZgacIf3XqF1dmtDbD2bx7dWCTEDbjT0QigwQD5y3J3zuJlufRtxXuZYXg
            # accesstoken = 'eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQzNTAiLCJhdXQiOiJBUFBMSUNBVElPTl9VU0VSIiwiYXVkIjoiQ0Rtc1NIMzJweTJjYmYzMHZjUk5MQ2FkX293YSIsIm5iZiI6MTcwNDYxODgzMCwiYXpwIjoiQ0Rtc1NIMzJweTJjYmYzMHZjUk5MQ2FkX293YSIsInNjb3BlIjoiZGVmYXVsdCIsImlzcyI6Imh0dHBzOlwvXC9uYXBpLmtvdGFrc2VjdXJpdGllcy5jb206NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjozNjE3MDQ2MTg4MzAsImlhdCI6MTcwNDYxODgzMCwianRpIjoiZTY4ZjhmNmMtYzViNy00NGQyLWIzZWMtNDc5ZDNmNWI1YzI5In0.GCgHpzR4ZxJKj1fqgRKt1jaem8idwVhjQGmphHKABgWIJpnTouXdwDukQsj1AgsEfojHEC-ZF4qeJC8fPYoFdZcAUiHoSYr1LE6CPQyahwthj-52FSJQpUjxrtMCD2sHK0jvRDr6rV_ZSEPsNcsU7B9vrzFIV2uB5OKQn7o1EjYPHiklM8eVJpKY_p4Jow3hQirPmVAsN8aXJ1gLvPDBaL6uBM39PB2-6p3iS0LcvnPEn8UDXrVlunPCGlD7Rc3rGwkNE1HQgoJBKIn-O9AliCmdNmMxLaSjnraiYvRN3Gv7Xnja98e_dZGisLX0jDkOba6R1Qrl1FdQ5MOK1MCi3A'
            accesstoken = Acc_token["access_token"]
            print(r.text)
            print(accesstoken)
            return accesstoken    

        # def zgentoken(self):
        #     t = threading.Thread(target=self.zgentokenthread)
        #     t.start()

    def login(self):
        global newtoken, newsid, newhsServerId, tokensam
        url = "https://gw-napi.kotaksecurities.com/login/1.0/login/v2/validate"
        # Set up request headers
        headers = {
            "accept":"*/*",
            "Content-Type": "application/json",
            "Authorization": "Bearer "+ accesstoken
        }
        try:
            # JSON data to send in request body
            data = {"mobileNumber": "+917019899942", "password": "Twinkie24@"}

            # Send POST request to first step login API
            response = requests.post(url, headers=headers, data=json.dumps(data))

            # Extract token and sid values from JSON response
            #token = response.json().get("token")
            #sid = response.json().get("sid")

            # Extract the 'token' and 'sid' values from the response
            json_data = response.json()
            token = json_data.get("data", {}).get("token")
            sid = json_data.get("data", {}).get("sid")
            print("first call sid", sid)
            print("first call kotak token", token)
            
            # Second step login API URL
            #second_step_url = "https://example.com/api/login/twofactor"

            # Prepare headers for second step login API
            second_step_headers =  {
                "Content-Type": "application/json",
                "Sid":sid,
                #"Auth":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJUcmFkZSJdLCJleHAiOjE2OTQxOTc4MDAsImp0aSI6ImU3ZWRlMjEzLWYzNzItNDhhOC1iZjEzLTMyY2I4ZDJjYWM3NyIsImlhdCI6MTY5NDE0MTM4NywiaXNzIjoibG9naW4tc2VydmljZSIsInN1YiI6ImIwNDQ1YWRkLTM5N2QtNDlmYS04NWYxLWRmZWIwNDcwNzk2NCIsInVjYyI6IllRUkNUIiwibmFwIjoiRVNCUE01NTQxUiIsImZldGNoY2FjaGluZ3J1bGUiOjAsImNhdGVnb3Jpc2F0aW9uIjoiIn0.SOP4JOOnjre1eVZ3L0QEbBzO-I0mpdDCcY_zT2un39-lfIF8fwCGk4-BkKN0d-3k7p4QeCrCxqFKl0gabH-IQmIXnOXCnPFRNg4wv7WxS6UhT4VnoJsr_cJvOPnXbDjeBkpjH3r8_StXNPNQgBR-qeTD6cAzmDG6h4rp6GCtbABji8p1btQ4ieCC9NNAIgRjZFrl0mOnuYv_arYGgAsHuvRDUcfoxYK24U76PgRzfvGQSlpeAhrUlJspwbJzYalrWGjateY1Ri4QnJFw-KNmw9kMlfDPG6RyKNj0BDbF0b48vGKk2vJXJmt57AiU0drB_gqfKDV7S_fvWBgmDxiOjw",
                "Auth":token,
                "neo-fin-key":"neotradeapi",
                "accept":"application/json",
                #"Authorization": "Bearer eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQzNTAiLCJhdXQiOiJBUFBMSUNBVElPTl9VU0VSIiwiYXVkIjoiQ0Rtc1NIMzJweTJjYmYzMHZjUk5MQ2FkX293YSIsIm5iZiI6MTY5NDQwNjIxMiwiYXpwIjoiQ0Rtc1NIMzJweTJjYmYzMHZjUk5MQ2FkX293YSIsInNjb3BlIjoiZGVmYXVsdCIsImlzcyI6Imh0dHBzOlwvXC9uYXBpLmtvdGFrc2VjdXJpdGllcy5jb206NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjozNjE2OTQ0MDYyMTIsImlhdCI6MTY5NDQwNjIxMiwianRpIjoiNmU1N2VkYmEtZGI1YS00OGEzLWFiMTgtNmNjNGI0NjBmZTc2In0.evj9Rhsz-NXmtUFTWox6r6_ACfel1YTrYFUiRr5tZFv3d15eecMDTXcu21OQDsfnDiQc-P8itQECiLROLj_Ly00ytdelZdJwjTZPRQiUwI-JeuF2ZU3hZ0gMrLH76YOGMJ9QIPtDAk-xGFRPia1KmQfdn41utfaaPqIrz3QwmYHOE2__pHjx4HczlGdXepxwCTKJJo4YuiwjRlziPzyGdmlj6_ttuT-eM5LdR9ateq9D-hiJvs0Qe37rpUV1BiIFPTSJuWh6QMKjlwaFNYiRGy2xTuIuhDPv_v0eG7h_d6Ra4chELwVz60PjyvQr12Tb3GBv3Qqp0MM_V8GZBmrGEQ"
                "Authorization": "Bearer "+ accesstoken
            }
            print('sec headres',second_step_headers)
            # Prepare JSON data for second step login API
            second_step_data = {"userId": "b0445add-397d-49fa-85f1-dfeb04707964","mpin": "252811"}

            # Send POST request to second step login API
            second_step_response = requests.post(url, headers=second_step_headers, data=json.dumps(second_step_data))

            # Check if second step login successful
            #if second_step_response.status_code == 200:
                # Login successful
            json_data1 = second_step_response.json()
            newtoken=json_data1.get("data", {}).get("token")
            newsid=json_data1.get("data", {}).get("sid")
            newhsServerId=json_data1.get("data", {}).get("hsServerId")
            print("second call sid",newsid)
            print("second call kotak token",newtoken)
            print("second call newhsServerId",newhsServerId)
            print("success")

            #Set up samco request headers
            headerssamco = {
                "Content-Type": "application/json"}
            data = {"userId": "DC4247", "password": "samco2024@", "yob": "1988"}
            #'data=%7B%22userId%22%3A%20%22DC4247%22%2C%20%22password%22%3A%20%22samco2024!%22%2C%20%22yob%22%3A%20%221988%22%7D'              url encoded string
            urlsamco="https://api.stocknote.com/login"
            # Send POST request to first step login API
            responsesam = requests.post(urlsamco, headers=headerssamco, data=json.dumps(data))

            # Extract token and sid values from JSON response
            #token = response.json().get("token")
            #sid = response.json().get("sid")

            # Extract the 'token' and 'sid' values from the response
            json_datasam = responsesam.json()
            tokensam = json_datasam["sessionToken"]
            # tokensam = "4e7fa320423036678a8cd0da3b477807"
            # token = json_data.get("data", {}).get("sessionToken")
            print("first call samco token", tokensam)    

        except Exception as e:
            print("Exception while connection to login apis ->socket: %s\n" % e)
        return  newsid, newtoken,  newhsServerId ,tokensam
    
if __name__ == "__main__":
    my_object = kotaklogin()
    my_object.main() 
        