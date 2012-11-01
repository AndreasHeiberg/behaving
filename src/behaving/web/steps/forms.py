import os
from behave import when
from behaving.personas.persona import persona_vars


@when(u'I fill in "{name}" with "{value}"')
@persona_vars
def i_fill_in_field(context, name, value):
    context.browser.fill(name, value)


@when(u'I choose "{value}" from "{name}"')
def i_choose_in_radio(context, name, value):
    context.browser.choose(name, value)


@when(u'I check "{name}"')
def i_check(context, name):
    context.browser.check(name)


@when(u'I uncheck "{name}"')
def i_uncheck(context, name):
    context.browser.uncheck(name)


@when(u'I select "{value}" from "{name}"')
def i_select(context, value, name):
    context.browser.select(name, value)


@when(u'I press "{name}"')
def i_press(context, name):
    button = context.browser.find_by_id(name) or \
             context.browser.find_by_name(name) or \
             context.browser.find_link_by_text(name) or \
             context.browser.find_link_by_partial_text(name) or \
             context.browser.find_by_xpath("//button[text()='%s']" % name) or \
             context.browser.find_by_xpath("//button[contains(text(), '%s')]" % name)
    assert button, u'Element not found'
    button.first.click()


@when('I attach the file "{path}" to "{name}"')
def i_attach(context, name, path):
    if not os.path.exists(path):
        path = os.path.join(context.attachment_dir, path)
        if not os.path.exists(path):
            assert False
    context.browser.attach_file(name, path)
