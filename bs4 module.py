Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import bs4
import requests
res = requests.get("https://www.amazon.in")
Traceback (most recent call last):
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connection.py", line 790, in connect
    sock_and_verified = _ssl_wrap_socket_and_match_hostname(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connection.py", line 969, in _ssl_wrap_socket_and_match_hostname
    ssl_sock = ssl_wrap_socket(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\util\ssl_.py", line 480, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls, server_hostname)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\util\ssl_.py", line 524, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
  File "C:\Program Files\Python313\Lib\ssl.py", line 455, in wrap_socket
    return self.sslsocket_class._create(
  File "C:\Program Files\Python313\Lib\ssl.py", line 1076, in _create
    self.do_handshake()
  File "C:\Program Files\Python313\Lib\ssl.py", line 1372, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
urllib3.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\adapters.py", line 667, in send
    resp = conn.urlopen(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='www.amazon.in', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    res = requests.get("https://www.amazon.in")
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\adapters.py", line 698, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='www.amazon.in', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)')))
res = requests.get("https://www.amazon.in")
Traceback (most recent call last):
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connection.py", line 790, in connect
    sock_and_verified = _ssl_wrap_socket_and_match_hostname(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connection.py", line 969, in _ssl_wrap_socket_and_match_hostname
    ssl_sock = ssl_wrap_socket(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\util\ssl_.py", line 480, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls, server_hostname)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\util\ssl_.py", line 524, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
  File "C:\Program Files\Python313\Lib\ssl.py", line 455, in wrap_socket
    return self.sslsocket_class._create(
  File "C:\Program Files\Python313\Lib\ssl.py", line 1076, in _create
    self.do_handshake()
  File "C:\Program Files\Python313\Lib\ssl.py", line 1372, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
urllib3.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\adapters.py", line 667, in send
    resp = conn.urlopen(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='www.amazon.in', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    res = requests.get("https://www.amazon.in")
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\adapters.py", line 698, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='www.amazon.in', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)')))
res = requests.get("https://github.com")
soup = bs4.BeautifulSoup(res.text)
soup = bs4.BeautifulSoup(res.text, "html.parser")
soup.select('span')

soup.select('span')[0].text
'\n\n'
soup.select('span')[0].text.strip()
''

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    
def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('//*[@id="CardInstanceoaJPsRaDelBQbpL-S6dSMA"]/div[2]/div/div[2]/span/span[1]/span[2]/span[2]/text()')
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.in')
Traceback (most recent call last):
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connection.py", line 790, in connect
    sock_and_verified = _ssl_wrap_socket_and_match_hostname(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connection.py", line 969, in _ssl_wrap_socket_and_match_hostname
    ssl_sock = ssl_wrap_socket(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\util\ssl_.py", line 480, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls, server_hostname)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\util\ssl_.py", line 524, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
  File "C:\Program Files\Python313\Lib\ssl.py", line 455, in wrap_socket
    return self.sslsocket_class._create(
  File "C:\Program Files\Python313\Lib\ssl.py", line 1076, in _create
    self.do_handshake()
  File "C:\Program Files\Python313\Lib\ssl.py", line 1372, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 488, in _make_request
    raise new_e
urllib3.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\adapters.py", line 667, in send
    resp = conn.urlopen(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\connectionpool.py", line 841, in urlopen
    retries = retries.increment(
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='www.amazon.in', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    price = getAmazonPrice('https://www.amazon.in')
  File "<pyshell#19>", line 2, in getAmazonPrice
    res = requests.get(productUrl)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\prasarav\AppData\Roaming\Python\Python313\site-packages\requests\adapters.py", line 698, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='www.amazon.in', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)')))
