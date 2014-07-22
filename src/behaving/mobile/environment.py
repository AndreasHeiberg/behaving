from . import setup, teardown


def before_all(context):
    setup(context)


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def after_feature(context, feature):
    pass


def after_scenario(context, scenario):
    if hasattr(context, 'iosdriver'):
        context.iosdriver.quit()
        del context.iosdriver


def after_all(context):
    teardown(context)
