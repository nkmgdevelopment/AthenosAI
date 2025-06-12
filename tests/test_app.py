import sys, os; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import app

def test_index():
    client = app.app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.get_json().get('message') == 'Welcome to the MYSTK creators portal'

def test_learn():
    client = app.app.test_client()
    resp = client.get('/learn')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data.get('section') == 'learn'


def test_metrics():
    client = app.app.test_client()
    resp = client.get('/metrics')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data.get('section') == 'metrics'


def test_support():
    client = app.app.test_client()
    resp = client.get('/support')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data.get('section') == 'support'
