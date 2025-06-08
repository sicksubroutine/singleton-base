import nox

VERSIONS = ["3.9", "3.10", "3.11", "3.12", "3.13"]


@nox.session(python=VERSIONS, venv_backend="uv")
def test_all_tests(session):
    session.install("-e", ".")
    session.install("pytest")
    session.run("pytest")
