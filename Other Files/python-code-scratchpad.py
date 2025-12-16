import json
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

radius_server_list = json.loads("[{\"caCertificate\":null,\"host\":\"10.0.30.241\",\"id\":\"585467951558637934\",\"openRoamingCertificateId\":null,\"port\":1812,\"radsecEnabled\":false},{\"caCertificate\":null,\"host\":\"10.1.2.3\",\"id\":\"585467951558637952\",\"openRoamingCertificateId\":null,\"port\":1812,\"radsecEnabled\":false}]")
wireless_ap_list = json.loads("[{\"address\": \"16200 Quarry Hill Dr, Parker, CO 80134\", \"details\": [], \"firmware\": \"wireless-32-1-5\", \"floorPlanId\": null, \"lanIp\": \"10.0.0.210\", \"lat\": 39.5298, \"lng\": -104.80381, \"mac\": \"cc:6e:2a:5f:49:f0\", \"model\": \"CW9176I\", \"name\": \"CW9176-1\", \"networkId\": \"L_585467951558186073\", \"serial\": \"Q5BK-7WHM-4MUB\", \"tags\": [], \"url\": \"https://n40.dashboard.meraki.com/Adams-Office-wir/n/5z4cNaO/manage/nodes/new_list/224773529356784\"}]")

url = "https://" + radius_server_list[0]['host'] + "/ers/config/networkdevice"

payload = {}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

response = requests.request("GET", url, headers=headers, auth=('ers_admin', 'Blkmc1mtr!'), data=payload, verify=False)

response_json = json.loads(response.text)

print(response_json["SearchResult"]["resources"][0]["name"])

