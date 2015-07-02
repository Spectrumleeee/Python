from wtforms import StringField, validators

from lib.utils import WTForm

class SearchForm(WTForm):
    deviceid = StringField('deviceid', [
        validators.Length(min = 0, max = 40, message = "deviceid length is wrong."),
    ])

    starttime = StringField('starttime', [
        validators.DataRequired(message = "starttime is required."),
        validators.length(min = 14, max = 14, message = "length of password is 14 like 20150508111156")
    ])

    finishtime = StringField('finishtime', [
        validators.DataRequired(message = "finishtime is required."),
        validators.length(min = 14, max = 14, message = "length of password is 14 like 20150508111156")
    ])
