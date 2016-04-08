import os

from behave import step
from behaving.web.steps.basic import _retry


@step(u'the file "{filename}" should have been downloaded within {timeout} seconds')
def verify_download(context, filename, timeout):
    path = os.path.join(context.download_dir, filename)

    def check():
        return os.path.exists(path)

    assert _retry(check, timeout), u'Alert not found'
