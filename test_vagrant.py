def test_package_docker(host):
  assert host.package('docker-ce').is_installed


def test_service_docker(host):
  assert host.service('docker').is_running


def test_helloworld_container(host):
  command = host.command('sudo docker inspect --format "{{.State.Status}}" helloworld')
  assert command.stdout == 'running\n'
  assert command.rc == 0
