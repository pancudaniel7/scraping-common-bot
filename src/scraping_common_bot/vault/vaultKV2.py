from hvac import Client


def read_secrets(url: str,
                 token: str,
                 path: str,
                 client_cert_path: str = None,
                 client_key_path: str = None,
                 server_cert_path: str = None):
    return Client(url=url,
                  token=token,
                  cert=(client_cert_path, client_key_path),
                  verify=server_cert_path) \
        .secrets.kv.v2.read_secret_version(path=path)
