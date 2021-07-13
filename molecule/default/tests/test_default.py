import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_tcp_timestamps_disabled(host):
    assert not host.sysctl("net.ipv4.tcp_timestamps")
