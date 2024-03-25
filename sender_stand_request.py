import requests
import configuration
import datat
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=datat.headers)
response = post_products_kits(datat.product_ids)
print(response.status_code)
print(response.json())
