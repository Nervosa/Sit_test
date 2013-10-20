from django.forms.widgets import TextInput


class ColorWidget(TextInput):

    class Media:
        css = {
            'all': ('/static/css/colorpicker.css', '/static/css/bootstrap2.css')
        }
        js = ('/static/js/jquery.js',
              '/static/js/create_colorpicker.js',
              '/static/js/bootstrap-colorpicker.js',
        )

    def render(self, name, value, attrs=None):
        pass