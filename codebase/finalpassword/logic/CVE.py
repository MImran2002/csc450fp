import requests

ip_address ="199.60.103.226"
cve_check = f"https://internetdb.shodan.io/{ip_address}"
cve_get = requests.get(cve_check)
cve_json = cve_get.json()
cve_vulns = cve_json["vulns"]
cve_id = cve_vulns[0]
cve_db = f"https://cve.circl.lu/api/cve/{cve_id}"
db_get = requests.get(cve_db)
db_json = db_get.json()



