from django.test import TestCase


class GetTestInfoMixin:
    _show_flg = False

    def assertEqual(first, second, msg=None):
        if self._show_flg:
            pass
        else:
            super(GetTestInfoMixin, self).super(first, second, msg)

class GetTestInfoTestCase(GetTestInfoMixin, TestCase):
    pass
