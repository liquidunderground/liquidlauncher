product_name = "LiquidLauncher"
product_version = "v1.0.1"
version_check_url = "https://api.github.com/repos/liquidunderground/liquidlauncher/releases/latest"

http_headers = {'User-Agent': '{}/{}'.format(product_name, product_version) }

def set_http_header(name, value):
    print("ll_info.http_headers[{}] = {}\n".format(name, value))
    http_headers[name] = value
