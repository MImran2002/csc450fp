from flask import Flask
import requests


app = Flask(__name__)

ip_address ="34.210.108.54"
cve_check = f"https://internetdb.shodan.io/{ip_address}"
cve_get = requests.get(cve_check)
print(cve_get)
cve_json = cve_get.json()
print(cve_json)
cve_vulns = cve_json["vulns"]
print(cve_vulns)
cve_id = cve_vulns[0]
cve_db = f"https://cve.circl.lu/api/cve/{cve_id}"
db_get = requests.get(cve_db)
db_json = db_get.json()
print(db_json)
db_json = db_json["capec"]
db_json = db_json[0]
attack_name = db_json["name"]
pre_req = db_json["prerequisites"]
sol = db_json["solutions"]
sum = db_json["summary"]

@app.route('/')
def hello_world():
    return f'The following website has the following cyber vulnerability: {attack_name} \n\n prerequiste: {pre_req} \n\n solution: {sol} \n\n summary: {sum}' 

if __name__ == '__main__':
    app.run(debug=True)


