import requests
from random import randint

def generate_url(base_url, endpoint):
    if "{id}" in endpoint:
        endpoint = endpoint.replace("{id}", str(randint(1, 100)))
    return base_url + endpoint

def check_endpoints(base_url, endpoints, output_file='routes.txt'):
    available_routes = []
    methods = ['GET', 'POST', 'PUT', 'DELETE']  

    for endpoint in endpoints:
        for method in methods:
            url = generate_url(base_url, endpoint)
            try:
                response = requests.request(method, url)
                if response.status_code == 200:
                    print(f"{method} - Endpoint disponível: {url}")
                    available_routes.append(f"{method} - {url}")
                else:
                    print(f"{method} - Endpoint não encontrado: {url} (Status: {response.status_code})")
            except requests.RequestException as e:
                print(f"{method} - Erro ao tentar acessar {url}: {e}")

    with open(output_file, 'w') as file:
        for route in available_routes:
            file.write(route + "\n")

def main():
    base_url = "https://api.exemplo.com"

    endpoints = [
        "/users", "/users/{id}", "/users/profile", "/users/login", "/users/logout",
        "/users/register", "/users/reset-password", "/users/activate", "/users/permissions", "/users/roles",
        "/products", "/products/{id}", "/products/categories", "/products/search", "/products/{id}/reviews", "/products/{id}/related",
        "/orders", "/orders/{id}", "/orders/{id}/status", "/orders/{id}/items", "/orders/{id}/track",
        "/auth/login", "/auth/logout", "/auth/register", "/auth/refresh-token", "/auth/forgot-password", "/auth/reset-password", "/auth/verify-email",
        "/profile", "/profile/settings", "/profile/avatar", "/profile/password", "/profile/notifications",
        "/docs", "/swagger", "/openapi", "/metadata", "/health-check",
        "/settings", "/permissions", "/permissions/{id}", "/roles", "/roles/{id}",
        "/comments", "/comments/{id}", "/comments/{id}/replies",
        "/notifications", "/notifications/{id}", "/notifications/unread",
        "/messages", "/messages/{id}", "/messages/unread", "/messages/send",
        "/categories", "/categories/{id}", "/categories/{id}/products",
        "/tags", "/tags/{id}", "/tags/{id}/products",
        "/cart", "/cart/items", "/cart/add", "/cart/remove", "/cart/checkout",
        "/favorites", "/favorites/{id}", "/favorites/add", "/favorites/remove",
        "/payments", "/payments/{id}", "/payments/intent", "/payments/capture", "/payments/refund"
    ]

    check_endpoints(base_url, endpoints)

if __name__ == "__main__":
    main()
