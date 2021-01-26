import datetime
import re
from typing import Any

class ValidationError(Exception):
    pass


class ValidationField:
    def __init__(self, default=None, blank=False, **kwargs):
        self.default = default
        self.blank = blank
        self.__dict__.update(kwargs)

    def validate(self, val):
        if val is None and self.blank is False:
            raise ValidationError


class CharField(ValidationField):
    def __init__(self, min_length=0, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, value):
        super().validate(value)

        if value is None:
            return

        if not isinstance(value, str):
            raise ValidationError

        if self.min_length is not None and len(value) < self.min_length:
            raise ValidationError

        if self.max_length is not None and self.max_length < len(value):
            raise ValidationError


class IntegerField(ValidationField):
    def __init__(self, min_value=None, max_value=None, **kwargs):
        super().__init__(**kwargs)
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        super().validate(value)

        if value is None:
            return

        if isinstance(value, bool):
            raise ValidationError

        if not isinstance(value, int):
            raise ValidationError

        if self.min_value is not None and value < self.min_value:
            raise ValidationError

        if self.max_value is not None and self.max_value < value:
            raise ValidationError


class BooleanField(ValidationField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate(self, value):
        super().validate(value)

        if value is None:
            return

        if not isinstance(value, bool):
            raise ValidationError


class DateTimeField(ValidationField):
    def __init__(self, default=None, auto_now=False, **kwargs):
        super().__init__(**kwargs)
        self.auto_now = auto_now
        self._default = default

    def __getattribute__(self, name: str) -> Any:
        if name == 'default':
            if self._default is None and self.auto_now is True:
                return datetime.datetime.now()
            else:
                return self._default
        return super().__getattribute__(name)

    def validate(self, value):
        super().validate(value)

        if value is None:
            return

        if not isinstance(value, datetime.datetime):
            raise ValidationError


class EmailField(ValidationField):
    def __init__(self, min_length=0, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, value):
        super().validate(value)

        if value is None:
            return

        if not isinstance(value, str):
            raise ValidationError

        if self.min_length is not None and len(value) < self.min_length:
            raise ValidationError

        if self.max_length is not None and self.max_length < len(value):
            raise ValidationError

        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValidationError


class Model:
    def __init__(self, **kwargs):
        for i in [i for i in dir(self.__class__) if i.startswith('_f_')]:
            attr = getattr(self.__class__, i)
            setattr(self, i[3:], attr.default)

        for i, j in kwargs.items():
            setattr(self, i, j)

    def __init_subclass__(cls) -> None:
        for i in [i for i in dir(cls) if not i.startswith('_')]:
            attr = getattr(cls, i)
            if isinstance(attr, (CharField, EmailField,
                                 IntegerField, BooleanField, DateTimeField)):
                delattr(cls, i)
                setattr(cls, '_f_' + i, attr)
        super().__init_subclass__()

    def validate(self):
        for i in [i for i in dir(self.__class__) if i.startswith('_f_') and hasattr(self, i[3:])]:
            class_attr = getattr(self.__class__, i)
            instance_attr = getattr(self, i[3:])
            class_attr.validate(instance_attr)
