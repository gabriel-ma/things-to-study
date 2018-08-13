import requests
r = requests.post("https://www.nappy.co/wp-admin/admin-ajax.php", data={'action': 'pd_load_more', 'type': 'issue'})
print(r.status_code, r.reason)