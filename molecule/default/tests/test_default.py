"""Testinfra checks for the RFC1323 role."""

import re


def test_tcp_timestamps_disabled(host):
    assert host.sysctl("net.ipv4.tcp_timestamps") == 0


def test_setting_persisted(host):
    conf = host.file("/etc/sysctl.d/99-rfc1323.conf")
    assert conf.mode == 0o644
    assert re.search(
        r"^net\.ipv4\.tcp_timestamps\s*=\s*0$", conf.content_string, re.M
    )
