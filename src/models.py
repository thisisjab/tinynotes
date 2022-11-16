from utils import datetime_tools


class Tag:
    def __init__(self, id_: int, name: str) -> None:
        self.id_ = id_
        self.name = name

    @property
    def id_(self):
        return self._id

    @id_.setter
    def id_(self, value: int):
        if not isinstance(value, int):
            raise ValueError("`id_` must be an integer.")

        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("`title` must be a string.")

        if len(value.strip()) == 0:
            raise ValueError("`title` cannot be a empty.")

        self._title = value.strip()


class Note:
    def __init__(self, id_: int, title: str, last_edit: str, content: str = None) -> None:
        # TODO: add `tag_id` property
        self.id_ = id_
        self.title = title
        self.last_edit = last_edit
        self.content = content

    @property
    def id_(self):
        return self._id

    @id_.setter
    def id_(self, value: int):
        if not isinstance(value, int):
            raise ValueError("`id_` must be an integer.")

        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str):
            raise ValueError("`title` must be a string.")

        if len(value.strip()) == 0:
            raise ValueError("`title` cannot be a empty.")

        self._title = value.strip()

    @property
    def last_edit(self):
        return self._last_edit

    @last_edit.setter
    def last_edit(self, value: str):
        if not isinstance(value, str):
            raise ValueError("`last_edit` must be a string.")

        if not datetime_tools.is_valid_datetime_str(value):
            raise ValueError("`last_edit` is not correctly formatted.")

        self._last_edit = value.strip()

    @property
    def content(self):
        if hasattr(self, "_content"):
            return self._content

        return ""

    @content.setter
    def content(self, value: str):
        if value is None:
            self._content = ""
        elif not isinstance(value, str):
            raise ValueError("`content` must be a string.")

        self._content = value
