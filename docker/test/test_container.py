import logging

import conu
import pytest


imagename = 'helloworld'
tag = '0.0.1'


@pytest.fixture()
def container():
  backend = conu.DockerBackend(logging_level = logging.DEBUG).__enter__()
  image = backend.ImageClass(imagename, tag = tag)
  container = image.run_via_binary()
  yield container
  container.delete(force = True)
  backend._clean()


def test_http(container):
  port = 80
  container.wait_for_port(port)
  http_response = container.http_request(port = port)
  assert http_response.text == 'Hello World.\n'
