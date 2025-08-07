import tldextract
import difflib

KNOW_DOMAINS = ["google.com", "paypal.com", "apple.com", "amazon.com", "facebook.com"]

def is_punycode(url):
    return 'xn--' in url

def extract_domain(url):
    ext = tldextract.extract(url)
    return f"{ext.domain}.{ext.suffix}"

def is_similar_to_known_brand(domain):
    for know in KNOW_DOMAINS:
        ratio = difflib.SequenceMatcher(None, domain, know).ratio()
        if ratio > 0.8 and domain != know:
            return True, know, ratio
    return False, None, 0

def analyze_url(url):
    result = {}
    domain = extract_domain(url)
    result['domain'] = domain
    result['pycode'] = is_punycode(url)
    sim, brand, score = is_similar_to_known_brand(domain)
    result['suspicious'] = sim
    result['brand'] = brand
    result['similarity'] = round(score * 100, 2)
    return result