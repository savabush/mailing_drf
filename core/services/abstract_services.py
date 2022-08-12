from abc import ABC, abstractmethod


class AbstractServices(ABC):

    @abstractmethod
    def validate_data_for_post_method(cls, *args):
        pass

    @abstractmethod
    def validate_data_for_get_method_to_get_list(cls, *args):
        pass

    @abstractmethod
    def validate_data_for_get_method_to_get_detail_info(cls, *args):
        pass

    @abstractmethod
    def validate_data_for_put_method(cls, *args):
        pass

    @abstractmethod
    def create(cls, *args):
        pass

    @abstractmethod
    def update(self, *args):
        pass

    @abstractmethod
    def delete(self, *args):
        pass