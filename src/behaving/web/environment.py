from urllib2 import URLError


def before_all(context):
    context.default_browser = ''
    if not hasattr(context, 'attachment_dir'):
        context.attachment_dir = '/'


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    context.browser = None
    context.browsers = dict()


def after_feature(context, feature):
    pass


def after_scenario(context, scenario):
    for browser in context.browsers.values():
        browser.quit()

    if context.browser is not None:
        try:
            context.browser.quit()
        except URLError:
            pass


def after_all(context):
    pass
