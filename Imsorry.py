import time
import requests




class Node:
    def __init__(self, data = None):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

keyList = LinkedList()
i = 0

keyList.head = Node("OlWVWVP8pfnu8XsqigM5WYJz965MGJtR")
key2 = Node("4blZSQnKgGprGonJdhdEGw3WDwGhctIB")
key3 = Node("0WjncFhCJfnDxsdVeieZoMbNa3fozIeR")
key4 = Node("sJIlGv8ntthrpxpW1ztT3NCzeFf21Ins")
key5 = Node("xyy66Y0aWMt7b0s1iQrHAKorSvHCuxZS")

keyList.head.next = key2
key2.next = key3
key3.next = key4
key4.next = key5
key5.next = keyList.head

currentNode = keyList.head
  
  
stupid_rate = "policies.ratelimit.QuotaViolation"
  
    
while True:
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key={}&page={}'.format(currentNode.data,  i)
    response = requests.get(url)
    response_json = response.json()
    print(i)
    if "fault" in list(response_json):
        currentNode = currentNode.next
        print(currentNode.data)
    else:
        print(response_json["response"]["docs"][0]["web_url"])
        i+=1


    
    