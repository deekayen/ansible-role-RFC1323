# deekayen.rfc1323

[![CI](https://github.com/deekayen/ansible-role-RFC1323/actions/workflows/ci.yml/badge.svg)](https://github.com/deekayen/ansible-role-RFC1323/actions/workflows/ci.yml) [![Ansible Galaxy](https://img.shields.io/badge/galaxy-deekayen.rfc1323-blue.svg)](https://galaxy.ansible.com/ui/standalone/roles/deekayen/rfc1323/) [![Project Status: Inactive – The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.](https://www.repostatus.org/badges/latest/inactive.svg)](https://www.repostatus.org/#inactive) ![BSD 3-Clause license](https://img.shields.io/badge/license-BSD%203--Clause-blue)

An Ansible role that sets the Linux `net.ipv4.tcp_timestamps` kernel parameter, which controls the TCP timestamp option from [RFC 1323](https://www.ietf.org/rfc/rfc1323.txt) (obsoleted by [RFC 7323](https://www.rfc-editor.org/rfc/rfc7323)). By default it turns timestamps off, so remote hosts can't estimate system uptime from them. Vulnerability scanners report that disclosure with a CVSS score of 2.6.

The role applies the value to the running kernel with `ansible.posix.sysctl` and persists it in `/etc/sysctl.d/99-rfc1323.conf`. A task before it creates `/etc/sysctl.d` if the directory is missing. The Galaxy name is lowercase `deekayen.rfc1323`, while the repository is `ansible-role-RFC1323`.

## Requirements

- ansible-core 2.15 or newer on the controller.
- The `ansible.posix` collection: `ansible-galaxy collection install ansible.posix`.
- Privilege escalation on the target. Run the play with `become: true`; the role writes under `/etc` and changes a kernel parameter.

## Supported platforms

From `meta/main.yml`, and each one runs through Molecule in CI:

| Platform | Versions |
| --- | --- |
| EL (Rocky Linux in CI) | 9, 10 |
| Amazon Linux | 2023 |
| Debian | 12 (bookworm), 13 (trixie) |
| Ubuntu | 22.04 (jammy), 24.04 (noble), 26.04 (resolute) |

## Installation

From Ansible Galaxy:

```bash
ansible-galaxy role install deekayen.rfc1323
ansible-galaxy collection install ansible.posix
```

Or pin it in `requirements.yml`:

```yaml
---
roles:
  - name: deekayen.rfc1323
    src: https://github.com/deekayen/ansible-role-RFC1323.git
    scm: git
    version: main

collections:
  - name: ansible.posix
```

```bash
ansible-galaxy install -r requirements.yml
```

## Role variables

| Variable | Default | Description |
| --- | --- | --- |
| `tcp_timestamps_enabled` | `false` | Boolean. `false` writes `net.ipv4.tcp_timestamps = 0`; `true` writes `1`. |

## Behavior

- Releases 1.0.1 and earlier wrote the setting to `/etc/sysctl.conf`, the `ansible.posix.sysctl` default. The current role writes only `/etc/sysctl.d/99-rfc1323.conf` and leaves any line an older release added to `/etc/sysctl.conf` in place.
## Dependencies

None.

## Example playbook

```yaml
---
- name: Stop TCP timestamp uptime disclosure.
  hosts: internet_facing

  become: true

  roles:
    - deekayen.rfc1323
```

## Tags

| Tag | Tasks |
| --- | --- |
| `configure`, `security` | The sysctl task. The `/etc/sysctl.d` directory task is untagged. |

## Development

CI runs on every push to `main` and every pull request (see `.github/workflows/ci.yml`):

1. Lint: installs `molecule/default/requirements.yml`, then runs `ansible-lint --profile production` and `flake8 molecule/`.
2. Molecule: converge, idempotence, and testinfra verification in Docker against each distribution in the table above.

To run the same checks locally with Docker available:

```bash
pip3 install ansible-core ansible-lint flake8 molecule "molecule-plugins[docker]" docker pytest-testinfra
ansible-galaxy install -r molecule/default/requirements.yml
ansible-lint --profile production
flake8 molecule/
MOLECULE_DISTRO=rockylinux9 molecule test
```

`MOLECULE_DISTRO` selects a `geerlingguy/docker-<distro>-ansible` image. The values CI uses are `rockylinux9`, `rockylinux10`, `amazonlinux2023`, `ubuntu2204`, `ubuntu2404`, `ubuntu2604`, `debian12`, and `debian13`. The testinfra checks in `molecule/default/tests/test_default.py` confirm that the running kernel reports `net.ipv4.tcp_timestamps` as `0` and that `/etc/sysctl.d/99-rfc1323.conf` has mode `0644` and contains `net.ipv4.tcp_timestamps = 0`.

The repository also has a `.pre-commit-config.yaml`; run `pre-commit run --all-files` before pushing.

### Repository layout

| Path | Purpose |
| --- | --- |
| `tasks/main.yml` | Creates `/etc/sysctl.d` and sets the sysctl. |
| `defaults/main.yml` | The one user-facing variable. |
| `meta/main.yml` | Galaxy metadata and the supported platform list. |
| `meta/argument_specs.yml` | Argument spec for `tcp_timestamps_enabled`. |
| `molecule/default/` | Molecule scenario: `prepare.yml`, `converge.yml`, collection requirements, and testinfra tests. |
| `.github/workflows/` | `ci.yml` for lint and Molecule, `release.yml` for Galaxy import. |

## Releases

Pushing a git tag runs `.github/workflows/release.yml`, which imports the tagged commit into Ansible Galaxy as `deekayen.rfc1323`. The import needs a `GALAXY_API_KEY` repository or organization secret.

## License

BSD 3-Clause. See [LICENSE](LICENSE).

## Author

[David Norman](https://github.com/deekayen). Sponsorship links are in [.github/FUNDING.yml](.github/FUNDING.yml).
