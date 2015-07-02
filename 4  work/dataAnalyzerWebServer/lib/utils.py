# coding=utf-8

from wtforms.form import Form

class WTForm(Form):
    """
    Quick example::
        from wtforms import TextField, validators
        from ui import WTForm

        class SampleForm(WTForm):
            username = TextField('Username', [
                validators.Length(min=4, message="Too short")
                ])

            email = TextField('Email', [
                validators.Length(min=4, message="Not a valid mail address"),
                validators.Email()
                ])

    Then, in the `RequestHandler`::

        def get(self):
            ui = SampleForm(self)
            if ui.validate():
                # do something with ui.username or ui.email
                pass
            self.render('template.html', ui=ui)
    """
    def __init__(self, formdata=None, obj=None, prefix='', **kwargs):
        self._handler = formdata
		# 第一个参数是list类型，需要用包装器转换，先不细究，安装python IDE Pycharm可以查看源码
        super(WTForm, self).__init__(TornadoInputWrapper(formdata),
            obj=obj, prefix=prefix, **kwargs)

    def _get_translations(self):
        return TornadoLocaleWrapper(self._handler.get_user_locale())


class TornadoInputWrapper(object):
    def __init__(self, handler):
        self._handler = handler

    def __iter__(self):
        return iter(self._handler.request.arguments)

    def __len__(self):
        return len(self._handler.request.arguments)

    def __contains__(self, name):
        if name in self._handler.request.arguments:
            return True
        return False

    def getlist(self, name):
        return self._handler.get_arguments(name)


class TornadoLocaleWrapper(object):

    def __init__(self, locale):
        self.locale = locale

    def gettext(self, message):
        return self.locale.translate(message) if self.locale else message

    def ngettext(self, message, plural_message, count):
        return self.locale.translate(message, plural_message, count) if self.locale else message
