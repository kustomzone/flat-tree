"""Version test module."""


def test_version_fails_gracefully(mocker):
    target = 'pkg_resources.get_distribution'
    with mocker.patch(target, side_effect=Exception()):
        from flat_tree.__init__ import __version__

        assert __version__ == 'unknown'
